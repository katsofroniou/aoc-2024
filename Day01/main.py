from utils import SolutionBase, parse_lines


class Day01Solution(SolutionBase):
    def __init__(self):
        super().__init__(day=1)

    def part_one(self) -> int:
        # parse the input into lines
        # auto split on any whitespace
        parsed_lines = parse_lines(self.input_data, delimiter=None)

        # ensure each line has exactly two parts
        sanitized_pairs = []
        for line in parsed_lines:
            # split on any whitespace
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"Malformed input line: {line}")
            sanitized_pairs.append((int(parts[0]), int(parts[1])))

        # separate into left and right lists and sort
        left_list, right_list = zip(*sanitized_pairs)
        left_list = sorted(left_list)
        right_list = sorted(right_list)

        # calculate the total distance
        total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
        return total_distance

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    solution = Day01Solution()
    solution.solve()
