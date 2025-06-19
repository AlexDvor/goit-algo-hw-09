from collections import defaultdict


# Жадібний алгоритм
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = defaultdict(int)
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result[coin] += 1
    return dict(result)


# Динамічне програмування
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):

    min_coins = [0] + [float("inf")] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = defaultdict(int)
    current = amount
    while current > 0:
        coin = coin_used[current]
        result[coin] += 1
        current -= coin

    return dict(result)


if __name__ == "__main__":
    amount = 113

    greedy_result = find_coins_greedy(amount)
    dp_result = find_min_coins(amount)

    print(f"Greedy для {amount}: {greedy_result}")
    print(f"Dynamic для {amount}: {dp_result}")
