# ==============================================================================
# LECTURE 2: CONDITIONAL STATEMENTS (if - elif - else)
# ==============================================================================
# Concept:
# - Conditionals Python mein decision making ke liye use hote hain.
# - 'if' pehle check hota hai. Agar False ho toh agle 'elif' par jata hai.
# - Agar sabhi conditions False hon toh aakhri 'else' block execute hota hai.
# - Python mein block boundaries braces `{}` ke bajaye Indentation (4 spaces) se banti hain.
# ==============================================================================

# ==============================================================================
# 1. QUESTION: CHECK NUMBER IS EVEN OR ODD
# Logic: Kisi bhi number ko 2 se divide karne par agar remainder 0 aaye (num % 2 == 0),
# toh wo Even number hota hai, warna Odd number hota hai.
# ==============================================================================
print("--- 1. Check Even or Odd ---")
a = int(input("enter your number: "))
b = a % 2

if b == 0:
    print("Result: even")
else:
    print("Result: odd")


# ==============================================================================
# 2. QUESTION: FIND GREATEST OF THREE NUMBERS
# Logic: Comparison operators ko 'and' ke sath combine karke check karte hain
# ki kaunsa number baaki dono se bada hai.
# ==============================================================================
print("\n--- 2. Greatest Out of Three Numbers ---")
c = int(input("enter 1st number: "))
d = int(input("enter 2nd number: "))
e = int(input("enter 3rd number: "))

if c > d and c > e:
    print("Greatest number is:", c)
elif c < d and d > e:
    print("Greatest number is:", d)
else:
    print("Greatest number is:", e)


# ==============================================================================
# 3. QUESTION: FIND GREATEST OF FOUR NUMBERS
# Logic: 4 numbers (f, g, h, i) ke beech step-by-step ladder banate hain:
# - Step 1: f sabhi 3 (g, h, i) se bada hai? -> f
# - Step 2: agar nahi, toh kya g baaki dono (h, i) se bada hai? -> g
# - Step 3: agar nahi, toh kya h baaki ek (i) se bada hai? -> h
# - Step 4: warna last mein i hi sabse bada hoga -> i
# ==============================================================================
print("\n--- 3. Greatest Out of Four Numbers ---")
f = int(input("enter 1st number: "))
g = int(input("enter 2nd number: "))
h = int(input("enter 3rd number: "))
i = int(input("enter 4th number: "))

if f > g and f > h and f > i:
    print("Greatest number is:", f)
elif g > h and g > i:
    print("Greatest number is:", g)
elif h > i:
    print("Greatest number is:", h)
else:
    print("Greatest number is:", i)


# ==============================================================================
# 4. QUESTION: CHECK IF NUMBER IS A MULTIPLE OF 7
# Logic: Multiple of 7 ka matlab hai ki number 7 se poori tarah divisible ho (j % 7 == 0).
# ==============================================================================
print("\n--- 4. Check Multiple of 7 ---")
j = int(input("enter your number: "))
k = j % 7

if k == 0:
    print("Result: its multiple by 7")
else:
    print("Result: its not multiple by 7")
