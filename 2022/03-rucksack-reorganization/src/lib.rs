use std::collections::HashSet;
use std::error::Error;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;

pub fn get_priorities(input: PathBuf) -> Result<(Vec<u8>, Vec<u8>), Box<dyn Error>> {
    let file = std::fs::File::open(input)?;
    let reader = BufReader::new(file);

    let mut priorities = Vec::new();
    let mut priorities2 = Vec::new();
    let mut rucksacks = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let compartments = line.split_at(line.len() / 2);
        let compartments = (
            HashSet::<char>::from_iter(compartments.0.chars()),
            HashSet::from_iter(compartments.1.chars()),
        );
        priorities.push(decode_priorities(
            compartments.0.intersection(&compartments.1).nth(0),
        )?);

        rucksacks.push(HashSet::from_iter(line.chars()));
        if rucksacks.len() == 3 {
            let mut badges: HashSet<char> = rucksacks.pop().unwrap();
            badges.retain(|i| rucksacks.iter().all(|rucksack| rucksack.contains(i)));
            priorities2.push(decode_priorities(badges.iter().nth(0))?);
            /*priorities2.push(decode_priorities(
                rucksacks
                    .iter()
                    .skip(1)
                    .fold(rucksacks[0].clone(), |a: HashSet<char>, b| {
                        a.intersection(b).cloned().collect()
                    })
                    .iter()
                    .nth(0),
            )?);*/
            rucksacks.clear();
        }
    }
    Ok((priorities, priorities2))
}

fn decode_priorities(decode: Option<&char>) -> Result<u8, Box<dyn Error>> {
    Ok(match decode {
        Some(c @ 'a'..='z') => *c as u8 - 'a' as u8 + 1,
        Some(c @ 'A'..='Z') => *c as u8 - 'A' as u8 + 27,
        Some(c) => return Err(format!("Bad item: {c}").into()),
        None => return Err("Missing item".into()),
    })
}

pub fn get_sum(priorities: Vec<u8>) -> u32 {
    priorities.iter().map(|&n| n as u32).sum::<u32>()
}

#[cfg(test)]
mod tests {
    use super::*;

    fn example() -> (Vec<u8>, Vec<u8>) {
        get_priorities(PathBuf::from("example")).unwrap()
    }

    #[test]
    fn example_get_priorities() {
        assert_eq!(example().0, [16, 38, 42, 22, 20, 19]);
    }

    #[test]
    fn example_get_sum() {
        assert_eq!(get_sum(example().0), 157);
    }

    #[test]
    fn example_get_priorities2() {
        assert_eq!(example().1, [18, 52]);
    }

    #[test]
    fn example_get_sum2() {
        assert_eq!(get_sum(example().1), 70);
    }
}
