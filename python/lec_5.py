# ==============================================================================
# LECTURE 5: LOOPS IN PYTHON (while, for, range, break, continue, pass)
# ==============================================================================
# Concept:
# - Loops ka use kisi specific task ya code block ko baar-baar repeat karne ke liye hota hai.
# - Do tarah ke loops hote hain:
#   1. while loop : Condition based (tab tak chalega jab tak condition True hai).
#   2. for loop   : Traversal based (kisi sequence jaise list, string, tuple par iterate karta hai).
# ==============================================================================


# ==============================================================================
# 1. WHILE LOOPS BASICS
# Structure: Initialization -> while Condition -> Body -> Increment / Decrement
# ==============================================================================
print("--- 1. While Loop Basics ---")

# (A) Count 1 to 5
a = 1
while a <= 5:
    print("salam", a)
    a += 1
print("Final value of a outside loop:", a)

# (B) Count 1 to 5 (simple numbers)
b = 1
while b <= 5:
    print(b)
    b += 1
print("loop ended")

# (C) Negative range iteration
c = -5
while c <= 0:
    print("Negative count:", c)
    c += 1

# (D) Reverse counting (5 down to 1)
d = 5
while d >= 1:
    print("Reverse:", d)
    d -= 1


# ==============================================================================
# 2. WHILE LOOP PRACTICE QUESTIONS
# ==============================================================================
print("\n--- 2. While Loop Practice Questions ---")

# Q1: Print numbers from 1 to 10 (sample of 1 to 100)
print("\n[Q1: Print numbers 1 to 10]")
e = 1
while e <= 10:
    print(e, end=" ")
    e += 1
print()

# Q2: Print numbers from 10 down to 1
print("\n[Q2: Print numbers 10 down to 1]")
f = 10
while f >= 1:
    print(f, end=" ")
    f -= 1
print()

# Q3: Print even numbers up to 10
print("\n[Q3: Even numbers up to 10]")
i = 2
while i <= 10:
    print(i, end=" ")
    i += 2
print()

# Q4: Print odd numbers up to 10
print("\n[Q4: Odd numbers up to 10]")
j = 1
while j <= 10:
    print(j, end=" ")
    j += 2
print()

# Q5: Print multiplication table of a number n
print("\n[Q5: Multiplication Table]")
n = int(input("enter a number for table: "))
o = 1
while o <= 10:
    print(f"{n} x {o} = {n * o}")
    o += 1

# Q6: Print elements of a list using while loop
print("\n[Q6: List Traversal via Index]")
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(list1):
    print(f"Index {idx} -> Value {list1[idx]}")
    idx += 1

# Q7: Linear search in a tuple using while loop & break
print("\n[Q7: Linear Search with Break]")
list2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter a number to search in tuple: "))
i = 0
found = False
while i < len(list2):
    if list2[i] == x:
        print(f"Element {x} found at index: {i}")
        found = True
        break  # Target milte hi loop ko turant terminate kar do
    else:
        print("searching...")
    i += 1

if not found:
    print("Element not found in tuple!")


# ==============================================================================
# 3. LOOP CONTROL STATEMENTS: break vs continue
# - break    : Loop ko poori tarah terminate karke loop ke bahar nikal deta hai.
# - continue : Current iteration ko skip karta hai aur seedhe agle round par chala jata hai.
# ==============================================================================
print("\n--- 3. break vs continue ---")

# (A) break demonstration
print("\n[Demonstrating break at 3]")
z = 1
while z <= 5:
    print(z)
    if z == 3:
        print("Breaking loop here!")
        break
    z += 1

# (B) continue demonstration (Skip number 3)
print("\n[Demonstrating continue to skip 3]")
k = 0
while k <= 5:
    if k == 3:
        k += 1
        continue  # 3 print nahi hoga, seedhe agla number aayega
    print(k)
    k += 1


# ==============================================================================
# 4. FOR LOOPS IN PYTHON
# Concept: Sequence (list, tuple, string) ke har element par one-by-one iterate karta hai.
# ==============================================================================
print("\n--- 4. For Loops ---")

# (A) List Iteration
k_list = [1, 2, 3, 4, 5]
for val in k_list:
    print("List item:", val)

# (B) Tuple Iteration
veggies = ("potato", "tomato", "brinjal", "apple")
for item in veggies:
    print("Item:", item)

# (C) Linear Search using For Loop & enumerate
print("\n[Linear Search using for loop]")
num_tuple = (1, 3, 5, 7, 9, 16, 36, 49, 54, 78, 87)
search_target = 78
for idx, val in enumerate(num_tuple):
    if val == search_target:
        print(f"Target {search_target} found at index: {idx}")
        break


# ==============================================================================
# 5. THE range() FUNCTION
# Syntax:
# - range(stop)             : 0 se lekar (stop - 1) tak
# - range(start, stop)      : start se lekar (stop - 1) tak
# - range(start, stop, step): start se lekar (stop - 1) tak step size ke jump ke sath
# ==============================================================================
print("\n--- 5. The range() Function ---")

# (A) range(stop)
print("range(5) output:")
for ele in range(5):
    print(ele, end=" ")
print()

# (B) range(start, stop)
print("range(2, 6) output:")
for ele in range(2, 6):
    print(ele, end=" ")
print()

# (C) range(start, stop, step)
print("range(2, 12, 2) output (Even numbers):")
for ele in range(2, 12, 2):
    print(ele, end=" ")
print()

# (D) Reverse range (10 down to 1)
print("Reverse range(10, 0, -1):")
for ele in range(10, 0, -1):
    print(ele, end=" ")
print()


# ==============================================================================
# 6. THE pass STATEMENT
# Concept: 'pass' ek null statement hoti hai. Jab hume syntax complete rakhna ho
# lekin koi code execute nahi karna ho (placeholder ke roop mein), tab 'pass' use hota hai.
# ==============================================================================
print("\n--- 6. The pass Statement ---")
for i in range(3):
    pass  # Kuch nahi karega, error se bachayega

if i < 5:
    pass  # Future implementation placeholder
print("pass statement executed without error!")


# ==============================================================================
# 7. PRACTICE ALGORITHMS: SUM & FACTORIAL
# ==============================================================================
print("\n" + "="*50)
print("PRACTICE ALGORITHMS: SUM & FACTORIAL")
print("="*50)

# Problem 1: Sum of First N Numbers
# Formula / Logic: 1 + 2 + 3 + ... + n
n_val = 5
total_sum_for = 0
for ele in range(1, n_val + 1):
    total_sum_for += ele
print(f"Sum of first {n_val} numbers (via for loop)   : {total_sum_for}")

# Same using while loop
start_pt = 1
total_sum_while = 0
while start_pt <= n_val:
    total_sum_while += start_pt
    start_pt += 1
print(f"Sum of first {n_val} numbers (via while loop) : {total_sum_while}")

# Problem 2: Factorial of First N Numbers
# Formula / Logic: n! = 1 * 2 * 3 * ... * n
m_val = 5
factorial_result = 1
for ele in range(1, m_val + 1):
    factorial_result *= ele
print(f"Factorial of {m_val}!                        : {factorial_result}")
