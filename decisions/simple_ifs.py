def is_cold_outside(temperature: float) -> bool:
    is_cold = temperature < 0
    return is_cold

temperature = -50

if is_cold_outside(temperature):
    print('wear a coat')
else:
    print('it is nice out')