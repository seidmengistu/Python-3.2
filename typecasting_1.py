""""
Type casting in Python is the process of converting one data type into another. Python provides several functions for casting, including `int()`, `float()`, `str()`, and `bool()`. Type casting is useful when you want to perform operations on data types that require them to be of a specific type.

### Examples of Type Casting in Python

1. **Integer to Float**

   ```python
   x = 5  # integer
   y = float(x)  # cast to float
   print(y)  # Output: 5.0
   ```

2. **Float to Integer**

   ```python
   x = 5.7  # float
   y = int(x)  # cast to integer (note: this truncates the decimal)
   print(y)  # Output: 5
   ```

3. **String to Integer**

   ```python
   x = "123"  # string
   y = int(x)  # cast to integer
   print(y)  # Output: 123
   ```

   > Note: The string must represent a valid integer value; otherwise, Python will throw an error.

4. **Integer to String**

   ```python
   x = 123  # integer
   y = str(x)  # cast to string
   print(y)  # Output: "123"
   ```

5. **String to Float**

   ```python
   x = "123.45"  # string
   y = float(x)  # cast to float
   print(y)  # Output: 123.45
   ```

6. **Integer to Boolean**

   ```python
   x = 1  # integer
   y = bool(x)  # cast to boolean
   print(y)  # Output: True

   x = 0
   y = bool(x)
   print(y)  # Output: False
   ```

   > In Python, any non-zero integer converts to `True`, while zero converts to `False`.

### Why Use Type Casting?

Type casting is useful when you want to work with values in specific formats, 
or when converting user input (which is often a string) into the necessary data type for calculations or other operations.
"""
x = 5  # integer
y = float(x)  # cast to float
print(y)  # Output: 5.0


x = 5.7  # float
y = int(x)  # cast to integer (note: this truncates the decimal)
print(y)  # Output: 5

x = "123"  # string
y = int(x)  # cast to integer
print(y)  # Output: 123

x=123
y=str(x)
z=y+str(x)  # to add and subtract they must be same data type
print(z)
print(f"integer to string conversion {type(y)}")  
