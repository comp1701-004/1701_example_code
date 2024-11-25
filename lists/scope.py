def modify_a_list(a_list: list) -> None:
    a_list.append(4)
    print(a_list)

def modify_an_int(a_int: int) -> None:
    a_int += 1
    print(a_int)

l = [1, 2, 3]
modify_a_list(l) # prints [1, 2, 3, 4]
print(l) # prints [1, 2, 3, 4]   why?

i = 5
modify_an_int(i)
print(i)


