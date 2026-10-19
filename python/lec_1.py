# ==============================================================================
# LECTURE 1: PYTHON BASICS, OPERATORS & TYPE CONVERSION
# ==============================================================================

# Base variables
a = 17
b = 8

# ==============================================================================
# 1. ARITHMETIC OPERATORS (+, -, *, /, %, **)
# Kaam: Numbers par basic aur advanced mathematical calculations perform karna.
# ==============================================================================
print("--- 1. Arithmetic Operators ---")
print("Addition (a + b)        :", a + b)       # 17 + 8 = 25
print("Subtraction (a - b)     :", a - b)       # 17 - 8 = 9
print("Multiplication (a * b)  :", a * b)       # 17 * 8 = 136
print("Division (a / b)        :", a / b)       # 17 / 8 = 2.125 (Python hamesha float return karta hai)
print("Modulo / Remainder (a % b):", a % b)     # 17 % 8 = 1 (Division ke baad bacha hua sheshphal)
print("Power / Exponent (a ** b) :", a ** b)    # 17^8 (17 ki power 8)


# ==============================================================================
# 2. RELATIONAL / COMPARISON OPERATORS (==, !=, <, >, >=, <=)
# Kaam: Do values ko compare karna. Inka result hamesha Boolean (True ya False) hota hai.
# ==============================================================================
print("\n--- 2. Relational Operators ---")
print("Equal to (a == b)                 :", a == b)   # Dono barabar hain? -> False
print("Not equal to (a != b)             :", a != b)   # Dono barabar nahi hain? -> True
print("Less than (a < b)                 :", a < b)    # Kya a chota hai b se? -> False
print("Greater than (a > b)              :", a > b)    # Kya a bada hai b se? -> True
print("Greater than or equal to (a >= b) :", a >= b)   # Bada ya barabar? -> True
print("Less than or equal to (a <= b)    :", a <= b)   # Chota ya barabar? -> False


# ==============================================================================
# 3. ASSIGNMENT OPERATORS (=, +=, -=, *=, /=, %=, **=)
# Kaam: Variable ki current value ko update karke wapas usi mein store karna.
# Short-hand: `number += 8` ka matlab hota hai `number = number + 8`.
# ==============================================================================
print("\n--- 3. Assignment Operators ---")
number = 17

number += 8   # number = 17 + 8 -> 25
print("number += 8  :", number)

number -= 8   # number = 25 - 8 -> 17
print("number -= 8  :", number)

number *= 8   # number = 17 * 8 -> 136
print("number *= 8  :", number)

number /= 8   # number = 136 / 8 -> 17.0
print("number /= 8  :", number)

number %= 8   # number = 17.0 % 8 -> 1.0
print("number %= 8  :", number)

number **= 8  # number = 1.0 ** 8 -> 1.0
print("number **= 8 :", number)


# ==============================================================================
# 4. LOGICAL OPERATORS (NOT, AND, OR)
# Kaam: Multiple conditions ko aapas mein jodna ya invert karna.
# Rules:
# - not : Result ko ulat deta hai (True -> False, False -> True).
# - and : Agar dono operands True hain tabhi True aayega, warna False.
# - or  : Agar koi ek bhi operand True hai toh final answer True aayega.
# ==============================================================================
print("\n--- 4. Logical Operators ---")

# (A) NOT Operator
y = 17
z = 8
print("y == z       :", y == z)         # False
print("not(y == z)  :", not(y == z))    # False ka ulta -> True

# (B) AND Operator
m = True
n = False
print("m and n      :", m and n)         # Ek False hai, isliye answer False hoga

# (C) OR Operator
print("m or n       :", m or n)          # Ek True hai, isliye answer True hoga

# Practice Expressions
print("Practice (m == n or m != n) :", m == n or m != n)  # (False or True) -> True
print("Practice (m == n and n != n):", m == n and n != n) # (False and False) -> False


# ==============================================================================
# 5. TYPE CONVERSION (Implicit) vs TYPE CASTING (Explicit)
# - Implicit Conversion : Python automatically chhote type ko bade type mein promote karta hai (e.g. int + float = float).
# - Explicit Casting    : Developer zabardasti type change karta hai jaise float('17.0') ya str(8).
# ==============================================================================
print("\n--- 5. Type Conversion & Casting ---")
c = 17
d = 8.0
print("c + d (Automatic Float):", c + d, "| Type:", type(c + d))

# String ko float mein cast karna
e = float('17.0')  # String '17.0' float 17.0 ban gaya
f = 8
print("Type of e (float)      :", type(e))
print("Type of f (int)        :", type(f))
print("e + f                  :", e + f)

# Integer ko string mein cast karna
g = 17
h = str(8)         # 8 number se string '8' ban gaya
print("Type of h (str)        :", type(h))


# ==============================================================================
# 6. PRACTICE QUESTIONS (USER INPUT)
# ==============================================================================
print("\n" + "="*50)
print("PRACTICE QUESTIONS (INPUT SECTION)")
print("="*50)

# Q1: Write a program to input 2 numbers and print their sum
print("\n--- Q1: Sum of Two Numbers ---")
first = float(input("enter first num: "))
second = float(input("enter second num: "))
print("sum is:", first + second)

# Q2: Write a program to input the side of a square and print its area (side^2)
print("\n--- Q2: Area of Square ---")
area = float(input("enter your side: "))
print("area of square is:", area ** 2)

# Q3: Write a program to input 2 floating numbers and print their average
print("\n--- Q3: Average of Two Numbers ---")
o = float(input("enter no 1: "))
p = float(input("enter no 2: "))
print("the average is:", (o + p) / 2)

# Q4: WAP to input 2 int numbers (a and b). Print True if a >= b, else print False.
print("\n--- Q4: Check if First Number is Greater Than or Equal ---")
q = int(input("enter no 1: "))
r = int(input("enter no 2: "))
print("Result (q >= r):", q >= r)
