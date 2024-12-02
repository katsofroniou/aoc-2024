from utils import SolutionBase, parse_lines


def is_safe(levels):
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # check if all diffs are in the range [1, 3] or [-3, -1]
    if not all(1 <= abs(diff) <= 3 for diff in diffs):
        return False

    # check if all diffs are positive or all are negative
    if all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs):
        return True

    return False


class Day02Solution(SolutionBase):
    def __init__(self):
        super().__init__(day=2)

    def part_one(self) -> int:
        # split into lines of numbers
        reports = parse_lines(self.input_data, delimiter=None)

        # convert each line to a list of ints
        reports = [list(map(int, line.split())) for line in reports]

        return sum(1 for report in reports if is_safe(report))

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    solution = Day02Solution()
    solution.solve()
