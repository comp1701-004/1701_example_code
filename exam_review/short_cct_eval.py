def a() -> bool:
    print('getting a')
    return True

def b() -> bool:
    print('getting b')
    return True

def c() -> bool:
    print('getting c')
    return True

# print(
#     'a or (b and c) = ', a() or (b() and c())
# )
print(
    'b and (c or a) = ', b() and (c() or a())
)



# the assignment 3 decision structure (using short-cct evaluation)
if has_fever():
    if has_nausea():
        diagnosis = 'flu'
    else:
        diagnosis = 'infection'
else:  #i.e. they don't have fever
    # here's the short circuit eval. 
    # has_high_cortisol only called if has_low_hrv is True
    if has_low_hrv() and has_high_cortisol(): 
        diagnosis = 'stress'
    else:
        diagnosis = 'healthy'