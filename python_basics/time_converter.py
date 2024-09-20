# Converts the time 4000 seconds to a number 
# of hours, minutes, and seconds 
# Prints the time in H:M:S format

time = 4000 # time in seconds

hours = time // 3600  # gives number of whole hours
time = time % 3600    # gives seconds left after the whole hours

minutes = time // 60
seconds = time % 60

print(hours, ":", minutes, ":", seconds)