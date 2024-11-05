"""
    Python provides a range of arithmetic operations and
built-in math functions for various calculations. 
Here’s an overview with examples for each:
"""

### Basic Arithmetic Operations

#1. **Addition (`+`)**
 #  ```python
x = 10
y = 5
result = x + y
print(result)  # Output: 15

#2. **Subtraction (`-`)**
   #```python
x = 10
y = 5
result = x - y
print(result)  # Output: 5


#3. **Multiplication (`*`)**
   #```python
x = 10
y = 5
result = x * y
print(result)  # Output: 50


# 4. **Division (`/`)**
#    ```python
x = 10
y = 4
result = x / y
print(result)  # Output: 2.5


# 5. **Floor Division (`//`)** (returns the integer part)
#    ```python
x = 10
y = 4
result = x // y
print(result)  # Output: 2


# 6. **Modulus (`%`)** (returns the remainder)
#    ```python
x = 10
y = 4
result = x % y
print(result)  # Output: 2


# 7. **Exponentiation (`**`)**
#    ```python
x = 2
y = 3
result = x ** y
print(result)  # Output: 8


### Common Math Functions (from `math` module)

# To access more advanced math functions, we need to import the `math` module:

# ```python
import math
# ```

# 1. **Square Root (`math.sqrt()`)**
#    ```python
result = math.sqrt(16)
print(result)  # Output: 4.0
 

# 2. **Power (`math.pow()`)**
#    ```python
result = math.pow(2, 3)
print(result)  # Output: 8.0

# 3. **Absolute Value (`math.fabs()`)**
#    ```python
result = math.fabs(-10)
print(result)  # Output: 10.0
 

# 4. **Trigonometric Functions (`math.sin()`, `math.cos()`, `math.tan()`)**
#    ```python
angle = math.radians(30)  # Convert degrees to radians
result = math.sin(angle)
print(result)  # Output: 0.5


# 5. **Logarithm (`math.log()` and `math.log10()`)**
#    ```python
result = math.log(10)     # Natural log
print(result)  # Output: 2.302585092994046

result = math.log10(10)   # Base 10 log
print(result)  # Output: 1.0


# 6. **Rounding Up (`math.ceil()`) and Down (`math.floor()`)**
#    ```python
num = 5.3
result = math.ceil(num)
print(result)  # Output: 6

result = math.floor(num)
print(result)  # Output: 5


# 7. **Factorial (`math.factorial()`)**
#    ```python
result = math.factorial(5)
print(result)  # Output: 120


def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Example usage
f = math.sin  # Function to differentiate
x = math.pi / 4  # Point at which to find the derivative
approx_derivative = derivative(f, x)
print(approx_derivative)  # Output: Approximate derivative of sin(x) at x = π/4


