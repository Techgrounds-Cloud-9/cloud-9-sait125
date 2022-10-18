# Lists
You can declare a list of values in a single variable. A list is represented by square brackets  [ ], and each value is separated by a comma.
# Excercise 1
- Create a new script.
- Create a variable that contains a list of five names.
- Loop over the list using a for loop. Print every individual name in the list on a new line.

## Code
```python
mylist = ["Ehab", "Elena", "Manisha", "Sait", "Tanuja"] # make sure to seperate every value.

for i in mylist:
    print(i)
```
## Result
![7.1](../../00_includes/PYT/PYT-07-01-01.png)

This is almost the same as exercise *PRG-04-loops 4.1*, except we have to create our own list this time. 
# Excercise 2
- Create a new script.
- Create a list of five integers.
- Use a for loop to do the following for every item in the list:
Print the value of that item added to the value of the next item in the list. If it is the last item, add it to the value of the first item instead (since there is no next item).
## Code
```python
list =[13, 6, 18, 25, 15]

for i in range(len(list)):
    if i < len(list)-1:
        print (list[i] + list[i+1])
    else:
        print (list[i] + list[0])
```
## Result
![7.2](../../00_includes/PYT/PYT-07-01-02.png)
