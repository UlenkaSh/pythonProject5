def rule():
    print("------------------------")
    print ("     Добро пожаловать ")
    print("          в игру ")
    print("     'Крестики - нолики'")
    print("-------------------------")
    print("Правила игры:")
    print("Введите:")
    print("x - номер строки")
    print("у - номер столбца")

rule()
field = [["  "] * 3 for i in range (3)]
def show_field():
        print(f"   | 0 | 1 | 2 |")
        print ('-----------------')
        for i in range(3):
            print (f" {i} | {field[i][0]} | {field[i][1]} | {field[i][2]}|")
            print ('-----------------')


def hod_igroka():
    while True:
        cords = input("Введите координаты:").split()
        if len(cords) != 2:
            print ('Введите 2 координаты')
            continue

        x,y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print ("Вы ввели не число")
            continue

        x = int(x)
        y = int(y)

        if 0 <= x <= 2 and 0 <= y <= 2 :
            if field[x][y] == "  ":
                print (x,y)
            else:
                print('клетка занята')
        else:
            print ("Координата вне диапазона")
            continue
        return (x,y)

def win ():
    for i in range(3):
        spisok = []
        for j in range(3):
            spisok.append (field[i][j])
            if spisok == ["X", "X", "X"]:
                print ("Вы выиграли!")
                return True

    for i in range(3):
        spisok = []
        for j in range(3):
            spisok.append (field[j][i])
            if spisok == ["X", "X", "X"]:
                print ("Вы выиграли!")
                return True

    spisok = []
    for i in range(3):
        spisok.append (field[i][i])
    if spisok == ["X", "X", "X"]:
        print ("Вы выиграли!")
        return True

    spisok = []
    for i in range(3):
        spisok.append (field[i][2-i])
    if spisok == ["X", "X", "X"]:
        print ("Вы выиграли!")
        return True

    for i in range(3):
        spisok = []
        for j in range(3):
            spisok.append (field[i][j])
            if spisok == ["0", "0", "0"]:
                print ("Вы выиграли!")
                return True

    for i in range(3):
        spisok = []
        for j in range(3):
            spisok.append (field[j][i])
            if spisok == ["0", "0", "0"]:
                print ("Вы выиграли!")
                return True

    spisok = []
    for j in range(3):
        spisok.append (field[i][i])
    if spisok == ["0", "0", "0"]:
        print ("Вы выиграли!")
        return True

    spisok = []
    for j in range(3):
        spisok.append (field[i][2-i])
    if spisok == ["0", "0", "0"]:
        print ("Вы выиграли!")
        return True




count = 0
while True:
    count +=1
    show_field()
    if count % 2 == 1:
        print ("ходит крестик")
    else:
        print ("Ходит нолик")

    x,y = hod_igroka()

    if count % 2 == 1:
        field[x][y] ="X"
    else:
        field[x][y] ="0"
    if win():
        break
    if count == 9:
        print ("Ничья")
        break

