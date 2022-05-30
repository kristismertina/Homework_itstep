def passing ():
    return ('None')

def work (a):
    s = a * 2
    return (s)

def parity (d):
    if d %2 == 0:
        print("yes")
    else:
        print("no")
    return (d)


def comparison (a, b):
    if a > b:
        print("yes")
    else:
        print("no")
        return (a, b)


a = lambda b, c : b % c
print(a)



a = [1, 2, 3]

def new (w):
    return w * 10

a = list(map(new, a))

print(a)


d = [1, 5, 6, 3, 7, 9]

def sort (y):
    return y > 5

d = list(filter(sort, d))


def der (a, s):
    return a + s



a = []

def ghj (g):
    return a.append(g)


m_m = [1, 2, 5]

max_num = max(m_m)
min_num = min(m_m)
print(max_num)
print(min_num)



def leap_year (a):
    if a %4 == 0:
        print("true")
    else:
        print("false")


ls = [16, -17, 2, 78.7, False , False , {'True':True }, 555, 12, 23, 42, "DD"]

def ls_1 ():
    new_ls = []
    for i in ls:
        if ls[i] == int or float:
            new_ls.append(ls[i])
            new_ls.sort()
            print(new_ls)



def season (a):
    if  a == 3 or 4 or 5:
        print('string')
    elif a == 6 or 7 or 8:
        print('summer')
    elif  a == 9 or 10 or 11:
        print('autumn')
    elif a == 1 or 2 or 12:
        print('winter')
    else:
        print('введите месяц от 1 до 12')












