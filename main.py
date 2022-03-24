size = 3
tictactoe = []
for i in range(size):
    tictactoe.append([0]*size)
    
class Format:
    end = "\033[0m"
    underline = "\033[4m"
    strike = "\u0336"

def visualization(matrix):
    matrix_size = len(matrix)
    for i in range(matrix_size):
        print("", (Format.underline + "   " + Format.end), end = "")
    print("")
    for i in range(matrix_size):
        print("", end = '|')
        for j in range(matrix_size):
            element = matrix[i][j]
            if element != 0:
                print(Format.underline, element, Format.end, end = '|')
            else:
                print(Format.underline + "   " + Format.end, end = '|')
        print("")        

def move(matrix, x, y, turn):
    if matrix[x][y] == 0 and (turn % 2) == 0 :
        print("Ходит х")
        matrix[x][y] = "x"
    elif matrix[x][y] == 0 and (turn % 2) == 1 :
        print("ходит о")
        matrix[x][y] = "o"
    else:
        False

def checker(matrix):
    matrix_size = len(matrix)
    for i in range(matrix_size):
        row = set(matrix[i])
        if len(row) == 1 and list(row)[0] != 0:
            print("Congratulations!", list(row)[0], "player won!")
            return False
        for i in range(matrix_size):
            column = []
            for j in range(matrix_size):
                column.append(matrix[j][i])
            if len(set(column)) == 1 and list(column)[0] != 0:
                print("Congratulations!", list(column)[0], "player won!")
                return False 
        diagonal = []
        for i in range(matrix_size):
            diagonal.append(matrix[i][i])
        if len(set(diagonal)) == 1 and list(set(diagonal))[0] != 0:
            print("Congratulations!", list(set(diagonal))[0], "player won!")
            return False
        else:
            k = 0
            for i in range(matrix_size):
                if 0 in matrix[i]:
                    k = 1
            if k == 0:                    
                print("It's a tie!")
                return False
    return True
i = 0
while i <= (size*size):
    print('Write row number')
    x = int(input()) - 1
    print('Write column number')
    y = int(input()) - 1
    if (x <= size-1) and (y <= size-1):
        if tictactoe[x][y] == 0:
            move(tictactoe, x, y, i)
            visualization(tictactoe)
            i+=1
        else:
            print("This field is already taken")
            visualization(tictactoe)
    else:
        print("Coordinates out of range")
        visualization(tictactoe)
    game_ended = checker(tictactoe)
    if game_ended == False:
        break;