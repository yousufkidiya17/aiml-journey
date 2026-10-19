# ==============================================================================
# LECTURE 7: FILE INPUT / OUTPUT (FILE I/O) IN PYTHON
# ==============================================================================
# Concept:
# - File I/O ka use external files (.txt, .csv, etc.) se data read ya write karne ke liye hota hai.
# - Modes:
#   'r'  : Read only (File pehle se exist honi chahiye, warna FileNotFoundError aayega).
#   'w'  : Write only (Purana data overwrite / wipe out kar deta hai; naye file create karta hai).
#   'a'  : Append (File ke aakhri mein naya data add karta hai bina purana data delete kiye).
#   'r+' : Read + Write (Stream shuruat par hoti hai, bina truncate kiye write karta hai).
#   'w+' : Write + Read (Purana data pehle truncate karta hai, fir write/read karta hai).
#   'a+' : Append + Read (End mein append karta hai aur read karta hai).
# ==============================================================================
import os

# ==============================================================================
# 1. TRADITIONAL WAY (open -> operation -> close)
# Problem: Agar code crash ho jaye toh file open reh sakti hai, isliye f.close() zaroori hai.
# ==============================================================================
print("--- 1. Traditional File Handling ---")

# File create & write
f = open("sample.txt", "w")
f.write("Hello, I am learning Python File I/O.")
f.close()  # Resource release karna zaroori hai

# File read
f = open("sample.txt", "r")
content = f.read()
print("Read Content:", content)
f.close()


# ==============================================================================
# 2. MODERN / BEST PRACTICE WAY (`with open()` Context Manager)
# Advantage: 'with' block khatam hote hi Python automatically file ko close kar deta hai.
# ==============================================================================
print("\n--- 2. Modern with open() Syntax ---")

# (A) Read using with block
with open("sample.txt", "r") as f:
    data = f.read()
    print("Read via 'with' block:", data)

# (B) Overwrite using with block
with open("sample.txt", "w") as f:
    f.write("New updated data via context manager.")

# (C) Delete file using os.remove()
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("sample.txt successfully deleted!")


# ==============================================================================
# 3. PRACTICE QUESTIONS
# ==============================================================================
print("\n" + "="*50)
print("FILE I/O PRACTICE QUESTIONS")
print("="*50)

# Q1: Create a new file "practice.txt" and write sample text into it
print("\n--- Q1: Create & Write practice.txt ---")
with open("practice.txt", "w") as new_file:
    new_file.write("Hii everyone.\nwe are learning file i/o using python.\ni like programming in python.")
print("practice.txt created successfully!")

# Q2: WAP to replace the word "python" with "java"
print("\n--- Q2: Word Replacement (python -> java) ---")
with open("practice.txt", "r") as nf:
    raw_text = nf.read()

# .replace() se word badal kar naya text create karte hain
updated_text = raw_text.replace("python", "java")
print("Updated Text Preview:\n", updated_text)

# Q3: Search if a word exists in the file or not
print("\n--- Q3: Word Existence Search ---")
search_word = input("enter a word to search: ")
with open("practice.txt", "r") as f1:
    file_content = f1.read()
    if search_word.lower() in file_content.lower():
        print(f"Result: '{search_word}' was FOUND in practice.txt")
    else:
        print(f"Result: '{search_word}' was NOT FOUND in practice.txt")

# Q4: Find the line number where a word exists
print("\n--- Q4: Line Number Search Function ---")
def find_word_line():
    target = input("enter word to find line number: ")
    line_number = 1
    found_line = False

    with open("practice.txt", "r") as f:
        while True:
            line_data = f.readline()
            if not line_data:  # End of file reached
                break
            if target.lower() in line_data.lower():
                print(f"Word '{target}' found in LINE: {line_number}")
                found_line = True
            line_number += 1

    if not found_line:
        print(f"Word '{target}' not present in any line.")

find_word_line()

# Q5: Count even numbers from a comma-separated numbers file
print("\n--- Q5: Parse Comma-separated Numbers & Count Evens ---")
# Temporary test numbers file create karte hain
with open("numbers_demo.txt", "w") as demo_file:
    demo_file.write("1, 2, 45, 84, 92, 17, 33, 50")

with open("numbers_demo.txt", "r") as demo:
    data = demo.read()
    even_count = 0
    numbers_list = data.split(",")
    print("Found Numbers:", numbers_list)

    print("Even Numbers:", end=" ")
    for n in numbers_list:
        clean_num = int(n.strip())
        if clean_num % 2 == 0:
            print(clean_num, end=" ")
            even_count += 1
    print(f"\nTotal Even Numbers Count: {even_count}")

# Cleanup temporary numbers file
if os.path.exists("numbers_demo.txt"):
    os.remove("numbers_demo.txt")
