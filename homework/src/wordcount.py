## wordcount.py

import argparse
import sys


def parse_args():

    parser = argparse.ArgumentParser(description="Count words in files.")

    parser.add_argument(
        "input",
        type=str,
        help="Path to the input folder containing files to process",
    )
    parser.add_argument(
        "output",
        type=str,
        help="Path to the output folder for results",
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output

def read_all_files(input_folder):
    pass

def main():
    input_folder, output_folder = parse_args()
    lines = read_all_files(input_folder)