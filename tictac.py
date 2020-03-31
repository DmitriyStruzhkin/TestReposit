# checking new coordinates
def check_crd():
    a, b = input("Enter the coordinates:").split()
    crd = str(a) + str(b)
    if a.isdigit() == False or b.isdigit() == False:
        return print("You should enter numbers!")
    elif int(a) > 3 or int(b) > 3:
        return print('Coordinates should be from 1 to 3!"')
    elif check_list[crd_list[crd]] == 'X' or check_list[crd_list[crd]] == 'O':
        return print("This cell is occupied! Choose another one!")
    else:
        check_list[crd_list[crd]] = turn_key
        visible_list[crd_list[crd]] = turn_key
        counting[0] = 1

# frame for game space
def inputing_matrix(empty_list):
    count = 0
    for i in empty_list[0: 5: 4]:
        for j in range(len(i)):
            i[j] = '-'
    for i in empty_list[1: 4]:
        for j in range(0, 9, 8):
            i[j] = '|'
    for i in empty_list[1:4]:
        for j in range(2, 8, 2):
            i[j] = visible_list[count]
            count += 1
    for i in empty_list:
        print(*i, sep='')


counting = [[0]]
visible_list = [" " for i in range(9)]
check_list = [i for i in range(9)]
rezult = 0
empty_list = [[' ' for i in range(9)] for j in range(5)]
crd_list = {'13': 0, '23': 1, '33': 2, '12': 3, '22': 4, '32': 5, '11': 6, '21': 7, '31': 8}

inputing_matrix(empty_list)

counting[0] = 0
win_count = 0
turn = 0

while win_count == 0 and visible_list.count(' ') != 0:
    # sequence for turn X or O
    if turn % 2 == 0:
        turn_key = 'X'
    else:
        turn_key = 'O'
    check_crd()
    # check list for game condition
    if rezult == 0:
        for i in range(0, 3, 2):
            if i == 2:
                if check_list[i] == check_list[i + 2] == check_list[i + 4]:
                    rezult = check_list[i]
                    win_count += 1
            elif i == 0:
                if check_list[i] == check_list[i + 4] == check_list[i + 8]:
                    rezult = check_list[i]
                    win_count += 1
        for i in range(0, 3):
            if check_list[i] == check_list[i + 3] == check_list[i + 6]:
                rezult = check_list[i]
                win_count += 1
        for i in range(0, 7, 3):
            if check_list[i] == check_list[i + 1] == check_list[i + 2]:
                rezult = check_list[i]
                win_count += 1
    if counting[0] == 1:
        inputing_matrix(empty_list)
        turn += 1
    counting[0] = 0

print("Draw" if rezult == 0 else f'{rezult} wins')
