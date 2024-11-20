def my_func(some_int: int, some_list: list) -> None:
    some_int += 1
    print(f'id of some_int', id(some_int))
    print(f'id of some_list', id(some_list))

a = 1
b = a
my_list = ['a', 'b', 'hello']

print('id of a', id(a))
print('id of my_list', id(my_list))
my_func(a, my_list)


