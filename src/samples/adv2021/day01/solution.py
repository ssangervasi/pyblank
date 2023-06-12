import itertools
import typing as t


def parse_input(input_lines: list[str]) -> list[int]:
    return [int(line.strip()) for line in input_lines if len(line) > 0]


def solve_part_one(input_nums: t.Union[list[int], list[float]]) -> int:
    nums_iter = iter(input_nums)
    prev = next(nums_iter, None)

    if prev is None:
        return 0

    increases = 0

    for n in nums_iter:
        if prev < n:
            increases += 1

        prev = n

    return increases


def solve_part_two(input_nums: list[int]) -> int:
    target_window_size = 3
    window_averages = [
        sum(window) / target_window_size
        for (left_edge) in range(len(input_nums))
        if (
            (window := input_nums[left_edge : (left_edge + target_window_size)])
            and len(window) == target_window_size
        )
    ]

    return solve_part_one(window_averages)
