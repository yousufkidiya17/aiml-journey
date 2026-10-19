# ==============================================================================
# LECTURE 3: LISTS & TUPLES IN PYTHON
# ==============================================================================
# Concepts:
# 1. Lists  : Built-in mutable (changeable) collection jo ordered sequence mein
#             different data types (int, float, string) ko store kar sakti hai.
# 2. Tuples : Lists ki tarah hi hote hain, lekin immutable (unchangeable) hote hain.
#             Ek baar tuple ban gaya toh uske elements ko modify nahi kiya ja sakta.
# ==============================================================================


# ==============================================================================
# 1. LISTS BASICS & MUTABILITY
# - Strings immutable hoti hain (str[0] = 'a' error deta hai).
# - Lists MUTABLE hoti hain (list[0] = 99 successfully update ho jata hai).
# ==============================================================================
print("--- 1. Lists Basics & Mutability ---")

marks = [85.5, 92.0, 78.5, 90.0, 65.0]
print("Original Marks List :", marks)
print("Data Type           :", type(marks))
print("Total Elements (len):", len(marks))

# Mutability test (Value change karna):
marks[0] = 95.0
print("After marks[0] = 95 :", marks)

# Mixed Data Types in List:
student_info = ["Mohd", 21, "Sillvassa", True]
print("\nMixed Data Type List:", student_info)


# ==============================================================================
# 2. LIST SLICING
# Syntax: list[start : stop : step] (Stop index exclude hota hai)
# ==============================================================================
print("\n--- 2. List Slicing ---")
numbers = [10, 20, 30, 40, 50, 60]

print("Original Numbers :", numbers)
print("numbers[1:4]     :", numbers[1:4])   # Index 1, 2, 3 -> [20, 30, 40]
print("numbers[:3]      :", numbers[:3])    # Shuru se Index 2 tak -> [10, 20, 30]
print("numbers[3:]      :", numbers[3:])    # Index 3 se end tak -> [40, 50, 60]
print("Negative [-3:-1] :", numbers[-3:-1]) # [40, 50]


# ==============================================================================
# 3. LIST BUILT-IN METHODS
# - .append(val) : End mein element add karta hai
# - .sort()      : Ascending order mein sort karta hai (in-place)
# - .reverse()   : List ko ulta karta hai
# - .insert(i, v): Specific index 'i' par value 'v' insert karta hai
# - .remove(val) : Pehle aane wale matching element ko delete karta hai
# - .pop(idx)    : Given index ke element ko delete karke return karta hai
# ==============================================================================
print("\n--- 3. List Built-in Methods ---")

my_list = [2, 1, 3]
print("Initial List     :", my_list)

# (A) append()
my_list.append(4)
print("After append(4)  :", my_list)

# (B) sort() in ascending order
my_list.sort()
print("After sort()     :", my_list)

# (C) sort() in descending order
my_list.sort(reverse=True)
print("Descending sort  :", my_list)

# (D) reverse()
my_list.reverse()
print("After reverse()  :", my_list)

# (E) insert(index, value)
my_list.insert(1, 99)  # Index 1 par 99 insert karega
print("After insert(1,99):", my_list)

# (F) remove(value)
my_list.remove(99)
print("After remove(99) :", my_list)

# (G) pop(index)
popped_val = my_list.pop(0)  # Index 0 ka element nikal lega
print(f"Popped value: {popped_val} | Remaining List: {my_list}")


# ==============================================================================
# 4. TUPLES IN PYTHON (IMMUTABLE)
# Concept:
# - Tuples parenthesis `()` se bante hain.
# - Important Interview Gotcha: Single element tuple banane ke liye comma `,` zaroori hai!
#   tup = (1)   -> Python ise Integer maan lega!
#   tup = (1,)  -> Yeh valid Tuple hai.
# ==============================================================================
print("\n--- 4. Tuples Basics ---")

tup = (1, 2, 3, 4, 2, 5)
print("Tuple Content    :", tup)
print("Tuple Type       :", type(tup))

# Single element tuple:
single_wrong = (1)
single_correct = (1,)
print("Type of (1)      :", type(single_wrong))    # <class 'int'>
print("Type of (1,)     :", type(single_correct))  # <class 'tuple'>

# Immutability Demonstration:
# tup[0] = 10  # TypeError: 'tuple' object does not support item assignment


# ==============================================================================
# 5. TUPLE METHODS
# - .index(val) : Value ka pehla index return karta hai
# - .count(val) : Value tuple mein kitni baar aayi hai wo count karta hai
# ==============================================================================
print("\n--- 5. Tuple Methods ---")
print("tup.index(2)     :", tup.index(2))  # Pehli baar index 1 par mila
print("tup.count(2)     :", tup.count(2))  # Total 2 times aaya


# ==============================================================================
# 6. PRACTICE QUESTIONS
# ==============================================================================
print("\n" + "="*50)
print("PRACTICE QUESTIONS (LISTS & TUPLES)")
print("="*50)

# Q1: WAP to ask the user to enter names of their 3 favorite movies and store in a list
print("\n--- Q1: Favorite Movies List ---")
movies = []
mov1 = input("enter 1st movie name: ")
mov2 = input("enter 2nd movie name: ")
mov3 = input("enter 3rd movie name: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Favorite Movies List:", movies)


# Q2 (INTERVIEW CLASSIC): WAP to check if a list contains a PALINDROME of elements
# Palindrome: Aisa sequence jise aage ya peeche se padhein toh same ho (e.g. [1, 2, 3, 2, 1])
# Logic: List ki ek copy banate hain, use reverse karte hain, fir compare karte hain.
print("\n--- Q2: Palindrome List Check ---")
test_list = [1, 2, 3, 2, 1]

# Copy banayi taaki original list modify na ho:
copy_list = test_list.copy()
copy_list.reverse()

if copy_list == test_list:
    print(f"{test_list} is a PALINDROME List!")
else:
    print(f"{test_list} is NOT a Palindrome List.")


# Q3: WAP to count the number of students with "A" grade in following tuple:
# grades = ("C", "D", "A", "A", "B", "B", "A")
print("\n--- Q3: Count 'A' Grades in Tuple ---")
grades = ("C", "D", "A", "A", "B", "B", "A")
count_A = grades.count("A")
print("Grades Tuple     :", grades)
print("Total 'A' Grades :", count_A)


# Q4: Store the above values in a list and sort them from "A" to "D"
print("\n--- Q4: Sort Grades List Ascending ---")
grades_list = list(grades)
grades_list.sort()
print("Sorted Grades List:", grades_list)
