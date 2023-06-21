import itertools
import typing as t
from dataclasses import dataclass, field


def solve(max_trades: int, prices: list[int]) -> int:
    grid: dict[Vec, Trade] = dict()

    def get_trade(r: int, c: int) -> t.Optional[Trade]:
        return grid.get((r, c), None)

    for (row, col) in itertools.product(range(len(prices)), range(len(prices))):
        current_buy_price = prices[row]
        current_sell_price = prices[col]

        left = get_trade(row, col - 1)
        min_buy_price = prices[row]
        buy_index = row

        if left is not None:
            if left.min_buy_price < min_buy_price:
                min_buy_price = left.min_buy_price
                buy_index = left.buy_index

        up = get_trade(row - 1, col)
        max_sell_price = prices[row]
        sell_index = row

        if up is not None:
            if up.max_sell_price < max_sell_price:
                max_sell_price = up.max_sell_price
                sell_index = up.sell_index

        ##
        # What if I BOUGHT here instead of earlier?

        earlier_buy = get_trade(row, col - 1)
        

        # In order to buy, I can't have already bought



        ##
        # What if I SOLD here instead of earlier?


        grid[(row, col)] = Trade(
            min_buy_price=min_buy_price,
            max_sell_price=max_sell_price,
            buy_index,
            sell_index,
            count=0,
            profit=0,
        )

    return (
        0
        if (final_trade := get_trade(len(prices) - 1, len(prices) - 1)) is None
        else final_trade.profit
    )


Vec = tuple[int, int]


@dataclass
class Trade:
    min_buy_price: int
    max_sell_price: int
    buy_index: int
    sell_index: int
    count = 0
    profit = 0


# if buy_index is None:
#     buy_index = i

# elif sell_index is None:
#     sell_index = i

# else:
#     buy_at = prices[buy_index]
#     sell_at = prices[sell_index]
#     trades.append(
#         sell_at - buy_at
#     )

#     buy_index = None
#     sell_index = None
