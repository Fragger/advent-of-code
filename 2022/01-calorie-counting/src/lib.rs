use std::error::Error;
use std::io::{BufRead, BufReader};
use std::path::PathBuf;

pub fn get_totals(input: PathBuf) -> Result<Vec<u32>, Box<dyn Error>> {
    let file = std::fs::File::open(input)?;
    let reader = BufReader::new(file);

    let mut totals = Vec::new();
    let mut total = 0;

    for line in reader.lines() {
        let line = line?;
        if line.is_empty() {
            totals.push(total);
            total = 0;
        } else {
            total += line.parse::<u32>()?;
        }
    }
    totals.push(total);

    Ok(totals)
}

pub fn get_max(totals: &Vec<u32>) -> u32 {
    *totals.iter().max().unwrap()
}

pub fn get_topn_sum(mut totals: Vec<u32>, n: usize) -> u32 {
    totals.sort();
    totals.iter().rev().take(n).sum::<u32>()
}

#[cfg(test)]
mod tests {
    use super::*;

    fn example() -> Vec<u32> {
        get_totals(PathBuf::from("example")).unwrap()
    }

    #[test]
    fn example_totals() {
        assert_eq!(example(), [6000, 4000, 11000, 24000, 10000]);
    }

    #[test]
    fn example_max() {
        assert_eq!(get_max(&example()), 24000);
    }

    #[test]
    fn example_topn_sum() {
        assert_eq!(get_topn_sum(example(), 3), 45000);
    }
}
