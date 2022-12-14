results = [115, 352, 0, 310, 500]


def get_winners(res):
    winners = []
    while len(winners) <= 2:
        winners.append(res.index(max(res)) + 1)
        res.remove(max(res))
    return winners


print(get_winners(results))
