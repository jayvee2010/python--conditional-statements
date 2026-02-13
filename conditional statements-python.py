## Experiment- 6 EDA- DATE- 30/01/2026
## Name : Jayvee Shah
## PRN : 25070123058
## Batch : EnTC A3
## Title: Study of conditional statements in Python

# 1a. Check whether a number is positive or negative
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")

# 1b. Check whether a number is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2. Check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Find the greater number between two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

# 4. Find the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print("Largest number is:", largest)

# 5. Get input for 5 subjects, find average and calculate grade
marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))
marks4 = int(input("Enter marks 4: "))
marks5 = int(input("Enter marks 5: "))
avg = (marks1 + marks2 + marks3 + marks4 + marks5) / 5
print("Average =", avg)
if avg >= 90:
    print("Grade A")
elif avg >= 75:
    print("Grade B")
elif avg >= 60:
    print("Grade C")
elif avg >= 40:
    print("Grade D")
else:
    print("Fail")

# 6. Check whether a year is a leap year
y = int(input("Enter year: "))
print("Leap Year" if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else "Not a Leap Year")

# 7. Check if a Date is valid and print the Incremented Date
x = input("Enter day/month/year: ").split("/")
d, m, y = int(x[0]), int(x[1]), int(x[2])

leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

if m in [1, 3, 5, 7, 8, 10, 12]:
    max_d = 31
elif m in [4, 6, 9, 11]:
    max_d = 30
elif m == 2:
    max_d = 29 if leap else 28
else:
    max_d = 0

if 1 <= d <= max_d:
    print("Valid date")
    d += 1
    if d > max_d:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    print(f"Next date: {d}/{m}/{y}")
else:
    print("Invalid date")

# 8. Salary Calculation with Allowances
basic = int(input("Enter your basic Salary: "))
if basic <= 10000:
    hra = basic * 0.20
    da = basic * 0.80
elif basic <= 20000:
    hra = basic * 0.25
    da = basic * 0.90
else:
    hra = basic * 0.30
    da = basic * 0.95
salary = basic + hra + da
print("Your final salary is:", salary)

# 9. Tax calculation on the basis of income
income = float(input("Enter your annual income (in INR): "))
tax = 0.0
if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10
elif income <= 1200000:
    tax = 45000 + (income - 900000) * 0.15
elif income <= 1500000:
    tax = 90000 + (income - 1200000) * 0.20
else:
    tax = 150000 + (income - 1500000) * 0.30
print(f"Your Income is ₹{income:,.2f}, the calculated tax is ₹{tax:,.2f}.")
