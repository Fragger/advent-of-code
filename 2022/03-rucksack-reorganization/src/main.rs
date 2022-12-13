use clap::Parser;
use std::path::PathBuf;
use std::process;

/// Calculate sum of priorities of mismatched items in rucksacks
#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// The file to use as input
    input: PathBuf,
}

fn main() {
    let args = Args::parse();

    let priorities = rucksack_reorganization::get_priorities(args.input).unwrap_or_else(|err| {
        eprintln!("Problem getting the item priorities: {err}");
        process::exit(1);
    });

    let sum = rucksack_reorganization::get_sum(priorities.0);
    println!("Sum of priorities: {sum}");

    let sum2 = rucksack_reorganization::get_sum(priorities.1);
    println!("Sum of group priorities: {sum2}");
}
