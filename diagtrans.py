board = [["00","01","02","03","04","05","06"],["10","11","12","13","14","15","16"],["20","21","22","23","24","25","26"],["30","31","32","33","34","35","36"],["40","41","42","43","44","45","46"],["50","51","52","53","54","55","56"]]

def fours(board):
    four = [[],[],[],[]]
    for a in range(0,4):
        four[0].append(board[3-a][a])
    for a in range(0,4):
        four[1].append(board[5-a][3+a])
    for a in range(0,4):
        four[2].append(board[2+a][0+a])
    for a in range(0,4):
        four[3].append(board[0+a][3+a])
    return four

def fives(board):
    five = [[],[],[],[]]
    for a in range(0,5):
        five[0].append(board[4-a][a])
    for a in range(0,5):
        five[1].append(board[5-a][2+a])
    for a in range(0,5):
        five[2].append(board[1+a][0+a])
    for a in range(0,5):
        five[3].append(board[a][2+a])
    return five

def sixes(board):
    six = [[],[],[],[]]
    for a in range(0,6):
        six[0].append(board[a][a])
    for a in range(0,6):
        six[1].append(board[a][1+a])
    for a in range(0,6):
        six[2].append(board[a][5-a])
    for a in range(0,6):
        six[3].append(board[5-a][1+a])
    return six

def DiagFlip(board):
    four = fours(board)
    five = fives(board)
    six = sixes(board)
    return four, five, six

def DiagCheck(board, player):
    GameOver = False
    token = player#s[player]
    four, five, six = DiagFlip(board)
    for row in four:
        if row[0] == token and row[1] == token and row[2] == token and row[3] == token:
            GameOver = True
            return GameOver
    for row in five:
        for i in range(2):
            if row[i] == token and row[i+1] == token and row[i+2] == token and row[i+3] == token:
                GameOver = True
                return GameOver
    for row in six:
        for i in range(3):
            if row[i] == token and row[i+1] == token and row[i+2] == token and row[i+3] == token:
                GameOver = True
                return GameOver
    return GameOver