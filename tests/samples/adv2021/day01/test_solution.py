from samples.adv2021.day01.solution import solve_part_one, solve_part_two, parse_input
from samples.adv2021.utils import read_input_lines


EXAMPLE_STR = """
199
200
208
210
200
207
240
269
260
263
"""
EXAMPLE_INPUT = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
EXAMPLE_ANSWER_ONE = 7
EXAMPLE_ANSWER_TWO = 5


def test_parse_input():
    assert parse_input(EXAMPLE_STR.splitlines()) == EXAMPLE_INPUT


def test_solve_part_one_example():
    assert solve_part_one(EXAMPLE_INPUT) == 7


def test_solve_part_one_solution():
    input_lines = read_input_lines(__file__)
    input_parsed = parse_input(input_lines)

    print(f"Parsed {type(input_parsed)} from {len(input_lines)} lines")

    result = solve_part_one(input_parsed)
    print(f"Result Part One: {result}")
    assert result == 1532


def test_solve_part_two_solution():
    input_lines = read_input_lines(__file__)
    input_parsed = parse_input(input_lines)

    print(f"Parsed {type(input_parsed)} from {len(input_lines)} lines")

    result = solve_part_two(input_parsed)
    print(f"Result Part Two: {result}")
    assert result == 1571
