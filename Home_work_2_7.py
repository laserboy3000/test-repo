# конвертер секунд в часы и наоборот
hou = 2 # number of hours
sec = 3600 # number of seconds in 1 hour
print("Hours:", hou) # printing the number of hours
print("Seconds in Hours:", hou*sec) # printing the number of seconds in a given number of hours
hou = 3
print("Seconds in Hours:", hou*sec)
print("Input number of hours to convert:")
hou = int(input())
print("Seconds in Hours: " + str(hou*sec))
