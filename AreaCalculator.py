print("==================")
print("Area Calculator 📐")
print("==================\n")

shapes = ["1. Triangle", 
         "2. Rectangle", 
         "3. Square", 
         "4. Circle", 
         "5. Quit"]

pi = 3.1416

[print(i) for i in shapes]

shape = int(input("\nWhich shape?: "))

if shape >= 1 and shape <= len(shapes):
    print("\nYou have chosen " + shapes[shape-1])

    if shape == 1:
        base = int(input("\nSelect the base: "))
        height = int(input("Select the height: "))
        print("\nThe area is: " + str(base * height / 2))

    elif shape == 2:
        base = int(input("\nSelect the base: "))
        height = int(input("Select the height: "))
        print("\nThe area is: " + str(base * height))

    elif shape == 3:
        side = int(input("\nSelect the side length: "))
        print("\nThe area is: " + str(side * side))

    elif shape == 4:
        radius = int(input("\nSelect the radius: "))
        print("\nThe area is: " + str(pi*radius*radius))

    elif shape == 5:
        print("\nGood bye!")

else:
    print("\nInvalid Choice")