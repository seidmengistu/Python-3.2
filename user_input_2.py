""""
In Python, `input()` is a function used to get input from the user. When you call `input()`, the program will pause and wait for the user to type something and press Enter. The input taken is always returned as a string, so you may need to cast it to other data types if needed.

### Example of User Input in Python

1. **Basic Example**

   ```python
   name = input("Enter your name: ")
   print("Hello, " + name + "!")
   ```

   **Output:**
   ```
   Enter your name: Alice
   Hello, Alice!
   ```

2. **User Input with Type Casting**

   If you want the user to enter a number (integer or float), you can cast the input to that type since `input()` returns a string by default.

   ```python
   age = int(input("Enter your age: "))
   print("You are", age, "years old.")
   ```

   **Output:**
   ```
   Enter your age: 25
   You are 25 years old.
   ```

   > Here, `int()` is used to cast the string input into an integer. If the user enters a non-integer value, this will raise a `ValueError`.

3. **Multiple Inputs in One Line**

   You can also get multiple inputs in one line, separated by spaces, and split them into separate variables.

   ```python
   x, y = input("Enter two numbers separated by space: ").split()
   x = int(x)
   y = int(y)
   print("The sum is:", x + y)
   ```

   **Output:**
   ```
   Enter two numbers separated by space: 3 5
   The sum is: 8
   ```

   > Here, `split()` divides the input into a list of strings based on spaces, allowing you to handle multiple values.
"""

# name=input("Enter your name")
# age=input("Enter your age")
# age_int=int(age)

# if age_int < 25:
#    print("you are not eligible")
# else:
#    print("your name is: ", name,"and your age is ", age)

# x, y = input("Enter two numbers separated by space: ").split()
# x = int(x)
# y = int(y)
# print("The sum is:", x + y)

#calculate area of the triangle exercise 1

# length=float(input("Length of the triangle:"))
# width=float(input("Width of the triangle:"))

# area=length*width

# print("Area of the triangle is: ", area)

#exercice 2 Shopping cart program
item=input("what would you like to buy: ")
price=float(input("price of the item: "))
quantity=int(input("How many you want to buy: "))

total=price*quantity

print(f"you have bought {quantity} x {item}/s")
print(f"Your Total is:  ${total}")



