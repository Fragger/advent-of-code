use std::error::Error;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;

#[derive(Eq, PartialEq, Clone, Copy)]
enum Shape {
    Rock,
    Paper,
    Scissors,
}

impl Shape {
    fn win(&self) -> Self {
        match self {
            Self::Rock => Self::Paper,
            Self::Paper => Self::Scissors,
            Self::Scissors => Self::Rock,
        }
    }
    fn lose(&self) -> Self {
        match self {
            Self::Rock => Self::Scissors,
            Self::Paper => Self::Rock,
            Self::Scissors => Self::Paper,
        }
    }
}

#[derive(Eq, PartialEq, Debug)]
enum Outcome {
    Lost,
    Draw,
    Win,
}

pub struct Round {
    opponent: Shape,
    selection: Shape,
}

impl Round {
    fn new(opponent: Shape, selection: Shape) -> Self {
        Self {
            opponent,
            selection,
        }
    }
    fn outcome(&self) -> Outcome {
        //if (self.opponent as u8 + 1) % 3 == self.selection as u8 { return Outcome::Win }
        if self.opponent.win() == self.selection {
            return Outcome::Win;
        }
        if self.opponent == self.selection {
            return Outcome::Draw;
        }
        Outcome::Lost
    }
    fn score(&self) -> u8 {
        self.selection as u8 + 1 + self.outcome() as u8 * 3
    }
}

pub fn get_total(rounds: Vec<Round>) -> u32 {
    rounds.iter().map(|r| r.score() as u32).sum()
}

pub fn get_rounds(input: PathBuf) -> Result<(Vec<Round>, Vec<Round>), Box<dyn Error>> {
    let file = std::fs::File::open(input)?;
    let reader = BufReader::new(file);

    let mut rounds = Vec::new();
    let mut rounds2 = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let opponent = match line.chars().nth(0) {
            Some('A') => Shape::Rock,
            Some('B') => Shape::Paper,
            Some('C') => Shape::Scissors,
            Some(c) => return Err(format!("Bad opponent choice: {c}").into()),
            None => return Err("Missing opponent choice".into()),
        };
        let selection = match line.chars().nth(2) {
            Some('X') => Shape::Rock,
            Some('Y') => Shape::Paper,
            Some('Z') => Shape::Scissors,
            Some(c) => return Err(format!("Bad selection choice: {c}").into()),
            None => return Err("Missing selection choice".into()),
        };
        let selection2 = match line.chars().nth(2) {
            Some('X') => opponent.lose(),
            Some('Y') => opponent,
            Some('Z') => opponent.win(),
            Some(c) => return Err(format!("Bad selection choice: {c}").into()),
            None => return Err("Missing selection choice".into()),
        };
        rounds.push(Round::new(opponent, selection));
        rounds2.push(Round::new(opponent, selection2));
    }

    Ok((rounds, rounds2))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_win_rock() {
        let round = Round::new(Shape::Scissors, Shape::Rock);
        assert_eq!(round.outcome(), Outcome::Win);
    }
    #[test]
    fn test_win_paper() {
        let round = Round::new(Shape::Rock, Shape::Paper);
        assert_eq!(round.outcome(), Outcome::Win);
    }
    #[test]
    fn test_win_scissors() {
        let round = Round::new(Shape::Paper, Shape::Scissors);
        assert_eq!(round.outcome(), Outcome::Win);
    }

    #[test]
    fn test_lose_rock() {
        let round = Round::new(Shape::Paper, Shape::Rock);
        assert_eq!(round.outcome(), Outcome::Lost);
    }
    #[test]
    fn test_lose_paper() {
        let round = Round::new(Shape::Scissors, Shape::Paper);
        assert_eq!(round.outcome(), Outcome::Lost);
    }
    #[test]
    fn test_lose_scissors() {
        let round = Round::new(Shape::Rock, Shape::Scissors);
        assert_eq!(round.outcome(), Outcome::Lost);
    }

    #[test]
    fn test_draw_rock() {
        let round = Round::new(Shape::Rock, Shape::Rock);
        assert_eq!(round.outcome(), Outcome::Draw);
    }
    #[test]
    fn test_draw_paper() {
        let round = Round::new(Shape::Paper, Shape::Paper);
        assert_eq!(round.outcome(), Outcome::Draw);
    }
    #[test]
    fn test_draw_scissors() {
        let round = Round::new(Shape::Scissors, Shape::Scissors);
        assert_eq!(round.outcome(), Outcome::Draw);
    }

    fn example_rounds() -> (Vec<Round>, Vec<Round>) {
        get_rounds(PathBuf::from("example")).unwrap()
    }

    #[test]
    fn test_example_rounds() {
        let scores: Vec<_> = example_rounds().0.iter().map(|r| r.score()).collect();
        assert_eq!(scores, [8, 1, 6]);
    }

    #[test]
    fn test_example_rounds_total() {
        assert_eq!(get_total(example_rounds().0), 15);
    }

    #[test]
    fn test_example_rounds2() {
        let scores: Vec<_> = example_rounds().1.iter().map(|r| r.score()).collect();
        assert_eq!(scores, [4, 1, 7]);
    }

    #[test]
    fn test_example_rounds_total2() {
        assert_eq!(get_total(example_rounds().1), 12);
    }
}
