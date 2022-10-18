list =[13, 6, 18, 25, 15]


for i in range(len(list)):
    if i < len(list)-1:
        print (list[i] + list[i+1])
    else:
        print (list[i] + list[0])