a = "vishesh"
b = 23
c = True
d = None
e = 5.6
print(type(a), type(b), type(c), type(d), type(e))

# ---------- Implicit Typecasting ----------
a = 10        # int
b = 5.5       # float
c = a + b     # int + float → float
print("Result of a + b:", c)
print("Type of result:", type(c))

# ---------- Explicit Typecasting ----------

# Float to int
a = 3.9
b = int(a)
print("Float to int:", b)

# Int to float
a = 5
b = float(a)
print("Int to float:", b)

# Number to string
x = 100
y = str(x)
print("Number to string:", y, type(y))

# String to int (valid case)
s = "123"
n = int(s)
print("String to int:", n + 1)

# Boolean conversions
print("Bool of 0:", bool(0)) #False
print("Bool of 5:", bool(5)) #True
print("Bool of empty string:", bool("")) #False
print("Bool of non-empty string:", bool("Hi")) #True

