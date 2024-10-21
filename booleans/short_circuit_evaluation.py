def a() -> bool:
    print('getting a')
    return True

def b() -> bool:
    print('getting b')
    return False

def c() -> bool:
    print('getting c')
    return True

print(
'a or (b and c) = ', a() or (b() and c())
)
print(
'b and (c or a) = ', b() and (c() or a())
)
