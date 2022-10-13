a = 'int'    #these values were given in the excercise
b = 7
c = False
d = "18.5"

print("a is", type(a))  # here we print the data types for each variable.
print("b is", type(b))
print("c is", type(c))
print("d is", type(d))

x = b + float(d) #the error is raised because 'd' is a string, float() geeft de parameter waarde terug als float.
print(x)         