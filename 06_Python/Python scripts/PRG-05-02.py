while True:  #using while True: is just a way of running a loop that will continue to run until you explicitly break out of it using break or return 
    x = float(input("Please input a number: "))
    if x > 100:
        print("Too high...")
    elif x < 100:
        print("Too low")
    elif x == 100:
        print("Spot on")
        break