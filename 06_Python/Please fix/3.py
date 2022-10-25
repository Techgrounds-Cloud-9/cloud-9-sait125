'''
The output should be:
30
'''
foo = 20 # was 20 changed foo so that it would substract one 10 times off 40.
for i in range(10):
	foo += 1 # we could also change -= to += so it adds 20 + 10 instead of 40 - 10.

print(foo)