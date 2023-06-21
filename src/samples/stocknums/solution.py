import itertools
import typing as t
from dataclasses import dataclass, field


def solve(max_trades: int, prices: list[int]) -> int:
    grid: dict[Vec, Trade] = dict()

    def get_trade(r: int, c: int) -> Trade:
        return grid.get((r, c), TRADE_ZERO)

    def get_neighbor_trades(r: int, c: int) -> list[Trade]:
        return [
            get_trade(r + dr, c + dc)
            for (dr, dc) in [
                (-1, 0),
                (0, -1),
                # What does the upper left trade represent? Should it be checked?
                (-1, -1),
            ]
        ]

    def grid_str(trade_trace: list[Trade] = []):
        index_set = set((tx.buy_index, tx.sell_index) for tx in trade_trace)

        return "\n".join(
            [
                "   "
                + " ".join([f"{f'{c} ({prices[c]})':^10}" for c in range(len(prices))])
            ]
            + [
                f"{r:2} "
                + " ".join(
                    [
                        f"{t.profit:4} ({t.count:2}){'!' if (r, c) in index_set else ' '}"
                        for c in range(len(prices))
                        if (t := get_trade(r, c))
                    ]
                )
                for r in range(len(prices))
            ]
        )

    def trace_trades(end_trade: Trade) -> list[Trade]:
        trades = [end_trade]

        while True:
            head = trades[0]
            prior = get_trade(head.prior_buy_index, head.prior_sell_index)
            if (prior.buy_index == -1) or (prior.sell_index == -1):
                break

            trades.insert(0, prior)

        return trades

    def trace_str(trade_trace: list[Trade]):
        return "\n".join(str(t) for t in trade_trace)

    for (buy_index, sell_index) in itertools.product(
        range(len(prices)), range(len(prices))
    ):
        # A sale can only happen after a buy
        if sell_index < buy_index:
            continue

        # Stats for taking the current trade
        buy_price = prices[buy_index]
        sell_price = prices[sell_index]

        possible_trades = []

        # MAKE this trade
        # Then the best history we can have is before this trade's indexes

        max_past_index = min(buy_index, sell_index) - 1
        max_past_trade = get_trade(max_past_index, max_past_index)
        new_trade = make_trade(
            from_trade=max_past_trade,
            buy_price=buy_price,
            sell_price=sell_price,
            buy_index=buy_index,
            sell_index=sell_index,
        )

        possible_trades += [new_trade]

        # SKIP this trade
        # Then all of the adjacent past trades are possible

        possible_trades += get_neighbor_trades(buy_index, sell_index)

        # Pick the trade with maximum profit

        best_trade = TRADE_ZERO

        for possible_trade in possible_trades:
            # Can't make any more trades
            if max_trades < possible_trade.count:
                continue

            # Otherwise compare by profits
            if best_trade.profit < possible_trade.profit:
                # print(f'{best_trade.profit} < {possible_trade.profit}')
                best_trade = possible_trade

            # For equal profit, prefer fewer trades
            if (
                best_trade.profit == possible_trade.profit
                and possible_trade.count < best_trade.count
            ):
                # print(f'{best_trade.profit} < {possible_trade.profit}')

                best_trade = possible_trade

        print(f"best: {best_trade.profit}")
        grid[(buy_index, sell_index)] = best_trade

    end_trades = [
        get_trade(buy_index, len(prices) - 1) for buy_index in range(len(prices))
    ]
    max_trade = max(end_trades, key=lambda t: t.profit)

    trade_trace = trace_trades(max_trade)
    print(
        f"""
Trade grid
---------
{grid_str(trade_trace)}
""",
        f"""
Max trace
---------
{trace_str(trade_trace)}
""",
    )

    return max_trade.profit


Vec = tuple[int, int]


@dataclass
class Trade:
    buy_price: int = -1
    sell_price: int = -1
    buy_index: int = -1
    sell_index: int = -1
    prior_buy_index: int = -1
    prior_sell_index: int = -1
    count: int = 0
    profit: int = 0

    def __str__(self) -> str:
        return f"({self.buy_index:2}, {self.sell_index:2}) {self.sell_price:4} - {self.buy_price:4} = {(self.sell_price - self.buy_price):4} => {self.profit:4} ({self.count:2})"


TRADE_ZERO = Trade()


def make_trade(
    from_trade: Trade,
    buy_price: int,
    sell_price: int,
    buy_index: int,
    sell_index: int,
) -> Trade:
    added_profit = sell_price - buy_price

    return Trade(
        buy_price=buy_price,
        sell_price=sell_price,
        buy_index=buy_index,
        sell_index=sell_index,
        #
        prior_buy_index=from_trade.buy_index,
        prior_sell_index=from_trade.sell_index,
        count=from_trade.count + 1,
        profit=from_trade.profit + added_profit,
    )
