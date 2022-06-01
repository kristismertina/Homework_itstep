from typing import Union, Any


def passing () -> str:
    return ('None')

def work (a: int) -> Union [int, float]:
    s = a * 2
    return (s)

def parity (d: int)-> int:
    if d %2 == 0:
        print("yes")
    else:
        print("no")
    return (d)


def comparison (a: float, b:float) -> Union [int, float]:
    if a > b:
        print("yes")
    else:
        print("no")
        return (a, b)




a = [1, 2, 3]

def new (w: int) -> Union [int, float]:
    return w * 10

a = list(map(new, a))

print(a)


d = [1, 5, 6, 3, 7, 9]

def sort (y: int) -> Union [int, float]:
    return y > 5

d = list(filter(sort, d))


def der (a:float, s:float):
    return a + s



a = []

def ghj (g: str)-> Union [int, str]:
    return a.append(g)


m_m = [1, 2, 5]

max_num = max(m_m)
min_num = min(m_m)
print(max_num)
print(min_num)



def leap_year (a: float):
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



def season (a:int):
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



def new_f (x:int, y:int, a:str) -> Any:
    return x*y +a

def new_f2 (x:str) -> int:
    return x*2



def decorate (a):
    def summ (x=2, y=2):
        print("сумма", x+y)
        a()
        print("степень", st)
    return summ


@decorate
def st ():
    return x+y **2


def numbers_range(n):
    for i in range(n):
        yield i
k = numbers_range(4)
print(next(k))
print(next(k))
print(next(k))
print(next(k))