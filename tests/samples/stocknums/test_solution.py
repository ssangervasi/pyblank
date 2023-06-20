from samples.adv2021.day01.solution import solve_part_one, solve_part_two, parse_input
from samples.adv2021.utils import read_input_lines


"""
The first element is an integer k. The second element is an array of stock prices
(which are numbers) where the i-th element represents the stock price on day i.

Determine the maximum possible profit you can earn using at most k transactions.
A transaction is defined as buying and then selling one share of the stock.
Note that you cannot engage in multiple transactions at once. In other words,
you must sell the stock before you can buy it again.
"""

EXAMPLE_INPUT = [
    7,
    [
        18,
        54,
        32,
        183,
        162,
        146,
        54,
        79,
        107,
        182,
        4,
        117,
        151,
        142,
        110,
        138,
        19,
        41,
        56,
        113,
        61,
        96,
        149,
        64,
        11,
        88,
        126,
        124,
    ],
]
MIN_EXPECTED = 36


def test_solve_part_one_example():
    solution = solve_part_one(EXAMPLE_INPUT)
    print(
        f"""
Stock nums
----------
{solution}
"""
    )
    assert solution > MIN_EXPECTED
