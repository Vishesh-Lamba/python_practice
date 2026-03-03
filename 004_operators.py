#Arithmetic operator
print(-17 / 5)  # division, it always return float , -3.4
print(-17 // 5) #floor division, divide krke jo float aayega usko smallest int m change krdega ,If any of the numbers is float, it returns output in float, -4
print(17 % 5) #Gives remainder , 2
print(2**5) # 2 to power 5, 32

#Comparison Operator
a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#logical Operator
a = True
b = False
print(a and b) # only true when both are true
print(a or b) # only false when both are false
print(not a) # true ka false, false ka true


# Membership Operator(in, not in), Used to check whether a value is in a sequence like a list, string, tuple, etc.
fruits = ['apple', 'banana', 'mango']

print('apple' in fruits)     # True
print('grape' not in fruits) # True
print('banana' not in fruits) # False

text = "hello world"
print('world' in text)       # True
print('World' in text)       # False (case-sensitive)

#Identity Operators(is, is not), Used to check if two variables refer to the same object in memory.
x = [1, 2, 3]
y = x           # Same object reference
z = [1, 2, 3]   # Same content, different object

print(x is y)       # True
print(x is z)       # False
print(x == z)       # True (content is same)
print(x is not z)   # True
# is checks identity (memory location), == checks value.

#Bitwise operators operate on binary digits (bits) of integers. Python stores integers in binary form internally, and bitwise operators allow us to manipulate these bits directly.
a = 5       # 0101
b = 3       # 0011
print(a & b)  # 1 (0001) Bitwise And
print(a | b)  # 7 (0111) Bitwise OR
print(a ^ b)  # 6 (0110) Bitwise XOR, Returns 1 if bits are different, else 0.
print(~a)    # -6 Bitwise NOT, Inverts each bit (0 becomes 1, 1 becomes 0).
print(a << 1)  # 10 (00001010) Left shift, Shifts bits to the left, filling with 0s. Equivalent to multiplying by 2ⁿ.
print(a << 2)  # 20 (00010100)
print(a >> 1)  # 10 (00001010) Right shift, Shifts bits to right, dropping rightmost bits. Equivalent to integer division by 2ⁿ.
print(a >> 2)  # 5  (00000101)


count = 5
count += 3
print("count after += 3:", count)  # Output: 8