"""
Certainly! The `math` package in Python provides foundational math functions, and while it’s not specialized for complex AI applications, it’s still highly useful for certain tasks in AI. Advanced AI often involves linear algebra, calculus, and probability, which typically requires libraries like NumPy or SciPy. However, the `math` package can support more fundamental tasks like custom function implementations, mathematical modeling, or algorithm development.

Here are some advanced uses of the `math` package that can be relevant for an AI student:

### 1. Custom Activation Functions

Activation functions are crucial in neural networks. While libraries like TensorFlow or PyTorch provide built-in activations, you can use `math` to implement custom ones.

**Example: Sigmoid Activation Function**

The sigmoid function is widely used in binary classification neural networks.

```python
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Example usage
value = 1.0
output = sigmoid(value)
print(output)  # Output: 0.7310585786300049
```

**Example: Hyperbolic Tangent Activation Function**

Another common function is the `tanh` function, which maps values to the range \([-1, 1]\).

```python
def tanh(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

# Example usage
value = 1.0
output = tanh(value)
print(output)  # Output: 0.7615941559557649
```

### 2. Calculating Cross-Entropy Loss for Classification

Cross-entropy loss is commonly used in classification tasks to measure the difference between actual and predicted probabilities. You can use `math.log` to implement it.

```python
def cross_entropy(y_true, y_pred):
    # y_true and y_pred should be lists of probabilities
    epsilon = 1e-15  # Small constant to avoid log(0)
    loss = 0
    for yt, yp in zip(y_true, y_pred):
        yp = max(epsilon, min(1 - epsilon, yp))  # Clip predictions
        loss += -yt * math.log(yp) - (1 - yt) * math.log(1 - yp)
    return loss

# Example usage
y_true = [1, 0, 1]
y_pred = [0.9, 0.1, 0.8]
loss = cross_entropy(y_true, y_pred)
print(loss)  # Output: Cross-entropy loss value
```

### 3. Distance Metrics

Distance metrics are often used in AI algorithms, like k-nearest neighbors (KNN) or clustering. You can calculate Euclidean distance or Manhattan distance with `math`.

**Example: Euclidean Distance**

The Euclidean distance between two points in an \(n\)-dimensional space is given by:
\[
\text{distance} = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}
\]

```python
def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

# Example usage
point1 = [1, 2, 3]
point2 = [4, 5, 6]
distance = euclidean_distance(point1, point2)
print(distance)  # Output: Euclidean distance
```

### 4. Gaussian Distribution (Normal Distribution)

The Gaussian or normal distribution is foundational in statistics, often used in AI for probability, modeling, and noise in data. You can create a probability density function (PDF) using `math`.

**Example: Gaussian PDF**

The Gaussian PDF formula:
\[
f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}}
\]

```python
def gaussian_pdf(x, mean, std_dev):
    return (1 / (math.sqrt(2 * math.pi * std_dev ** 2))) * math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))

# Example usage
x = 0.5
mean = 0
std_dev = 1
probability = gaussian_pdf(x, mean, std_dev)
print(probability)  # Output: Probability density at x
```

### 5. Numerical Differentiation

Calculating gradients is essential in optimization and deep learning. Using `math`, you can implement a numerical approximation for derivatives, such as with the finite difference method.

**Example: Derivative Using Central Difference**

\[
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}
\]

```python
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Example usage
f = math.sin  # Function to differentiate
x = math.pi / 4  # Point at which to find the derivative
approx_derivative = derivative(f, x)
print(approx_derivative)  # Output: Approximate derivative of sin(x) at x = π/4
```

### 6. Cosine Similarity

Cosine similarity is often used in NLP and recommendation systems to measure the similarity between two vectors.

\[
\text{cosine similarity} = \frac{\sum (A \cdot B)}{\sqrt{\sum A^2} \cdot \sqrt{\sum B^2}}
\]

```python
def cosine_similarity(vector1, vector2):
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vector1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vector2))
    return dot_product / (magnitude1 * magnitude2)

# Example usage
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
similarity = cosine_similarity(vector1, vector2)
print(similarity)  # Output: Cosine similarity
```

### 7. Sigmoid Derivative

The sigmoid derivative is used in backpropagation for updating weights in neural networks.

\[
\text{sigmoid derivative} = \sigma(x) \cdot (1 - \sigma(x))
\]

```python
def sigmoid_derivative(x):
    sig = 1 / (1 + math.exp(-x))
    return sig * (1 - sig)

# Example usage
value = 0.5
output = sigmoid_derivative(value)
print(output)  # Output: Derivative of sigmoid at x = 0.5
```

These examples demonstrate how you can use the `math` package for core functions,
distance calculations, probability functions, and gradient estimation, 
all of which can be building blocks in implementing and understanding AI algorithms at a deeper level.
"""

a=3
b=4

def pytagore_theorem(a,b):
    return math.sqrt(a**2 + b**2)

print(f'The length of the hypotenuse is {pytagore_theorem(a,b)} units.')


#Exercise 1 Area of the circle
radius =float(input("Enter the radius of the circle: "))

def calculate_area(radius):
    return math.pi * radius ** 2


print(f'The area of the circle is {round(calculate_area(radius),2)} square units.')
