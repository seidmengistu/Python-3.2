# In Python, conditions (also known as conditional statements) allow you to make decisions in your code based on certain criteria. Conditions control the flow of execution depending on whether an expression evaluates to `True` or `False`. Python supports several conditional statements, including `if`, `elif`, and `else`.

# ### 1. `if` Statement

# The `if` statement checks if a condition is `True`. If it is, the code block under the `if` statement is executed.

# **Example:**

# ```python
age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible to vote.")


# **Explanation:** Since `age` is 18, the condition `age >= 18` is `True`, so the message "You are eligible to vote." is printed.

# ### 2. `if-else` Statement

# The `if-else` statement provides an alternative path if the condition is `False`.

# **Example:**

# ```python
# age = 16

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")
# ```

# **Explanation:** Here, `age` is 16, so `age >= 18` is `False`, and the `else` block is executed, printing "You are not eligible to vote."

# ### 3. `if-elif-else` Statement

# The `if-elif-else` statement allows for multiple conditions to be checked sequentially. If the first condition is `False`, it checks the `elif` condition, and so on. If all conditions are `False`, the `else` block is executed.

# **Example:**

# ```python
# score = 85

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# else:
#     print("Grade: D")
# ```

# **Explanation:** Here, `score` is 85, so the first `if` condition is `False`. The second `elif` condition (`score >= 80`) is `True`, so "Grade: B" is printed. The rest of the conditions are not checked once a `True` condition is found.

# ### 4. Nested Conditions

# You can also nest `if` statements inside one another to create more complex conditions.

# **Example:**

# ```python
age = 20
is_student = True

if age >= 18:
    if is_student:
        print("You are an adult student.")
    else:
        print("You are an adult non-student.")
else:
    print("You are a minor.")


# **Explanation:** Here, the outer `if` checks if `age` is 18 or more. Since it is, the inner `if` checks if the person is a student (`is_student`). Because both conditions are `True`, "You are an adult student." is printed.

# ### 5. Using Logical Operators

# Python provides logical operators (`and`, `or`, `not`) to combine multiple conditions.

# - `and`: Both conditions must be `True`.
# - `or`: At least one condition must be `True`.
# - `not`: Inverts the Boolean value.

# **Example:**

# ```python
age = 25
has_permission = True

if age >= 18 and has_permission:
    print("Access granted.")
else:
    print("Access denied.")
# ```

# **Explanation:** Both `age >= 18` and `has_permission` are `True`, so "Access granted." is printed. If either of these conditions was `False`, "Access denied." would be printed.

# ### Summary

# | Statement         | Description                                  |
# |-------------------|----------------------------------------------|
# | `if`             | Executes if the condition is `True`          |
# | `if-else`        | Provides an alternative path if `False`      |
# | `if-elif-else`   | Allows for multiple conditions               |
# | Nested `if`      | Allows for checking conditions within other conditions |
# | Logical Operators| Combines multiple conditions (`and`, `or`, `not`) |

# Conditional statements are foundational in Python programming, allowing for decision-making and controlling the flow of the code based on different conditions.

name=input("Enter your name: ")

if name == " ":
    print("Name cannot be empty.")
else:
    print(f"Hello , {name}!")
    
    #python calculator
    

number1=float(input("Enter your first number: "))
number2=float(input("Enter your second number: "))

operation=input("Enter your operation (+,-,*,/): ")

if operation == "+":
    print(f"{number1} + {number2} = {number1 + number2}")
elif operation == "-":
    print(f"{number1} - {number2} = {number1 - number2}")
elif operation == "*":
    print(f"{number1} * {number2} = {number1 * number2}")
elif operation == "/":
    if number2!= 0:
        print(f"{number1} / {number2} = {number1 / number2}")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")
    
    
    
# weight calculator


weight=float(input("Enter your weight: "))
unit=input("Kilograms or pounds(K Or L): ")

if unit == "K":
    weight=weight * 2.20462
    unit="Lbs"    
elif unit == "L":
    weight=weight / 2.20462
    unit="Kgs"
    

print(f"Your weight in {unit} is {weight}")
           
       
       
# Temoertaure calculator

Temperature = float(input("Enter your temperature: "))
unit = input("Celsius or Fahrenheit(C Or F): ")

if unit=="C":
    Temperature= (Temperature * 9/5) + 32
    unit="Fahrenheit"
elif unit=="F":
    Temperature= (Temperature - 32) * 5/9
    unit="Celsius"
else:
    print("Invalid unit.")
    
print(f"Your temperature in {unit} is {round(Temperature,1)}")
        
    