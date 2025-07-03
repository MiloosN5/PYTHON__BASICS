from rich.console import Console
from enum import Enum

console = Console()

# DEFINING FUNCTIONS

def func_1(n):   
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    console.print()

func_1(2000) # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
console.print(func_1) # <function func_1 at 0x0000022BF51F8680>
f_1 = func_1
f_1(100) # 0 1 1 2 3 5 8 13 21 34 55 89

def func_2(n):  
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)   
        a, b = b, a+b
    return result

f_2 = func_2(100)    
console.print(f_2) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 

# DEFAULT ARGUMENT VALUES

def func_3(prompt, retries=3, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in { 'y', 'ye', 'yes' }:
            return True
        if reply in { 'n', 'no', 'nop', 'nope' }:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        console.print(reminder)

func_3('Do you really want to quit?');
'''
message for prompt: Do you really want to quit? (attempt: 1)
prompt: s
-------------------------------------------------------------
message for prompt: Please try again!
message for prompt: Do you really want to quit? (attempt: 2, retry: 1)
prompt: something
-------------------------------------------------------------
message for prompt: Please try again!
message for prompt: Do you really want to quit? (attempt: 3, retry: 2)
prompt: horse
-------------------------------------------------------------
message for prompt: Please try again!
message for prompt: Do you really want to quit? (attempt: 4, retry: 3)
prompt: nopee
ValueError: invalid user response
'''
func_3('OK to overwrite the file?', 2);
'''
message for prompt: OK to overwrite the file? (attempt: 1)
prompt: s
-------------------------------------------------------------
message for prompt: Please try again!
message for prompt: OK to overwrite the file? (attempt: 2, retry: 1)
prompt: something
-------------------------------------------------------------
message for prompt: Please try again!
message for prompt: OK to overwrite the file? (attempt: 3, retry: 2)
ValueError: invalid user response
'''
func_3('OK to overwrite the file?', 2, 'Come on, only yes or no!');
'''
message for prompt: OK to overwrite the file? (attempt: 1)
prompt: s
-------------------------------------------------------------
message for prompt: Come on, only yes or no!
message for prompt: OK to overwrite the file? (attempt: 2, retry: 1)
prompt: yyy
-------------------------------------------------------------
message for prompt: Come on, only yes or no!
message for prompt: OK to overwrite the file? (attempt: 3, retry: 2)
ValueError: invalid user response
'''

## defining scope

i_4 = 5

def func_4(arg=i_4):
    console.print(arg);

i_4 = 10
func_4(); # 5
func_4(i_4); # 10

## default value is mutable object

a_5 = []

def func_5(a_5, L=[]):
    L.append(a_5);
    return L;

console.print(func_5(1)); # [1]
console.print(func_5(5)); # [1, 5]
console.print(func_5(2)); # [1, 5, 2]
# console.print(L); # L is not defined

a_6 = []

def func_6(a_6, L=None):
    if L is None:
        L = [];
    L.append(a_6);
    return L;

console.print(func_6(1)); # [1]
console.print(func_6(5)); # [5]
console.print(func_6(2)); # [2]

# KEYWORD ARGUMENTS

def func_7(a, b = 5, c = 10, d = 7):
    console.print('a', a, '', 'b', b, '', 'c', c, '', 'd', d);
    console.print('sum', a + b + c + d);

func_7(20); # 1 positional argument
'''
a 20  b 5  c 10  d 7
sum 42
'''
func_7(a=20); # 1 keyword argument
'''
a 20  b 5  c 10  d 7
sum 42
'''
func_7(a=30, b = 200); # 2 keyword arguments
'''
a 30  b 200  c 10  d 7
sum 247
'''
func_7(b=200, a = 30); # 2 keyword arguments
'''
a 30  b 200  c 10  d 7
sum 247
'''
func_7(70, 80, 15); # 3 positional arguments
'''
a 70  b 80  c 15  d 7
sum 172
'''
func_7(70, d=100); # 1 positional, 1 keyword
'''
a 70  b 5  c 10  d 100
sum 185
'''

## invalid invokes
# func_7(); # TypeError: func_7() missing 1 required positional argument: 'a'
# func_7(a=70, 50); # Positional argument cannot appear after keyword arguments
# func_7(20, a=50); # TypeError: func_7() got multiple values for argument 'a'
# func_7(a=20, m=50); # TypeError: func_7() got an unexpected keyword argument 'm'

## restrictions
def func_8(a):
    pass

func_8(a = 10);
# func_8(12, a = 10); # TypeError: func_8() got multiple values for argument 'a'

# ARBITRARY ARGUMENTS (*args, **kwargs)

def func_9(a, *args, **kwargs):
    console.print('formal parameter: ', a);
    console.print('*args: ', args);
    console.print('**kwargs: ', kwargs);

func_9('apple', 'blue', 'red', 'green', country="Serbia", year=2025);
'''
formal parameter:  apple
*args:
('blue', 'red', 'green')
**kwargs:
{'country': 'Serbia', 'year': 2025}
'''

# SPECIAL PARAMETERS

def func_10(arg): # no restrictions - arguments may be passed by position or keyword
    console.print(arg);

func_10(5); # 5
func_10(arg=5); # 5

def func_11(arg, /): # restricted to only use positonal parameters
    console.print(arg);

func_11(5); # 5
# func_11(arg=5); # TypeError: func_11() got some positional-only arguments passed as keyword arguments: 'arg'

def func_12(*, arg): # only allows keyword arguments
    console.print(arg);

# func_12(5); # TypeError: func_12() takes 0 positional arguments but 1 was given
func_12(arg=5); # 5

def func_13(pos_only, /, standard, *, kwd_only):
    console.print(pos_only, standard, kwd_only);

func_13(1, 2, kwd_only=3); # 123
func_13(1, standard=2, kwd_only=3); # 123
# func_13(pos_only=1, standard=2, kwd_only=3); # TypeError: func_13() got some positional-only arguments passed as keyword arguments: 'pos_only'

# POTENTIAL COLLISION

def func_14(name, **kwds): # potential collision between the positional argument name and **kwds which has name as a key
    return 'name' in kwds;

# console.print(func_14(1, **{'name': 2})); # TypeError: func_14() got multiple values for argument 'name'

def func_15(name, /, **kwds): # But using / (positional only arguments), it is possible since it allows name as a positional argument and 'name' as a key in the keyword arguments
    return 'name' in kwds;

console.print(func_15(1, **{'name': 2})); # True

# UNPACKING ARGUMENT LISTS

console.print(list(range(5, 9))); # [5, 6, 7, 8]
args_16 = [5, 9];
console.print(list(range(*args_16))); # [5, 6, 7, 8]

def func_17(a, b='some', c='thing'):
    console.print('a', a, '', 'b', b, '', 'c', c);

d_17_1 = {"a": 22, "b": 19, "c": 8};
d_17_2 = {"a": 22, "c": 8};
d_17_3 = {"b": 19, "c": 8};
func_17(**d_17_1); # a 22  b 19  c 8
func_17(**d_17_2); # a 22  b some  c 8
# func_17(**d_17_3); # TypeError: func_17() missing 1 required positional argument: 'a'

# LAMBDA EXPRESSIONS

def func_18(n):
    return lambda x: x + n;

f_18 = func_18(44);
console.print(f_18(0)); # 44
console.print(f_18(5)); # 49

pairs_19 = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')];
pairs_19.sort(key=lambda pair: pair[1]);
console.print(pairs_19); # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# DOCUMENTATION STRINGS

class Dog_20:
    """
    A simple Dog_20 class.

    Attributes:
        name (str): The name of the dog.
        age (int): The age of the dog.

    Methods:
        bark(): Prints a bark sound.
    """

    def __init__(self, name, age):
        """
        Initialize the Dog_20 with name and age.
        """
        self.name = name
        self.age = age

    def bark(self):
        """
        Make the dog bark.
        """
        print(f"{self.name} says woof!")

d_20 = Dog_20('Jacky', 5);
console.print(d_20.__doc__);
'''
    A simple Dog_20 class.

    Attributes:
        name (str): The name of the dog.
        age (int): The age of the dog.

    Methods:
        bark(): Prints a bark sound.
'''

# FUNCTION ANNOTATIONS

def func_21(ham: str, eggs: str = 'eggs') -> str:
    console.print("Annotations:", func_21.__annotations__);
    console.print("Arguments:", ham, eggs);
    return ham + ' and ' + eggs;

func_21('spam');
'''
Annotations:
{'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
Arguments: spam eggs
'''