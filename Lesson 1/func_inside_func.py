# Мы можмем расширить работу функции, передав ее в другую
def func(x, F): # Декорирование функции
    print(F(x))

def inside_func(x):
    return x + 3

x = 2
func(x, inside_func)