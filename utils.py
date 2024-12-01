import sys
import time
import math
from enum import Enum
from pathlib import Path
from typing import Callable, Any, List


class InputType(Enum):
    EXAMPLE = "example"
    MAIN = "main"


def load_input(day: int, input_type: InputType = InputType.MAIN) -> str:
    """
    Load the input for a specific day and type
    """
    file_name = "example.txt" if input_type == InputType.EXAMPLE else "input.txt"
    input_file = Path(f"./Day{day:02}/{file_name}")

    if input_file.exists():
        with open(input_file, "r") as f:
            return f.read().strip()
    else:
        raise FileNotFoundError(f"Input file for day {day:02} not found!")


def time_solution(func: Callable, *args, **kwargs) -> Any:
    """
    Measure the execution time of a solution function
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()

    execution_time_sec = end_time - start_time
    execution_time_ms = execution_time_sec * 1_000
    execution_time_us = execution_time_sec * 1_000_000

    print(f"Execution time:")
    print(f"- {execution_time_sec:.3f} sec")
    print(f"- {execution_time_ms:.2f} ms")
    print(f"- {math.ceil(execution_time_us)} µs")
    return result
de

def parse_lines(input_str: str, delimiter: str = None) -> list[list[str]] | list[str]:
    """
    Parse input into lines, optionally splitting each line by a delimiter
    """
    lines = input_str.strip().splitlines()
    if delimiter:
        return [line.split(delimiter) for line in lines]
    return lines


def parse_integers(input_str: str) -> List[int]:
    """
    Parse input into a list of integers
    """
    return [int(x) for x in input_str.strip().splitlines()]


def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """
    Chunk a list into smaller lists of a given size
    """
    return [data[i:i + size] for i in range(0, len(data), size)]


def print_grid(grid: List[List[Any]]) -> None:
    """
    Print a 2D grid for debugging purposes
    """
    for row in grid:
        print("".join(str(cell) for cell in row))


def setup_day_folder(day: int) -> None:
    """
    Create a folder for the given day with zero-padded numbering, and
    initialize input.txt, example.txt, and main.py with user-provided data

    Args:
        day (int): The day number (1-24)
    """
    folder_path = Path(f"./Day{day:02}")
    folder_path.mkdir(parents=True, exist_ok=True)

    print(f"Input: ")
    input_data = sys.stdin.read().strip()

    print(f"Example: ")
    example_data = sys.stdin.read().strip()

    input_file = folder_path / "input.txt"
    example_file = folder_path / "example.txt"
    main_file = folder_path / "main.py"

    with open(input_file, "w") as f:
        f.write(input_data)

    with open(example_file, "w") as f:
        f.write(example_data)

    with open(main_file, "w") as f:
        pass


class SolutionBase:
    """
    Base class for Advent of Code solutions
    Provides structure for each day's solution
    """

    def __init__(self, day: int, input_type: InputType = InputType.MAIN):
        self.day = day
        self.input_type = input_type
        self.input_data = load_input(day, input_type)

    def part_one(self) -> Any:
        """
        Solve part one of the day's problem.
        """
        raise NotImplementedError("Part one is not implemented.")

    def part_two(self) -> Any:
        """
        Solve part two of the day's problem.
        """
        raise NotImplementedError("Part two is not implemented.")

    def solve(self) -> None:
        """
        Solve both parts and print results.
        """
        print(f"Day {self.day:02} - {self.input_type.value.capitalize()} Input")
        print("Part One:")
        result_one = time_solution(self.part_one)
        print(f"Result: {result_one}")

        print("\nPart Two:")
        result_two = time_solution(self.part_two)
        print(f"Result: {result_two}")
