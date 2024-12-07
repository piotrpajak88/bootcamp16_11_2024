def change_upper(fun):
    def wew():
        try:
            return fun().upper()
        except:
            return "Funkcja ktora dekorujemy nie zwraca stringa"

    return wew

#bold_decorator

def bold_decorator(func):
    def wrapper():
        result = func()
        return f"\033[1m" + result +"\033[0m"

    return wrapper

@change_upper
def moja_funkcja():
    return "aaaa"
@change_upper
def moja_funkcja2():
    return 123

print(moja_funkcja())
print(moja_funkcja2())

@change_upper
def greeting():
    return "Hello World!"

@bold_decorator
def greeting2():
    return "Hello World!"

print(greeting()) # HELLO WORLD!
print(greeting2()) # Hello World!

@bold_decorator
@change_upper
def greeting3():
    return "Hello World!"

@change_upper
@bold_decorator
def greeting4():
    return "Hello World!"

print(greeting3())
print(greeting4())

# Kolejnosc ma znaczenie
