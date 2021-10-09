import random


def change_index(row11, row22, row33):
    Available_blocks = True

    rows = [row11, row22, row33]

    for i in range(3):
        row = random.choice(rows)
        indx = random.randint(0, 2)
        if row[indx] == 0:
            row[indx] = 1
        else:
            change_index(row11, row22, row33)
    else:
        print('test1')

    print(row11)
    print(row22)
    print(row33)
