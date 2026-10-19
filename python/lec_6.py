# ==============================================================================
# LECTURE 6: FUNCTIONS & RECURSION IN PYTHON
# ==============================================================================
# Concepts:
# 1. Functions : Code ka ek reusable block jo specific task perform karta hai.
#                Yeh redundancy (code repeat hona) ko kam karta hai (DRY Principle).
# 2. Recursion : Jab koi function khud ko hi baar-baar call karta hai jab tak ki
#                ek Base Case (stopping condition) na aa jaye.
# ==============================================================================


# ==============================================================================
# 1. FUNCTION DEFINITION & RETURN VALUES
# Syntax:
#   def function_name(param1, param2):
#       # code
#       return value
# ==============================================================================
print("--- 1. Function Definition & Return Values ---")

# (A) Function with print (Returns None by default)
def calc_sum(c, d):
    sum1 = c + d
    print("Sum inside function:", sum1)
    return  # Explicitly returning None

calc_sum(1, 2)
calc_sum(4, 8)
calc_sum(8, 17)

# (B) Function with Return Value (Result ko variable mein store kar sakte hain)
def cal_sum(e, f):
    return e + f

sum2 = cal_sum(2, 3)
print("Returned Sum:", sum2)

# (C) Simple greeting function (Zero parameters)
def salam():
    print("Assalamu Alaikum wa Rahmatullahi wa Barakatuh 😊")

salam()

# (D) Understanding Return Value Concept:
# Agar kisi function mein 'return' statement na ho ya khali return ho,
# toh Python automatically 'None' return karta hai:
dua = salam()
print("Return value of salam():", dua)  # Prints: None


# ==============================================================================
# 2. DEFAULT PARAMETERS
# Rule: Default arguments hamesha parameters list ke end (right side) par hone chahiye.
# Example: def func(a, b=10): is VALID. def func(a=10, b): is SYNTAX ERROR.
# ==============================================================================
print("\n--- 2. Default Parameters ---")

def calculator(x=2, y=1):
    result = x * y
    print(f"calculator({x}, {y}) = {result}")
    return result

calculator()       # Uses defaults: x=2, y=1 -> 2
calculator(5, 3)    # Overwrites defaults: x=5, y=3 -> 15


# ==============================================================================
# 3. PRACTICE FUNCTIONS
# ==============================================================================
print("\n--- 3. Practice Functions ---")

# Q1: Average of 3 numbers
def avg(m, n, o):
    result = (m + n + o) / 3
    print(f"Average of ({m}, {n}, {o}): {result:.2f}")

avg(4, 5, 6)
avg(7, 8, 9)

# Q2: Function to print the length of a list
hometowns = ["sillvassa", "bangluru", "upleta", "khandwa", "nanded", "balangir"]
def print_list_len(lst):
    print("Length of list is:", len(lst))

print_list_len(hometowns)

# Q3: Function to print all elements of a list in a single line
def print_elements(lst):
    print("List elements:", end=" ")
    for ele in lst:
        print(ele, end=", ")
    print()

print_elements(hometowns)

# Q4: Function to calculate factorial using loop
def print_facto(m):
    facto = 1
    for ele in range(1, m + 1):
        facto *= ele
    print(f"Loop Factorial of {m}!: {facto}")

print_facto(5)

# Q5: USD to INR Currency Converter (Default rate: 1 USD = 86 INR)
def converter_usd(usd=1, rate=86):
    inr = usd * rate
    print(f"{usd} USD = {inr} INR")

converter_usd(6)
converter_usd(99)

# Q6: Even or Odd Checker Function
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

check_even_odd(17)


# ==============================================================================
# 4. RECURSION IN PYTHON
# Concept:
# - Recursion mein 2 cheezein sabse important hoti hain:
#   1. Base Case: Function kab rukega (warna Infinite Loop & RecursionError ho jayega).
#   2. Recursive Call: Problem ko chhote hisse mein todkar khud ko call karna.
# ==============================================================================
print("\n--- 4. Recursion ---")

# (A) Countdown Demonstration (Backtracking Call Stack)
def show(k):
    if k == -1:  # Base Case: -1 aate hi return ho jao
        return
    print("Countdown:", k)
    show(k - 1)  # Recursive Step
    print(f"Backtracking end for k = {k}")

show(3)

# (B) Recursive Factorial: n! = n * (n - 1)!
# Base Case: 0! = 1 aur 1! = 1
def fact(h):
    if h == 0 or h == 1:
        return 1
    return h * fact(h - 1)

print("\nRecursive Factorial of 4!:", fact(4))  # 4 * 3 * 2 * 1 = 24

# (C) Recursive Sum of First N Natural Numbers: sum(n) = n + sum(n - 1)
def rec_sum(n):
    if n == 0 or n == 1:
        return n
    return n + rec_sum(n - 1)

print("Recursive Sum of first 5 numbers:", rec_sum(5))  # 5 + 4 + 3 + 2 + 1 = 15

# (D) Recursive List Printing (Traversing list without for-loop)
def print_list_recursive(lst, idx=0):
    if idx == len(lst):  # Base Case: Index jab list ki length ke barabar ho jaye
        return
    print(f"Index {idx} -> {lst[idx]}")
    print_list_recursive(lst, idx + 1)

sample_list = ["a", "b", "c", "d", "e"]
print("\nRecursive List Traversal:")
print_list_recursive(sample_list)