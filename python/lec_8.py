# ==============================================================================
# LECTURE 8: OBJECT ORIENTED PROGRAMMING (OOPs) IN PYTHON
# ==============================================================================
# Concepts:
# 1. Class     : Ek blueprint ya template hota hai jisme properties aur methods define hote hain.
# 2. Object    : Us class ka real-world instance hota hai jo memory occupy karta hai.
# 3. self      : Current object instance ka reference hota hai (har instance method mein pehla parameter).
# 4. __init__  : Constructor method jo naya object bante hi automatically execute hota hai.
# 5. Pillars   :
#    - Abstraction   : Internal complex implementation ko chhupana aur sirf zaroori features dikhana.
#    - Encapsulation : Data aur methods ko ek capsule mein band karna, private attributes (__attr) banana.
# ==============================================================================


# ==============================================================================
# 1. BASIC CLASS & OBJECT CREATION
# ==============================================================================
print("--- 1. Basic Class & Object Creation ---")

class Student:
    name = "mohd"

# Object instantiate karna
s1 = Student()
print("Student Object Name:", s1.name)

# Example 2: Books class
class Book:
    quran = "para1"
    Hayatusssahaba = "baab1"

bname = Book()
print("Book 1:", bname.quran)
print("Book 2:", bname.Hayatusssahaba)


# ==============================================================================
# 2. THE __init__ CONSTRUCTOR & self KEYWORD
# Concept:
# - __init__(self, ...) object initialization ke waqt chalta hai.
# - 'self' batata hai ki kaunsa object apna data store ya access kar raha hai.
# ==============================================================================
print("\n--- 2. Constructor (__init__) & self ---")

class Talaba:
    name = "yousuf"
    def __init__(self):
        print("Constructor called for object:", self)
        print("Ahlan wa Sahlan Marhaba!")

t1 = Talaba()

# Parameterized Constructor: Har object ko alag data pass karna
class Students:
    def __init__(self, fullname, address):
        self.name = fullname
        self.address = address

s1_student = Students("yasir", "dudh talai")
print(f"Student 1: Name = {s1_student.name}, Address = {s1_student.address}")

s2_student = Students("ammar", "dudh talai")
print(f"Student 2: Name = {s2_student.name}, Address = {s2_student.address}")


# ==============================================================================
# 3. CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# - Class Attribute    : Poori class ke sabhi objects ke liye common/shared hota hai (e.g. Mname).
# - Instance Attribute : Har object ka apna personal unique data hota hai (e.g. self.name).
# ==============================================================================
print("\n--- 3. Class Attributes vs Instance Attributes ---")

class Madarsa:
    Mname = "gada"  # Class Attribute (Shared)

    def __init__(self, student_name):
        self.name = student_name  # Instance Attribute (Unique)

m1 = Madarsa("mohd")
print("Class Attribute (Madarsa.Mname) :", Madarsa.Mname)
print("Instance Attribute (m1.name)     :", m1.name)


# ==============================================================================
# 4. INSTANCE METHODS
# Concept: Functions jo class ke andar define hote hain aur object ke data par kaam karte hain.
# ==============================================================================
print("\n--- 4. Instance Methods ---")

class Car:
    name = "BMW"  # Class Attribute

    def __init__(self, driver_name, age):
        self.driver_name = driver_name
        self.age = int(age)

    def drive(self):
        print(f"{self.driver_name} is driving.")

    def show_age(self):
        print(f"He is {self.age} years old.")

    def car_name(self):
        print(f"Driving car model: {self.__class__.name}")

d = Car("rihan", 21)
d.drive()
d.show_age()
d.car_name()


# ==============================================================================
# 5. PRACTICE EXAMPLE: STUDENT MARKS & AVERAGE
# ==============================================================================
print("\n--- 5. Student Marks & Average Calculation ---")

class StudentClass:
    def __init__(self, name, eng_marks, math_marks, sci_marks):
        self.name = name
        self.eng_marks = eng_marks
        self.math_marks = math_marks
        self.sci_marks = sci_marks

    def get_average(self):
        return (self.eng_marks + self.math_marks + self.sci_marks) / 3

d1 = StudentClass("Mohd Ali", 85, 90, 80)
print(f"Student: {d1.name}")
print(f"English: {d1.eng_marks}, Maths: {d1.math_marks}, Science: {d1.sci_marks}")
print(f"Average Marks: {d1.get_average():.2f}")


# ==============================================================================
# 6. STATIC METHODS (@staticmethod)
# Concept:
# - Static methods class ya object ke data ko access nahi karte (inme 'self' ki zaroorat nahi hoti).
# - Yeh general utility functions banane ke kaam aate hain.
# ==============================================================================
print("\n--- 6. Static Methods ---")

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        return "Cannot divide by zero"

print("Calculator.add(10, 5)      :", Calculator.add(10, 5))
print("Calculator.multiply(4, 3)  :", Calculator.multiply(4, 3))


# ==============================================================================
# 7. ABSTRACTION (Hiding Internal Complexity)
# Concept: User ko sirf zaroori controls (jaise start button) dikhana,
# andar ke internal working (clutch, fuel injection) ko hide karna.
# ==============================================================================
print("\n--- 7. Abstraction Demonstration ---")

class Truck:
    def __init__(self):
        self.accelerate = False
        self.brake = False

    def start(self):
        # Internal operations user se abstracted (hidden) hain
        self.accelerate = True
        self.brake = True
        print("Truck started successfully (Internal systems active)!")

t = Truck()
t.start()


# ==============================================================================
# 8. ENCAPSULATION & PRIVATE ATTRIBUTES (Bank Account System)
# Concept:
# - Data aur methods ko secure tareeqe se ek class mein wrap karna.
# - Private attribute banane ke liye do underscores lagate hain (e.g., self.__balance).
# - Private variable ko class ke bahar direct access ya manipulate nahi kiya ja sakta.
# ==============================================================================
print("\n--- 8. Encapsulation (Bank Account System) ---")

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute (Cannot be accessed outside directly)

    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Credited: Rs. {amount} | New Balance: Rs. {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def debit(self, amount):
        if amount > self.__balance:
            print(f"Insufficient funds! Current Balance: Rs. {self.__balance}")
        elif amount > 0:
            self.__balance -= amount
            print(f"Debited: Rs. {amount} | Remaining Balance: Rs. {self.__balance}")

    def get_balance(self):
        return self.__balance

# Bank Account Test Run
acc1 = BankAccount("Mohd", 1000)
print(f"Account created for {acc1.account_holder} with Initial Balance: Rs. {acc1.get_balance()}")

credit_amt = int(input("Enter amount to credit: "))
acc1.credit(credit_amt)

debit_amt = int(input("Enter amount to debit: "))
acc1.debit(debit_amt)
