while True:
    x = float(input("Please input a number: "))
    if x > 100:
        print("Too high...")
    elif x < 100:
        print("Too low")
    elif x == 100:
        print("Spot on")
        break