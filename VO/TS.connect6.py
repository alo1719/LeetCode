class Connect6:
    def __init__(self):
        self.cnt = -1
        self.white = set()
        self.black = set()
    
    def getTurn(self):
        if 1 <= self.cnt%4 <= 2:
            return 'W'
        return 'B'
    
    def placeWhite(self, x, y):
        self.cnt += 1
        if self.getTurn() != 'W':
            self.cnt -= 1
            raise Exception('Wrong turn')
        if (x, y) in self.white or (x, y) in self.black:
            self.cnt -= 1
            raise Exception('Occupied')
        self.white.add((x, y))
        return self.tryHor(self.white, x, y) or self.tryVer(self.white, x, y) or self.tryDiag(self.white, x, y) or self.tryAntiDiag(self.white, x, y)

    
    def placeBlack(self, x, y):
        self.cnt += 1
        if self.getTurn() != 'B':
            self.cnt -= 1
            raise Exception('Wrong turn')
        if (x, y) in self.white or (x, y) in self.black:
            self.cnt -= 1
            raise Exception('Occupied')
        self.black.add((x, y))
        return self.tryHor(self.black, x, y) or self.tryVer(self.black, x, y) or self.tryDiag(self.black, x, y) or self.tryAntiDiag(self.black, x, y)

    def tryHor(self, s, x, y):
        left = right = 0
        while (x-left-1, y) in s:
            left += 1
            if left >= 5: return True
        while (x+right+1, y) in s:
            right += 1
            if left+right+1 >= 6: return True
        return False
    
    def tryVer(self, s, x, y):
        up = down = 0
        while (x, y-up-1) in s:
            up += 1
            if up >= 5: return True
        while (x, y+down+1) in s:
            down += 1
            if up+down+1 >= 6: return True
        return False
    
    def tryDiag(self, s, x, y):
        up = down = 0
        while (x-up-1, y-up-1) in s:
            up += 1
            if up >= 5: return True
        while (x+down+1, y+down+1) in s:
            down += 1
            if up+down+1 >= 6: return True
        return False
    
    def tryAntiDiag(self, s, x, y):
        up = down = 0
        while (x-up-1, y+up+1) in s:
            up += 1
            if up >= 5: return True
        while (x+down+1, y-down-1) in s:
            down += 1
            if up+down+1 >= 6: return True
        return False
    
board = Connect6()
print(board.getTurn()) # B
print(board.placeBlack(50, 50))
print(board.getTurn()) # W
print(board.placeWhite(51, 50))
print(board.placeWhite(51, 51))
print(board.getTurn()) # B
print(board.placeBlack(50, 51))
print(board.placeBlack(50, 49))
print(board.placeWhite(52, 50))
print(board.placeWhite(53, 51))
print(board.placeBlack(50, 52))
print(board.placeBlack(50, 53))
print(board.placeWhite(53, 50))
print(board.placeWhite(54, 51))
print(board.placeBlack(50, 48)) # True
