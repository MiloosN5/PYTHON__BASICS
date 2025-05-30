from rich.console import Console

console = Console()

# indexed (accessed), replaced, sliced, extended

my_list = [1, 10, 8, 7, 129, 33]
console.print(my_list[0]) # 1
console.print(my_list[4]) # 129
# console.print(my_list[11]) # IndexError: list index out of range
console.print(my_list[-2]) # 129
console.print(my_list[-3:]) # [7, 129, 33]
console.print(my_list[1:3]) # [10, 8]
console.print(my_list[1:20]) # [10, 8, 7, 129, 33] 

my_listExtended = my_list + [10, 19, 5]
console.print(my_listExtended) # [1, 10, 8, 7, 129, 33, 10, 19, 5]

my_list[1] = 105
console.print(my_list) # [1, 105, 8, 7, 129, 33]
console.print(my_listExtended) # [1, 10, 8, 7, 129, 33, 10, 19, 5]

# append

my_list.append(27)
# my_list.append(32, 38)  # TypeError: list.append() takes exactly one argument
my_list.append([32, 38])
console.print(my_list) # [1, 105, 8, 7, 129, 33, 27, [32, 38]]

# assignment

my_list2a = [14, 30, 25]
my_list2b = my_list2a
my_list2a[1] = 300
my_list2b[2] = 250
console.print(my_list2a) # [14, 300, 250]
console.print(my_list2b) # [14, 300, 250]
console.print(id(my_list2a) == id(my_list2b)) # True

my_list2a.append(82)
my_list2b.append(83)
console.print(my_list2a) # [14, 300, 250, 82, 83]
console.print(my_list2b) # [14, 300, 250, 82, 83]
console.print(id(my_list2a) == id(my_list2b)) # True

# shallow copy

my_list3a = [1, 2, 3]
my_list3b = my_list3a[:]

my_list3a[1] = 20
my_list3a.append(200)
console.print(my_list3a) # [1, 20, 3, 200]
console.print(my_list3b) # [1, 2, 3]

my_list3b[2] = 30
my_list3b.append(300)
console.print(my_list3a) # [1, 20, 3, 200, 300]
console.print(my_list3b) # [1, 2, 30, 300]

# size (len() -> built-in)

my_list4 = [10, 8, 77, 54, 121]
console.print(len(my_list4)) # 5
my_list4[:] = []
console.print(len(my_list4)) # 0

# nesting

my_list5a = ['a', 'b', 'c']
my_list5b = [1, 2, 3]
my_list5c = [my_list5a, my_list5b]
console.print(my_list5c) # [['a', 'b', 'c'], [1, 2, 3]]

my_list5c[0][1] = 'bb'
console.print(my_list5c) # [['a', 'bb', 'c'], [1, 2, 3]]

my_list5a[1] = 'bbb'
console.print(my_list5c) # [['a', 'bbb', 'c'], [1, 2, 3]] 

# mixed types

my_list6 = [1, 2, 3]
my_list6[0] = 'a'
console.print(my_list6) # ['a', 2, 3] 