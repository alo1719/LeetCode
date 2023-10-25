from random import *


class Board:
    def __init__(self, m, n, ais):
        self.m = m
        self.n = n
        self.k = len(ais)
        self.cheese = (randint(0, m-1), randint(0, n-1))
        self.pos = {}
        self.ais = ais
        for i in range(self.k):
            ais[i].secret = randint(0, 10000000)  # UUID
            self.pos[ais[i].secret] = (randint(0, m-1), randint(0, n-1))
            ais[i].get_distance = lambda x: abs(self.pos[x][0]-self.cheese[0])+abs(self.pos[x][1]-self.cheese[1])
            ais[i].get_pos = lambda x: self.pos[x]

    def start(self):
        while True:
            for ai in self.ais:
                secret = ai.secret
                self.handle_move(secret, ai.move())
                print(secret, self.pos[secret], ai.get_distance(secret))
                if ai.get_pos(secret) == self.cheese:
                    print(secret, ' got the cheese!')
                    return
                
    def handle_move(self, secret, direction):
        if direction < 0 or direction > 3:
            raise Exception("Invalid direction")
        if direction == 0:  # up
            x, y = self.pos[secret][0]-1, self.pos[secret][1]
        elif direction == 1:  # down
            x, y = self.pos[secret][0]+1, self.pos[secret][1]
        elif direction == 2:  # left
            x, y = self.pos[secret][0], self.pos[secret][1]-1
        elif direction == 3:  # right
            x, y = self.pos[secret][0], self.pos[secret][1]+1
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            raise Exception("Invalid move")
        self.pos[secret] = (x, y)

class AI:
    def __init__(self):
        self.get_distance = None
        self.get_pos = None
        self.secret = None
    
    def move(self):
        return randint(0, 3)

board = Board(5, 5, [AI(), AI()])
board.start()