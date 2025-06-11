from datetime import *

x = "12:51AM"

time = datetime.strptime(x, "%I:%M%p")
time1 = datetime.strftime(time, '%H:%M%p')
print(time)
print(time1)