
def tri_area_calc(a: float, b: float, c: float) -> float:
    "computes area of a triangle with sides a, b, and c"

    s = (a + b + c) / 2
    A = (s * (s-a) * (s-b) * (s-c))**0.5
    return A

a = float(input('enter side 1: '))
b = float(input('enter side 2: '))
c = float(input('enter side 3: '))
print(f'area is {tri_area_calc(a, b, c)}')
