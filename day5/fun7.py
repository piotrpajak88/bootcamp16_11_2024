def connect(**opcje):
    print(opcje)
    # print(type(opcje))
    param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    param.update(opcje)
    print(param)
    param['pwd'] = opcje
    print(param)


connect()
# {}
# <class 'dict'>

connect(a=9)
# {'a': 9}

connect(a=9, name='AAA')


# {}
# {'host': '127.0.0.1', 'port': '8080'}
# {'host': '127.0.0.1', 'port': '8080', 'pwd': {}}
# {'a': 9}
# {'host': '127.0.0.1', 'port': '8080', 'a': 9}
# {'host': '127.0.0.1', 'port': '8080', 'a': 9, 'pwd': {'a': 9}}
# {'a': 9, 'name': 'AAA'}
# {'host': '127.0.0.1', 'port': '8080', 'a': 9, 'name': 'AAA'}
# {'host': '127.0.0.1', 'port': '8080', 'a': 9, 'name': 'AAA', 'pwd': {'a': 9, 'name': 'AAA'}}


def connect_all(*args, **kwargs):
    print(args, kwargs)


connect_all()
connect_all(1, 2, 3, 4, 5, 6)
connect_all(1, 2, 3, 4, 5, 6, 'Zenek')
connect_all(a=0, b=9)
connect_all(1, 2, 3, 4, 5, 6, 'Zenek', a=0, b=9)

# () {}
# (1, 2, 3, 4, 5, 6) {}
# (1, 2, 3, 4, 5, 6, 'Zenek') {}
# () {'a': 0, 'b': 9}
# (1, 2, 3, 4, 5, 6, 'Zenek') {'a': 0, 'b': 9}

# connect_all(c=10,1, 2, 3, 4, 5, 6, 'Zenek', a=0, b=9)
# SyntaxError: positional argument follows keyword argument

