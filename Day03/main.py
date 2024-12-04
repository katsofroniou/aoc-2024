from utils import SolutionBase
import re


class Day03Solution(SolutionBase):
    def __init__(self):
        super().__init__(day=3)

    def part_one(self) -> int:
        # define regex to find valid mul(x, y)
        valid_mul_pattern = r"mul\((\d+),(\d+)\)"

        # extract matches from input data
        matches = re.findall(valid_mul_pattern, self.input_data)

        # return the sum of products
        return sum(int(x) * int(y) for x, y in matches)

    def part_two(self) -> int:
        # regex patterns for valid mul(x, y), do(), and don't()
        valid_mul_pattern = r"mul\((\d+),(\d+)\)"
        enable_pattern = r"do\(\)"
        disable_pattern = r"don't\(\)"

        total = 0
        enabled = True

        # process input linearly
        # TODO check if refactorable
        tokens = re.split(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", self.input_data)
        for token in tokens:
            token = token.strip()
            if not token:
                continue

            if re.match(enable_pattern, token):
                enabled = True
            elif re.match(disable_pattern, token):
                enabled = False
            elif re.match(valid_mul_pattern, token) and enabled:
                x, y = map(int, re.findall(r"\d+", token))
                total += x * y

        return total


if __name__ == "__main__":
    solution = Day03Solution()
    solution.solve()
