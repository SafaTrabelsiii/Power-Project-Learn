my_list = []

for i in [10,20,30,40]:
    my_list.append(i)

my_list.insert(1,15)

my_list.extend([50,60,70])

del my_list[-1]

my_list.sort()

print(my_list.index(30))
