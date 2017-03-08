board = [raw_input() for i in range(1,5)]
print ['NO','YES'][any((board[x][y:y+2]+board[x+1][y:y+2]).count('#') != 2 for x in range(3) for y in range(3))]