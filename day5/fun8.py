def all_params(a, b, /, c, **kwargs):
    print(a, b, c)
    print(kwargs)


all_params(1, 2, 3)
# 1 2 3
# {}
all_params(1, 2, c=9)
# 1 2 9
# {}


# po dodaniu /, argumenty a i b musza być przekazane po pozycji I NIE MOGĄ BYĆ PO NAZWIE !!!
# gdyby nie było slasha to nastepna linijka by zadziałała bez problemu

# all_params(a=1,b=2,c=9)
# TypeError: all_params() missing 2 required positional arguments: 'a' and 'b'

all_params(1, 2, c=9, a=10)


# 1 2 9
# {'a': 10}

def allparams_all(a, b, /, c=43, *args, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{args=}")
    print(f"{kwargs=}")


allparams_all(1, 2)
# a=1, b=2
# c=43, d=256
allparams_all(1, 2, 3)
# a=1, b=2
# c=3, d=256
allparams_all(1, 2, c=90)
# a=1, b=2
# c=90, d=256
allparams_all(1, 2, c=90)
allparams_all(1, 2, 90, 5)
allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 100, 200)
allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 100, 200, d=89)
# a=1, b=2
# c=90, d=256
# args=()
# a=1, b=2
# c=90, d=256
# args=(5,)
# a=1, b=2
# c=90, d=256
# args=(5, 6, 7, 8, 9, 100, 200)
# a=1, b=2
# c=90, d=89
# args=(5, 6, 7, 8, 9, 100, 200)


# allparams_all(1, 2, 90, d=89,5, 6, 7, 8, 9, 100, 200)
# SyntaxError: positional argument follows keyword argument

allparams_all(1, 2, 90, 5, 6, 7, 8, 9, 100, 200, d=89,e=1009,name="radek",a=0)
# a=1, b=2
# c=90, d=89
# args=(5, 6, 7, 8, 9, 100, 200)
# kwargs={'e': 1009, 'name': 'radek', 'a': 0}
