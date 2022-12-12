use clap::Parser;
use std::path::PathBuf;
use std::process;

/// Calculate total score from following strategy guide file
#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Args{
    /// The file to use as input
    input: PathBuf
}

fn main() {
    let args = Args::parse();

    let (rounds, rounds2) = rock_paper_scissors::get_rounds(args.input).unwrap_or_else(|err| {
        eprintln!("Problem getting the results: {err}");
        process::exit(1);
    });

    let total = rock_paper_scissors::get_total(rounds);
    println!("Total score following stategy guide: {total}");

    let total2 = rock_paper_scissors::get_total(rounds2);
    println!("Total score following stategy guide with elfs instructions: {total2}");
}
