# ==============================================================================
# LECTURE 4: DICTIONARIES & SETS IN PYTHON
# ==============================================================================

# ==============================================================================
# 1. DICTIONARIES (Key - Value Pairs)
# Concept:
# - Dictionaries unordered, mutable (changeable) aur indexed collection hoti hain.
# - Duplicate keys allowed nahi hoti; har key unique honi chahiye.
# - Values kisi bhi data type (int, str, list, tuple, ya nested dict) ki ho sakti hain.
# ==============================================================================
print("--- 1. Dictionary Creation & Nested Access ---")
info = {
    "name": "mohd hanzla",
    "age": 7,
    "school name": "indian publuc school",
    "class": 1,
    "marks": {
        'english': 57,
        'hindi': 60,
        'maths': 55,
        'sci': {
            'phy': 25,
            'chm': 24,
            'bio': 26,
        },
        'ss': {
            'geo': 24,
            'hist': 25,
            'civi': 23,
        },
        'gujrati': 57,
    },
    "fav subjects": ["maths", "science", "ss"],   # List as a value
    "fav games": ("subway sufer", "tample run"),   # Tuple as a value
}

print("Full Info Dict :", info)
print("Structure Type :", type(info))
# Nested access: marks -> ss -> civi
print("Civics Marks   :", info["marks"]["ss"]["civi"])


# ==============================================================================
# 2. DICTIONARY BUILT-IN METHODS
# ==============================================================================
print("\n--- 2. Dictionary Methods ---")

# (A) dict.keys() -> Saari keys return karta hai
print("info.keys()           :", info.keys())
print("Keys as List          :", list(info.keys()))
print("Total Keys Count      :", len(list(info.keys())))

# (B) dict.values() -> Saari values return karta hai
print("\ninfo.values()         :", info.values())
print("Values as List        :", list(info.values()))
print("Total Values Count    :", len(list(info.values())))

# (C) dict.items() -> (key, value) pairs tuples ke form mein return karta hai
print("\ninfo.items()          :", info.items())
pairs = list(info.items())
print("First Pair (Index 0)  :", pairs[0])
print("Seventh Pair (Index 6):", pairs[6])

# (D) dict["key"] vs dict.get("key") -> Crucial Interview Difference!
# - info["name"]      : Value return karta hai, lekin agar key na mile toh KeyError deta hai aur program crash hota hai.
# - info.get("name")  : Safe access karta hai. Agar key na mile toh None return karta hai (crash nahi hota).
print("\ninfo['name']          :", info["name"])
print("info.get('name')      :", info.get("name"))
print("info.get('name2')     :", info.get("name2")) # Key exist nahi karti -> safely returns None

# (E) dict.update() -> Naye key-value pairs add ya existing ko modify karna
info.update({"fav places": "khandwa"})
print("\nAfter update()        :", info["fav places"])


# ==============================================================================
# 3. SETS IN PYTHON
# Concept:
# - Sets unordered collection of UNIQUE elements hote hain.
# - Duplicate values automatically discard (remove) ho jaati hain.
# - Sets mutable hote hain, lekin unke andar ke elements immutable hone chahiye (strings, numbers, tuples). Lists aur dicts set ke andar nahi aa sakte!
# ==============================================================================
print("\n--- 3. Sets Basics ---")
collection = {1, 2, 3, 4}
print("Set Content           :", collection)
print("Type                  :", type(collection))

# Duplicates automatically drop ho jaate hain:
collection1 = {"hello", "hello", "world", 1, 2, 2, 3, 3, 4, 5}
print("Duplicates Dropped    :", collection1)
print("Length (Unique Count) :", len(collection1))

# Empty set banane ka syntax:
# Note: `{}` empty dictionary banata hai. Empty set ke liye `set()` use karte hain.
collection3 = set()
print("Empty Set Type        :", type(collection3))


# ==============================================================================
# 4. SET METHODS (.add, .remove, .clear, .pop, .union, .intersection)
# ==============================================================================
print("\n--- 4. Set Methods ---")

# (A) set.add() -> Element add karna
collection3.add(1)
collection3.add(2)
collection3.add(2)  # Duplicate ignore ho jayega
collection3.add(("hellow", "world"))  # Tuple immutable hai, isliye set mein add ho sakta hai
collection3.add("hellow")
print("After add()           :", collection3)

# (B) set.remove() -> Specific element delete karna
collection3.remove(1)
collection3.remove("hellow")
print("After remove()        :", collection3)

# (C) set.clear() -> Saare elements delete karna
collection3.clear()
print("After clear()         :", collection3, "| Length:", len(collection3))

# (D) set.pop() -> Unordered set se koi bhi random element nikal kar return karta hai
print("\nPopped from collection:", collection.pop())
print("Popped from collection:", collection.pop())

# (E) set.union() -> Do sets ko jodta hai (Duplicates remove karke naya set banata hai)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print("\nset1.union(set2)      :", set3) # {1, 2, 3, 4, 5}

# (F) set.intersection() -> Sirf dono sets ke common elements return karta hai
print("set1.intersection(set2):", set1.intersection(set2)) # {3}


# ==============================================================================
# 5. PRACTICE QUESTIONS
# ==============================================================================
print("\n" + "="*50)
print("PRACTICE QUESTIONS (DICTIONARIES & SETS)")
print("="*50)

# Q1: Store word meanings in a dictionary (single key with multiple meanings in a list)
print("\n--- Q1: Word Meanings Dictionary ---")
dict1 = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts and figures"]
}
print(dict1)

# Q2: Calculate classrooms needed for given subjects using unique sets
print("\n--- Q2: Unique Classrooms for Subjects ---")
# Agar subjects list mein repeat ho rahe hain, toh set mein convert karke unique count mil jata hai:
subjects_set = {"java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print("Unique Subjects:", subjects_set)
print("Total Classrooms Needed:", len(subjects_set))

# Q3: WAP to enter marks of 3 subjects from user and store in empty dict
print("\n--- Q3: Enter Marks in Empty Dictionary ---")
dictionary = {}
eng = int(input("enter english marks: "))
math = int(input("enter maths marks: "))
sci = int(input("enter science marks: "))

dictionary.update({"english": eng})
dictionary.update({"maths": math})
dictionary.update({"science": sci})
print("Resulting Dictionary:", dictionary)

# Q4: Figure out a way to store 9 and 9.0 as separate values in a set
print("\n--- Q4: Store 9 and 9.0 as Separate Values in Set ---")
# Approach 1: Ek value ko string banana kyunki Python set 9 == 9.0 ko numerically equal manta hai
values1 = {9, "9.0"}
print("Approach 1 (int + str):", values1)

# Approach 2: Dono ko individual sets bana kar tuple form mein rakhna
value2 = ({9}, {9.0})
print("Approach 2 (tuple of sets):", value2)
