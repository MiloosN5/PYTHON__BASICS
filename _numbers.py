from rich.console import Console

console = Console()

console.print(2 + 5, type(2 + 5)) # 7 <class 'int'>
console.print(100 - 20 * 2, type(100 - 20 * 2)) # 60 <class 'int'>

console.print(100 / 3, type(100 / 3)) # 33.333333333333336 <class 'float'>
console.print(100 / 2, type(100 / 2)) # 50.0 <class 'float'>
console.print(100.0 / 2, type(100.0 / 2)) # 50.0 <class 'float'>

console.print(100 // 33, type(100 // 33)) # 3 <class 'int'>
console.print(100 // 1, type(100 // 1)) # 100 <class 'int'>
console.print(100 // 50, type(100 // 50)) # 2 <class 'int'>
console.print(50 // 100, type(50 // 100)) # 0 <class 'int'>

console.print(100 % 33, type(100 % 33)) # 1 <class 'int'>
console.print(100 % 1, type(100 % 1)) # 0 <class 'int'>
console.print(100 % 50, type(100 % 50)) # 0 <class 'int'>
console.print(50 % 100, type(50 % 100)) # 50 <class 'int'>

console.print(100 / 3 - 3, type(100 / 3 - 3)) # 30.333333333333336 <class 'float'>
console.print(100.0 / 2 * 2, type(100.0 / 2 * 2)) # 100.0 <class 'float'>

console.print(7 ** 3, type(7 ** 3)) # 343 <class 'int'>
console.print(7 ** 0, type(7 ** 0)) # 1 <class 'int'>
console.print(7 ** -2, type(7 ** -2)) # 0.02040816326530612 <class 'float'>

# console.print(10 * None) # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

console.print(3 * 'love', type(3 * 'love')) # lovelovelove <class 'str'>
console.print(3 * [2, 8], type(3 * [2, 8])) # [2, 8, 2, 8, 2, 8] <class 'list'>

console.print(int("20"), type(int("20"))) # 20 <class 'int'>
console.print(int('20'), type(int('20'))) # 20 <class 'int'>
# console.print(int([2]), type(int([2]))) # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# console.print(int('b\'ABC\''), type(int('b\'ABC\''))) # ValueError: invalid literal for int() with base 10: "b'ABC'"
# console.print(int(b'ABC'), type(int(b'ABC'))) # ValueError: invalid literal for int() with base 10: b'ABC'
console.print(int(b'123'), type(int(b'123'))) # 123 <class 'int'>
console.print(int(bytearray(b'123')), type(int(bytearray(b'123')))) # 123 <class 'int'>