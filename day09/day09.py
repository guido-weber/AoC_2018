import re
from collections import Counter, deque

TEST = [
    '10 players; last marble is worth 1618 points: high score is 8317',
    '13 players; last marble is worth 7999 points: high score is 146373',
    '17 players; last marble is worth 1104 points: high score is 2764',
    '21 players; last marble is worth 6111 points: high score is 54718',
    '30 players; last marble is worth 5807 points: high score is 37305'
]

PATTERN = r'(\d+) players; last marble is worth (\d+) points'


def play(players, last_marble):
    circle = deque([0])
    player = 1
    scores = Counter()
    for next_marble in range(1, last_marble + 1):
        # The "current" position is always the last entry in the deque, rotate
        # the circle accordingly.
        if (next_marble % 23) == 0:
            circle.rotate(7)
            scores[player] += next_marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(next_marble)
        player = 1 if player == players else player + 1
    return scores.most_common(1)[0]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        # lines = TEST
    for line in lines:
        players, last_marble = [int(x) for x in re.match(PATTERN, line).group(1, 2)]
        (player, score) = play(players, last_marble)
        print("Part 1: player %d, highscore %d" % (player, score))
        (player, score) = play(players, last_marble * 100)
        print("Part 2: player %d, highscore %d" % (player, score))
