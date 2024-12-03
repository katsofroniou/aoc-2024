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
        return 0


if __name__ == "__main__":
    solution = Day03Solution()
    solution.solve()
