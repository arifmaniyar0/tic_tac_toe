from random import randint

border = [" " for x in range(1,10)]

def print_border():
    print(border[0] + " | " + border[1] + " | " + border[2])
    print("--+---+--")
    print(border[3] + " | " + border[4] + " | " + border[5])
    print("--+---+--")
    print(border[6] + " | " + border[7] + " | " + border[8])

def AddValueX(val,pos):
    while not CheckPosition(pos):
        print("position already allocated")
        pos = input("Enter different position:")
        pos = ValidatePosition(pos)

    border[pos] = val

def CheckPosition(pos):
    return border[pos] == " "

def compMove():
    possibleMoves = [x for x in range(len(border)) if border[x] == " " and border[x] != "X"]
    move = 0
    # take winnig move or block opponent winning move
    for val in ["O","X"]:
        for i in possibleMoves:
            boardCopy = border[:]
            boardCopy[i] = val
            if isWinner(boardCopy,val):
                move = i
                return move
    # take corner
    corner = [y for y in [0,2,6,8] if border[y] == " "]
    for a in range(0,(len(corner))):
        if CheckPosition(a):
            move = selectRandom(corner)
            return move
    # take center
    if CheckPosition(4):
        move = 4
        return 4
    # take edge
    edge = [y for y in [1,3,5,7] if border[y] == " "]
    for b in range(0,len(edge)):
        if CheckPosition(b):
            move = selectRandom(edge)
            return move

def isWinner(b,l):
    return ((b[0] == l and b[1] == l and b[2] == l)
            or (b[3] == l and b[4] == l and b[5] == l)
            or (b[6] == l and b[7] == l and b[8] == l)
            or (b[0] == l and b[3] == l and b[6] == l)
            or (b[1] == l and b[4] == l and b[7] == l)
            or (b[2] == l and b[5] == l and b[8] == l)
            or (b[0] == l and b[4] == l and b[8] == l)
            or (b[2] == l and b[4] == l and b[6] == l))

def selectRandom(list):
    import random
    index = random.randrange(0,len(list))
    return list[index]

def AddValueO(val,pos):
    # while not CheckPosition(pos):
    #     pos = randint(0,8)
    border[pos] = val

def ValidatePosition(pos):
    while not pos.isdigit():
        pos = input("Invalid Number! Enter valid number:")
    pos = int(pos) - 1
    while pos < 0 or pos > 9:
        pos = input("enter valid position within 1 to 9:")
        pos = int(pos)-1
    return pos

def isFull():
    count = 0
    for h in border:
        if h == " ":
            count += 1
    return count == 0


def main():
    print("tik tac toe")
    print_border()
    while True:
        pos = input("Enter value (1-9):")
        pos = ValidatePosition(pos)
        if not isFull():
            AddValueX("X", pos)
        else:
            print("GameTie")
            print_border()
            break
        if not isFull():
            AddValueO("O", compMove())
        else:
            print("Game Tie")
            print_border()
            break
        if isWinner(border, "X"):
            print_border()
            print("You win")
            break
        elif isWinner(border, "O"):
            print_border()
            print("you lose")
            break
        else:
            print_border()

# start
main()

