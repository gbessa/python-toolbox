# READ
import datetime

file = open("linus.txt", "r")
linus = file.read()
file.close()
print(linus)

# WRITE
file = open("output.txt", "w")
linus = file.write("Now: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
file.close()