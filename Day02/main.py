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


def is_safe_with_dampener(levels):
    # if already safe, return true
    if is_safe(levels):
        return True

    # try removing each level and check if the remaining report is safe
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i + 1:]  # remove the i-th level
        if is_safe(modified_report):
            return True

    return False


def parse_into_lists(input_data):
    # split into lines of numbers
    reports = parse_lines(input_data, delimiter=None)

    # convert each line to a list of ints and return
    return [list(map(int, line.split())) for line in reports]


class Day02Solution(SolutionBase):
    def __init__(self):
        super().__init__(day=2)

    def part_one(self) -> int:
        reports = parse_into_lists(self.input_data)

        return sum(1 for report in reports if is_safe(report))

    def part_two(self) -> int:
        reports = parse_into_lists(self.input_data)

        return sum(1 for report in reports if is_safe_with_dampener(report))


if __name__ == "__main__":
    solution = Day02Solution()
    solution.solve()
