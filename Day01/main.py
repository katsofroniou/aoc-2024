from collections import Counter

from utils import SolutionBase, parse_lines, parse_input_pairs


class Day01Solution(SolutionBase):
    def __init__(self):
        super().__init__(day=1)

    def part_one(self) -> int:
        # get left/right list
        left_list, right_list = parse_input_pairs(self.input_data)

        left_list = sorted(left_list)
        right_list = sorted(right_list)

        # calculate the total distance
        total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
        return total_distance

    def part_two(self) -> int:
        # get left/right list
        left_list, right_list = parse_input_pairs(self.input_data)

        # count occurrences in the right list
        right_count = Counter(right_list)

        # calculate the similarity score
        similarity_score = sum(num * right_count[num] for num in left_list)
        return similarity_score


if __name__ == "__main__":
    solution = Day01Solution()
    solution.solve()
