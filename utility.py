gfib = 0
file_local_path = "/home/stage/PycharmProjects/dir_thread/Prova.txt"


def my_fib(n):  # definisce fibonacci
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return my_fib(n-1) + my_fib(n-2)