min_speed = int(input('enter minimum kph speed: '))
max_speed = int(input('enter minimum kph speed: '))

print('kph\tmph')
print('___\t___')

for kph_speed in range(min_speed, max_speed+10, 10):
    mph_speed = kph_speed * 0.614
    print(f'{kph_speed}\t{mph_speed:.0f}')