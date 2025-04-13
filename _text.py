from rich.console import Console

console = Console()

# Quotes

# single quotes
console.print('some text') # some text
# double quotes
console.print("some text") # some text
# digits & numerals enclosed in quotes are also strings
console.print('2025') # 2025

# Escape

console.print('doesn\'t') # doesn't
console.print("doesn't") # doesn't
console.print("doesn\'t") # doesn't

console.print("you are \"beautiful\"") # you are "beautiful"
console.print('you are "beautiful"') # you are "beautiful"
console.print('you are \"beautiful\"') # you are "beautiful"

console.print('First line.\nSecond line.')
'''
First line.
Second line.
'''
console.print("First line.\nSecond line.")
'''
First line.
Second line.
'''
console.print(r'First line.\nSecond line.') # First line.\nSecond line. 
console.print(r"First line.\nSecond line.") # First line.\nSecond line.

# multiline

console.print("""\
List for shopping1
     -Fish
     -Bread
""")
'''
List for shopping1
     -Fish
     -Bread
'''
console.print("""
List for shopping2
     -Fish
     -Bread
""")
'''
List for shopping
     -Fish
     -Bread
'''
console.print("""\
List for shopping3
     Fish
     Bread
""")
'''
List for shopping3
     Fish
     Bread
'''
console.print("""
List for shopping4
     Fish
     Bread
""")
'''
List for shopping4
     Fish
     Bread
'''

console.print('Put several strings within parentheses '
        'to have them joined together.') # Put several strings within parentheses to have them joined together. 

# concatenation

console.print('pine' + 'apple') # pineapple
console.print('pine''apple') # pineapple
console.print('pine' 'apple') # pineapple

console.print("pine" + "apple") # pineapple
console.print("pine""apple") # pineapple
console.print("pine" "apple") # pineapple

console.print('pine' "apple") # pineapple
console.print("pine" 'apple') # pineapple

prefix = 'Py'
# console.print(prefix'thon') # SyntaxError: invalid syntax
# console.print(prefix 'thon') # SyntaxError: invalid syntax
console.print(prefix + "thon") # Python

# repetition

console.print(3 * 'apple') # appleappleapple

# indexed (subscripted)

console.print('Python'[0]) # P
# console.print('Python'[10]) # IndexError: string index out of range
console.print('Python'[-1]) # n
# console.print('Python'[-10]) # IndexError: string index out of range

console.print('Python'[:2]) # Py
console.print('Python'[:10]) # Python
console.print('Python'[2:]) # thon
console.print('Python'[10:]) # 

console.print('Python'[:2] + 'Python'[2:]) # Python
console.print('Python'[:4] + 'Python'[4:]) # Python

# assignment

word = 'Python'
# word[0] = 'M' # TypeError: 'str' object does not support item assignment
# word[2:] = 'py' # TypeError: 'str' object does not support item assignment

# len

console.print(len('supernatural')) # 12
console.print(len('   supernatural')) # 15
console.print(len('supernatural   ')) # 15
console.print(len('something else')) # 14
console.print(len('something    else')) # 17