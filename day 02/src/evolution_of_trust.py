from collections import Counter
from random import sample, choice
from itertools import combinations


class Player(object):
    def __init__(self):
        self.score = 0

    def action(self, own, other):
        pass

    def update(self, own, other):
        pass


class Cheater(Player):
    def action(self, own, other):
        return False


class Cooperator(Player):
    def action(self, own, other):
        return True


class Copycat(Player):
    def __init__(self):
        super(Copycat, self).__init__()
        self.last_action = True

    def action(self, own, other):
        if self.last_action:
            return True
        else:
            return False

    def update(self, own, other):
        self.last_action = other


class Grudger(Player):
    def __init__(self):
        super(Grudger, self).__init__()
        self.is_cheater = False

    def action(self, own, other):
        if self.is_cheater:
            return False
        else:
            return True

    def update(self, own, other):
        if not other:
            self.is_cheater = True


class Detective(Player):
    def __init__(self):
        super(Detective, self).__init__()
        self.state = 0
        self.is_copycat = False
        self.last_action = True

    def action(self, own, other):
        if self.state < 4:
            self.state += 1
            if self.state == 2:
                return False
            else:
                return True
        else:
            if self.is_copycat and self.last_action:
                return True
            else:
                return False

    def update(self, own, other):
        if self.state < 4 and not other:
            self.is_copycat = True
        if self.state > 3 and self.is_copycat:
            self.last_action = other


class RandomGuy(Player):
    def action(self, own, other):
        return choice([True, False])


class NotSameGuy(Player):
    def __init__(self):
        super(NotSameGuy, self).__init__()
        self.same_action = False

    def action(self, own, other):
        if self.same_action:
            return False
        return True

    def update(self, own, other):
        if own == other:
            return True


class Game(object):
    def __init__(self, matches=10):
        self.action1, self.action2 = None, None
        self.score1, self.score2 = 0, 0
        self.player_pairs = set()
        self.matches = matches
        self.registry = Counter()
        self.players = [Cheater(), Cooperator(), Copycat(),
                        Detective(), Grudger(), RandomGuy(), NotSameGuy()]

    def play(self):
        for k in range(self.matches):
            player_pairs = self.players_set()
            while len(player_pairs) > 0:
                player1, player2 = player_pairs.pop()
                self.action1 = player1.action(self.action1, self.action2)
                self.action2 = player2.action(self.action2, self.action1)
                if self.action1 and self.action2:
                    score1 = 2
                    score2 = 2
                elif not self.action1 and not self.action2:
                    score1 = 0
                    score2 = 0
                elif self.action1 and not self.action2:
                    score1 = -1
                    score2 = 3
                elif not self.action1 and self.action2:
                    score1 = 3
                    score2 = -1
                player1.update(self.action1, self.action2)
                player2.update(self.action2, self.action1)
                self.registry[type(player1).__name__] += score1
                self.registry[type(player1).__name__] += score2

    def top3(self):
        top = self.registry.most_common(3)
        print("Top 3 players:")
        for i, score in enumerate(top):
            print(f"{i+1}. {score[0]}: {score[1]}")

    def players_set(self):
        while len(self.player_pairs) < len(self.players) * (len(self.players) - 1) // 2:
            pair = tuple(sample(self.players, 2))
            if pair[0] != pair[1] and pair not in self.player_pairs:
                self.player_pairs.add(pair)
        return self.player_pairs


if __name__ == '__main__':
    game = Game()
    game.play()
    top = game.top3()
