use clap::Parser;
use std::path::PathBuf;
use std::process;

/// Count total calories from a file and output the highest
#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Args{
    /// The file to use as input
    input: PathBuf
}

fn main() {
    let args = Args::parse();

    let totals = calorie_counting::get_totals(args.input).unwrap_or_else(|err| {
        eprintln!("Problem getting the total Calories: {err}");
        process::exit(1);
    });

    let max_total = calorie_counting::get_max(&totals);
    println!("Total Calories from Elf with most Calories: {max_total}");

    let top_3_sum = calorie_counting::get_topn_sum(totals, 3);
    println!("Sum of Calories from top 3 Elves {top_3_sum}");
}

