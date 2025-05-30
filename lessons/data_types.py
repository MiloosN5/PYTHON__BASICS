from rich.console import Console
import math

console = Console()

# Numeric types (int, float, complex)
my_x1 = 10
my_x2 = 3.14
my_x3 = 1 + 2j
console.print(f"Integer: {my_x1}, Float: {my_x2}, Complex: {my_x3}") # Integer: 10, Float: 3.14, Complex: (1+2j)
console.print(type(my_x1)) # <class 'int'>
console.print(type(my_x1).__name__) # int
console.print(type(my_x2)) # <class 'float'>
console.print(type(my_x2).__name__) # float
console.print(type(my_x3)) # <class 'complex'>
console.print(type(my_x3).__name__) # complex

# Sequence types (list, tuple, range)
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_range = range(7)
console.print(f"List: {my_list}, Tuple: {my_tuple}, Range: {my_range}") # List: [1, 2, 3], Tuple: (4, 5, 6), Range: range(0, 7)
console.print(type(my_list)) # <class 'list'>
console.print(type(my_list).__name__) # list
console.print(type(my_tuple)) # <class 'tuple'>
console.print(type(my_tuple).__name__) # tuple
console.print(type(my_range)) # <class 'range'>
console.print(type(my_range).__name__) # range

# Text type (str)
my_string = "Hello, Python!"
console.print(f"String: {my_string}") # String: Hello, Python!
console.print(type(my_string)) # <class 'str'>
console.print(type(my_string).__name__) # str

# Mapping type (dict)
my_dict = {"a": 1, "b": 2}
console.print(f"Dictionary: {my_dict}") # Dictionary: {'a': 1, 'b': 2}
console.print(type(my_dict)) # <class 'dict'>
console.print(type(my_dict).__name__) # dict

# Set types (set, frozenset)
my_set = {1, 2, 3}
my_frozenset = frozenset((1, 2, 3))
console.print(f"Set: {my_set}, Frozen set: {my_frozenset}") # Set: {1, 2, 3}, Frozen set: frozenset({1, 2, 3})
console.print(type(my_set)) # <class 'set'>
console.print(type(my_set).__name__) # set
console.print(type(my_frozenset)) # <class 'frozenset'>
console.print(type(my_frozenset).__name__) # frozenset

# Boolean type
my_flag1 = True
my_flag2 = False
# my_flag3= true # NameError: name 'true' is not defined. Did you mean: 'True'?
# my_flag4 = false # NameError: name 'false' is not defined. Did you mean: 'False'?
my_flag5 = 1
my_flag6 = 0
console.print(f"Boolean: {my_flag1}, Boolean: {my_flag2}") # Boolean: True, Boolean: False
console.print(type(my_flag1)) # <class 'bool'>
console.print(type(my_flag1).__name__) # bool
console.print(type(my_flag2)) # <class 'bool'>
console.print(type(my_flag2).__name__) # bool
console.print(type(my_flag5)) # <class 'int'>
console.print(type(my_flag5).__name__) # int
console.print(type(my_flag6)) # <class 'int'>
console.print(type(my_flag6).__name__) # int

# Binary types (bytes, bytearray, memoryview)
my_bytes1 = bytes([65, 66, 67])
my_bytes2 = bytes("Hello", "utf-8")
console.print(f"Byte: {my_bytes1!r}, Byte: {my_bytes2!r}") # Byte: b'ABC', Byte: b'Hello'
console.print(type(my_bytes1)) # <class 'bytes'>
console.print(type(my_bytes1).__name__) # bytes
console.print(type(my_bytes2)) # <class 'bytes'>
console.print(type(my_bytes2).__name__) # bytes

my_bytearray1 = bytearray([65, 66, 67])
console.print(my_bytearray1[0]) # 65
console.print(f"Bytearr: {my_bytearray1}") # Bytearr: bytearray(b'ABC')
my_bytearray1[1] = 90
console.print(f"Bytearr: {my_bytearray1}") # Bytearr: bytearray(b'AZC')
my_bytearray1.append(68)
console.print(f"Bytearr: {my_bytearray1}") # Bytearr: bytearray(b'AZCD')
console.print(type(my_bytearray1)) # <class 'bytearray'>
console.print(type(my_bytearray1).__name__) # bytearray

my_bytearray2 = bytearray([65, 66, 67]) 
my_memoryView_1 = memoryview(my_bytearray2)
console.print(my_memoryView_1[0])
console.print(f"Memory view: {my_memoryView_1}") # Memory view: <memory at 0x0000021DFB064D00>
my_memoryView_1[1] = 90
console.print(f"Bytearr: {my_bytearray2}") # Bytearr: bytearray(b'AZC')
console.print(f"Memory view: {my_memoryView_1}") # Memory view: <memory at 0x0000021DFB064D00>
console.print(type(my_memoryView_1)) # <class 'memoryview'> 
console.print(type(my_memoryView_1).__name__) # memoryview

# Special types (others)

## module
console.log(type(math)) # <class 'module'>  

## function
def my_Func():
    console.print("Hello")
console.print(type(my_Func)) # <class 'function'>
console.print(type(my_Func.__code__)) # <class 'code'>

## Class & type
class My_Class:
    pass 
console.print(type(My_Class)) # <class 'type'>
console.print(type(type(12))) # <class 'type'>

## None
console.print(type(None)) # <class 'NoneType'>

## ellipsis (...)
console.print(type(...)) # <class 'ellipsis'>

## NotImplemented
console.print(type(NotImplemented)) # <class 'NotImplementedType'>



