x, y, z = input("liczenie: ").split()

x = int(x)
z = int(z)
if y == "+":
    print(float(x + z))
elif y == "-":

    print(float(x - z))
elif y == "*":
    print(float(x * z))

elif y == "/" and z == 0:
    print("you cannot divide by 0!!!")

elif y == "/" and z != 0:
    print(x / z)

else:
    print("try again...")
