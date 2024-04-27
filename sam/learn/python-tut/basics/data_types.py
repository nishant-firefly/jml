print("""
Python has several built-in data types, including:
Numeric Types: Integers (int), floating-point numbers (float), and complex numbers (complex).
Sequence Types: Lists (list), tuples (tuple), and strings (str).
Mapping Types: Dictionaries (dict).
Set Types: Sets (set).
Boolean Type: Boolean (bool).
Python also supports type conversion functions like int(), float(), str(), etc., for converting between different types.
""")
i,f,b,s,c = 1, 2.3, True, "Text String", 1+2j # Equicalent to i=1 nl f=2.3 , ..... in new line @TODO  
print(i, type(i)) # 1 <class 'int'>
print(b, type(b)) # True <class 'bool'>
print(f, type(f)) # 2.3 True <class 'float'>
print(s, type(s)) # Text String <class 'str'>
print(c, type(c)) # (1+2j) <class 'complex'>

# int, float, bool, str