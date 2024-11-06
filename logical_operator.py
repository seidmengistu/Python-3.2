# In Python, logical operators are used to combine conditional statements and perform more complex checks. 
# Python has three logical operators: `and`, `or`, and `not`.

# ### Logical Operators in Python

# 1. **`and` Operator**  
#    - Returns `True` if both conditions are `True`. If any condition is `False`, it returns `False`.
   
#    ```python
#    # Basic example
a = 5
b = 10
print(a > 0 and b > 0)  # Output: True (both conditions are True)
#    ```

# 2. **`or` Operator**  
#    - Returns `True` if at least one of the conditions is `True`. Only returns `False` if both conditions are `False`.

#    ```python
#    # Basic example
#    a = 5
#    b = -10
#    print(a > 0 or b > 0)  # Output: True (only the first condition is True)
#    ```

# 3. **`not` Operator**  
#    - Reverses the Boolean value. If a condition is `True`, it becomes `False`, and vice versa.

#    ```python
#    # Basic example
#    a = 5
#    print(not a > 0)  # Output: False (since a > 0 is True, not True is False)
#    ```

# ### Advanced Examples with Logical Operators

# #### 1. **Using `and` and `or` in Complex Conditions**

# In a scenario where you need to check multiple conditions, you can use `and` and `or` together.

# ```python
age = 20
income = 40000
is_student = True

# Check if a person is eligible for a loan based on age and income
if (age >= 18 and income >= 30000) or (is_student and age >= 18):
    print("Eligible for a loan")
else:
    print("Not eligible for a loan")
# ```

# **Explanation:** Here, the person is eligible for a loan if they are an adult with sufficient income or if they are a student over 18. The condition `age >= 18 and income >= 30000` or `(is_student and age >= 18)` combines the conditions logically.

# #### 2. **Using `not` for Inverse Conditions**

# The `not` operator can be handy when you want to run code only if a condition is `False`.

# ```python
# is_admin = False
# is_user_logged_in = True

# # Restrict access if the user is not an admin and is not logged in
# if not is_admin and is_user_logged_in:
#     print("Access limited")
# else:
#     print("Full access granted")
# ```

# **Explanation:** Here, the `not` operator inverts `is_admin`, meaning the message "Access limited" is displayed because the user is not an admin, even though they are logged in.

# #### 3. **Checking Multiple Ranges**

# Logical operators are useful when working with numeric ranges.

# ```python
# temperature = 22

# # Check if temperature is in a comfortable range (between 20 and 25)
# if temperature >= 20 and temperature <= 25:
#     print("The temperature is comfortable.")
# else:
#     print("The temperature is uncomfortable.")
# ```

# **Explanation:** This example uses `and` to check if the temperature is within a specific range.

# #### 4. **Combining Multiple Conditions with Nested Logical Operators**

# You can use nested logical operators to combine multiple checks.

# ```python
# age = 30
# experience = 5
# has_degree = True

# # Check if a candidate is eligible for a senior position
# if (age > 25 and experience >= 5) or (has_degree and experience >= 3):
#     print("Eligible for senior position")
# else:
#     print("Not eligible for senior position")
# ```

# **Explanation:** In this example, the candidate is eligible for a senior position if they have experience and meet either the age or degree requirements. The use of nested conditions allows for more nuanced criteria.

# #### 5. **Using Logical Operators in List Filtering**

# Logical operators can also be used in list comprehensions for filtering data.

# ```python
# # List of ages
# ages = [15, 20, 25, 30, 35, 40]

# # Filter ages to find people who are either teenagers or adults over 30
# filtered_ages = [age for age in ages if (age >= 13 and age <= 19) or age > 30]
# print(filtered_ages)  # Output: [15, 35, 40]
# ```

# **Explanation:** Here, the list comprehension filters ages that are either within the teenage range or above 30. The logical operators `and` and `or` are used to construct the filter condition.

# #### 6. **Using Logical Operators in Function Parameters**

# Logical operators can also be used in functions to make checks on multiple parameters.

# ```python
# def is_eligible_for_discount(is_member, total_purchase):
#     # Customer is eligible for discount if they are a member or have a large purchase
#     return is_member or total_purchase >= 100

# print(is_eligible_for_discount(True, 50))    # Output: True
# print(is_eligible_for_discount(False, 150))  # Output: True
# print(is_eligible_for_discount(False, 50))   # Output: False
# ```

# **Explanation:** Here, the function checks if a customer is eligible for a discount. If they are either a member or their purchase amount is over 100, the function returns `True`.

# These examples demonstrate the flexibility of logical operators in building complex conditional expressions for various scenarios in Python.

def is_eligible_for_vote(country,age):
    
    # Check if a person is eligible to vote based on their country and age
    if country == "USA" and age >= 18:
       return  "Eligble to vote"
    elif country == "Ethiopia" and age >=28:
     return  "Eligble to vote"  
    elif country=="South Korea" and age>=90:
      return  "Eligble to vote" 
    else:
       return  "Not Eligible to vote"
      
country=input("Enter Your Country: ")
age=int(input("Enter Your Age: "))
    
print(is_eligible_for_vote(country,age))
 
#  Conditions

# X IF conditin else false Like Ternary OPerator

num=8
user_role="Guest"

print ("even" if num%2==0 else "odd")

print("Full Acess" if user_role=="Administrator" else " Limted Acess")

