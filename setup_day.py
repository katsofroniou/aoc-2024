from utils import setup_day_folder
import argparse

parser = argparse.ArgumentParser(description="Setup a folder for a specific Advent of Code day.")
parser.add_argument("day", type=int, help="The day number (1-25) to set up.")
args = parser.parse_args()

setup_day_folder(day=args.day)
print(f"Folder for Day {args.day:02} has been set up successfully.")
