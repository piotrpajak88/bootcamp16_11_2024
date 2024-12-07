# funkcja zagniezdzona (funkcja w funkcji)
# wykorzystywane w dekoratorach

def fun1():

    def fun2():
        print("To jest fun2")

    return fun2()

func = fun1
print(func)
print(type(func))
func()