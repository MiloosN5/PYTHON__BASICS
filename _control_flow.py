from rich.console import Console
from enum import Enum

console = Console()

#IF STATEMENT

if_input1 = int(input("Please enter your number: ")) 
if if_input1 < 0:
    if_input1 = 0
    console.print('Negative changed to zero')
elif if_input1 == 0:
    console.print('Zero')
elif if_input1 == 1:
    console.print('One')
else:
    console.print('More')
'''
input: 25
output: More
'''
'''
input: -5
output: Negative changed to zero
'''

#FOR STATEMENT

for_words1 = ['cat', 'dog', 'horse', 'sea turtle']
for w in for_words1:
    console.print(w, len(w))
'''
cat 3
dog 3
horse 5
sea turtle 10
'''

## Change existing collection (loop over a copy)

### Create a sample collection
for_users1 = {'Jack': 'active', 'Kate': 'inactive', 'Michael': 'active'}
console.print(for_users1) # {'Jack': 'active', 'Kate': 'inactive', 'Michael': 'active'}

### Iterate over a copy
for user, status in for_users1.copy().items():
    if status == 'inactive':
        del for_users1[user]
console.print(for_users1) # {'Jack': 'active', 'Michael': 'active'}

## Create a new collection
for_active_users1 = {}
for user, status in for_users1.items():
    if status == 'active':
        for_active_users1[user] = status
console.print(for_active_users1) # {'Jack': 'active', 'Michael': 'active'}

# The range() Function

for i in range(5):
    console.print(i)
'''
0
1
2
3
4
'''

console.print(list(range(5, 10))) # [5, 6, 7, 8, 9]
console.print(list(range(0, 10, 3))) # [0, 3, 6, 9]
console.print(list(range(-10, -100, -30))) # #[-10, -40, -70]

for_word_sequence = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(for_word_sequence)):
    console.print(i, for_word_sequence[i])
'''
0 Mary
1 had
2 a
3 little
4 lamb
'''

console.print(range(10)) # range(0, 10)
console.print(range(0, 10)) # range(0, 10)

console.print(sum(range(4))) # 6

# BREAK & CONTINUE STATEMENTS

## break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            console.print(f"{n} equals {x} * {n//x}")
            break
'''
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
'''

## continue
for num in range(2, 10):
    if num % 2 == 0:
        console.print(f"Found an even number {num}")
        continue
    console.print(f"Found an odd number {num}")
'''
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
'''

# ELSE CLAUSE

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            console.print(n, 'equals', x, '*', n//x)
            break
    else:
         console.print(n, 'is a prime number')
'''
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
'''

# PASS STATEMENT

'''
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
'''

## for creating minimal classes
'''
class MyEmptyClass:
    pass
'''

## place-holder for a function or conditional body when you are working on new code
'''
def initlog(*args):
    pass   # Remember to implement this!
'''

# MATCH STATEMENT

def match_http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
console.print(match_http_error(403)) # Not allowed
console.print(match_http_error(411)) # Something's wrong with the internet
        
def match_point_coordinates(point):
    match point:
        case (0, 0):
             console.print("Origin")
        case (0, y):
             console.print(f"Y={y}")
        case (x, 0):
             console.print(f"X={x}")
        case (x, y):
             console.print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
match_point_coordinates((3, 5)) # X=3, Y=5
match_point_coordinates((5, 0)) # X=5

class MatchColor1(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

match_color = MatchColor1(input("Enter your choice of 'red', 'blue' or 'green': "))
'''
input: blue
output: I'm feeling the blues :(
'''
'''
input: Blue
output: ValueError: 'Blue' is not a valid Color
'''

match match_color:
    case MatchColor1.RED:
         console.print("I see red!")
    case MatchColor1.GREEN:
         console.print("Grass is green")
    case MatchColor1.BLUE:
         console.print("I'm feeling the blues :(")

# FUNCTIONS

def func_fib1(n):   
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    console.print()

func_fib1(2000) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
console.print(func_fib1) # <function fib at 0x0000022BF51F8680>
func_f1 = func_fib1
func_f1(100) # 0 1 1 2 3 5 8 13 21 34 55 89

console.print(func_fib1(0)) # None

def func_fib2(n):  
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)   
        a, b = b, a+b
    return result

func_f2 = func_fib2(100)    
console.print(func_f2) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 

