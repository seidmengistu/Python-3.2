# # Python provides two primary types of loops: `for` loops and `while` loops. Both are essential in AI for data processing, batch processing, and iterative algorithm implementation, such as in training neural networks or implementing machine learning algorithms. Here, we’ll explore each type of loop with advanced examples in the AI field.

# # ### 1. `for` Loop

# # A `for` loop iterates over a sequence (like a list, tuple, string, or range) and executes the code block for each element in that sequence. 

# # #### Basic Example
# # ```python
# for i in range(5):
#     print(i)
# # ```

# # **Output:** `0 1 2 3 4`

# # ### Advanced Examples of `for` Loops in AI

# # #### Example 1: Iterating Through Data Batches
# # In machine learning, data is often processed in batches. A `for` loop can iterate over these batches for training.

# # ```python
# # # Assume data is split into batches
# data_batches = [[0.5, 0.7], [0.3, 0.4], [0.9, 0.6]]

# for batch in data_batches:
#     # Simulate processing each batch
#     print("Processing batch:", batch)
# # ```

# # **Explanation:** Here, each batch is processed individually, which is common in neural network training where data is fed in small batches.

# # #### Example 2: Implementing Stochastic Gradient Descent (SGD)
# # A common optimization algorithm in training AI models is stochastic gradient descent, which iterates through data points to update model weights.

# # ```python
# data_points = [0.5, 0.6, 0.1, 0.4]  # Example data points
# learning_rate = 0.01
# weight = 0.5  # Initial weight

# for point in data_points:
#     gradient = 2 * (weight * point - point)  # Simple gradient computation
#     weight = weight - learning_rate * gradient  # Update weight

# print("Final weight:", weight)
# # ```

# # **Explanation:** Each iteration represents an update step based on one data point, emulating the SGD process in model training.

# # ### 2. `while` Loop

# # A `while` loop continues to execute as long as its condition remains `True`. This is useful for indefinite loops, where the number of iterations is not known in advance.

# # #### Basic Example
# # ```python
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# # ```

# # **Output:** `0 1 2 3 4`

# # ### Advanced Examples of `while` Loops in AI

# # #### Example 1: Training Until Convergence
# # In machine learning, some algorithms (like k-means clustering) are trained until the results stabilize (or "converge").

# # ```python
# import random

# centroids = [random.random() for _ in range(3)]  # Initialize centroids
# data_points = [0.1, 0.3, 0.4, 0.7, 0.8, 0.9]
# converged = False

# while not converged:
#     new_centroids = [random.random() for _ in range(3)]  # Simulate centroid update
#     if new_centroids == centroids:  # Check if centroids have converged
#         converged = True
#     else:
#         centroids = new_centroids  # Update centroids

# print("Converged centroids:", centroids)
# # ```

# # **Explanation:** The `while` loop continues until the centroids stabilize, simulating the convergence process in clustering algorithms.

# # #### Example 2: Early Stopping in Model Training
# # In training machine learning models, a `while` loop can be used to implement early stopping, where training stops when the model performance no longer improves.

# # ```python
# current_loss = 0.4  # Initial loss
# min_loss = current_loss
# patience = 3
# no_improvement_count = 0

# while no_improvement_count < patience:
#     # Simulate loss update (for demonstration, we're using random values)
#     new_loss = current_loss - random.uniform(0, 0.05)
#     if new_loss < min_loss:
#         min_loss = new_loss
#         no_improvement_count = 0  # Reset counter if there's improvement
#     else:
#         no_improvement_count += 1  # Increment if no improvement

#     current_loss = new_loss

# print("Training stopped with minimum loss:", min_loss)
# # ```

# # **Explanation:** The loop stops if there is no improvement in loss for a set number of iterations, mimicking early stopping in model training.

# # ### 3. Nested Loops

# # Nested loops (a loop inside another loop) are often used in matrix operations or multi-dimensional data processing, both of which are common in AI.

# # #### Example 1: Calculating Cosine Similarity Between Document Vectors
# # Cosine similarity is frequently used in NLP for comparing document vectors.

# # ```python
import math

documents = [[0.1, 0.2, 0.3], [0.3, 0.5, 0.7], [0.2, 0.8, 0.4]]

for i in range(len(documents)):
    for j in range(i + 1, len(documents)):
        dot_product = sum(a * b for a, b in zip(documents[i], documents[j]))
        norm_i = math.sqrt(sum(a ** 2 for a in documents[i]))
        norm_j = math.sqrt(sum(b ** 2 for b in documents[j]))
        cosine_similarity = dot_product / (norm_i * norm_j)
        print(f"Cosine similarity between doc {i} and doc {j}: {cosine_similarity}")
# # ```

# # **Explanation:** The nested loop allows us to calculate the cosine similarity between each pair of document vectors, which is useful in information retrieval and NLP tasks.

# # #### Example 2: Building a Confusion Matrix
# # A confusion matrix is used to evaluate classification models by showing the counts of true positive, false positive, true negative, and false negative results.

# # ```python
# # Predicted and actual labels
# # predicted = [0, 1, 1, 0, 1, 1, 0, 0]
# # actual = [0, 1, 0, 0, 1, 0, 1, 1]

# # # Initialize confusion matrix
# # confusion_matrix = [[0, 0], [0, 0]]

# # for p, a in zip(predicted, actual):
# #     confusion_matrix[a][p] += 1

# # print("Confusion Matrix:")
# # for row in confusion_matrix:
# #     print(row)
# # ```

# # **Explanation:** The nested list structure of the confusion matrix allows us to increment counts based on predicted and actual labels, useful in model evaluation.

# # ### Summary

# # | Loop Type       | Description                         | Example Use Case in AI                                             |
# # |-----------------|-------------------------------------|---------------------------------------------------------------------|
# # | `for` loop      | Iterates over sequences             | Data batch processing, stochastic gradient descent                 |
# # | `while` loop    | Runs as long as condition is `True` | Convergence detection in clustering, early stopping in training    |
# # | Nested loop     | Loops within loops                  | Cosine similarity calculation, confusion matrix construction       |
# break and continues 
# # These loop structures provide a foundation for processing data, training models, and building metrics, all of which are key steps in AI workflows.

import time

my_time=int(input("Enter the time in Seconds: "))

for i in range(my_time,0,-1 ):
    seconds=i % 60
    minutes=int(i /60) % 60
    hours=int(i /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)