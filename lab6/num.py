# 3	Распределение памяти разделами переменной величины
a = [' ' for i in range(64)]
n = 0
# A = 65 chr(65)


def add():
    print("ВВедите размер процесса ( целое число меньше 64)")
    t = int(input())
    if t > 64:
        return ''
    if addprocess(t):
        return '1'
    else:
        return ''


def addprocess(size):
    global n
    s = 0
    index = 0
    li = []
    # Составляем список пустых пространств
    for i in range(64):
        if a[i] == ' ':
            s += 1
            if s == 1:
                index = i
                print(i)
            if i == 63:
                li.append([s, index])
                s = 0
        else:
            li.append([s, index])
            s = 0
    # минимальное пустое место подходящщее под размер
    minIndex = -1
    mini = 64
    for i in range(len(li)):
        if (li[i][0] >= size) and (li[i][0] <= mini):
            minIndex = li[i][1]
            mini = li[i][0]
    #
    if minIndex < 0:
        return 0
    else:
        for i in range(minIndex, minIndex + size):
            a[i] = chr(n + 65)
        n += 1
        return 1


def delete():
    print("ВВедите имя процесса ( A, B, C ...)")
    t = input()
    t.upper()
    if deleteprocess(t):
        return '2'
    else:
        return ''


def deleteprocess(b):
    global n
    exist = 0
    for i in range(64):
        if a[i] == b:
            exist = 1
            a[i] = ' '
    if exist:
        return 1
    else:
        return 0


def zprint(ax):
    s = ''
    print('_' * 64)
    for i in range(64):
        s = s + str(ax[i])
    print(s)
    print('_' * 64)


def menu():
    print(
        '''
        1. Добавить 
        2. Удалить
        '''
    )
    t = ''
    while t == '':
        t = input()
        if t == '1':
            t = add()
            if t == '':
                print('Нет места. Пожалуйста удалите процесс')

        elif t == '2':
            t = delete()
            if t == '':
                print('Нет процессов для удаления')
        else:
            t = ''
            print('Неверный символ')


while True:
    zprint(a)
    menu()
    print("\n" * 10)
