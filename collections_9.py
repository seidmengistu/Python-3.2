# In Python, collections are data structures that allow you to store and manipulate groups of related elements.
# The built-in collections include lists, tuples, sets, and dictionaries, each with unique properties and use cases.
# These data structures are foundational in AI, especially for handling datasets, processing batches of data, and
# managing model configurations. Python also offers specialized collections in the `collections` module,
# such as `Counter`, `defaultdict`, and `deque`.

# Let’s go through each collection type with explanations and advanced examples in the In Python, 
# collections are data structures that allow you to store and manipulate groups of related elements. 
# The built-in collections include lists, tuples, sets, and dictionaries, each with unique properties and use cases.
# These data structures are foundational in AI, especially for handling datasets, processing batches of data, and managing 
# model configurations. Python also offers specialized collections in the `collections` module, such as `Counter`, `defaultdict`, and
# `deque`.

# Let’s go through each collection type with explanations and advanced examples in the AI field.

# ---

# ### 1. **List**

# A `list` is an ordered, mutable collection that allows duplicate elements.
# Lists are commonly used in AI for storing datasets, managing data batches, and keeping track of model predictions.

# #### Basic Example
# ```python
numbers = [1, 2, 3, 4, 5]

numbers[0] = 4  #mutable collection
print(numbers)

# ```

# #### Advanced Example: Storing and Managing Batches of Data
# In machine learning, data is often processed in batches to make training more efficient. A `list` can be used to store these batches.

# ```python
# # Sample data
data = [0.5, 0.6, 0.8, 0.9, 0.2, 0.3, 0.4, 0.7]

# Split data into batches of size 3
batch_size = 2
batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

# print(batches)


# Process each batch
for batch in batches:
    print("Processing batch:", batch)


# ```

# **Explanation:** This code divides the `data` list into smaller batches of size 3, 
# which is a common preprocessing step in machine learning training pipelines.

# ---

# ### 2. **Tuple**

# A `tuple` is an ordered, immutable collection that allows duplicate elements.
# Tuples are often used in AI to represent fixed sets of data, such as model hyperparameters, 
# coordinates, or dimensional shapes, where immutability is beneficial.

# #### Basic Example
# ```python
# point = (2.5, 3.5)
# ```

# #### Advanced Example: Storing Model Hyperparameters
# Tuples are suitable for storing model hyperparameters since they should not be modified after initialization.

# ```python
# Hyperparameters for a neural network model
hyperparameters = (0.01, 32, 50)  # (learning_rate, batch_size, epochs)
# print(help(hyperparameters))

# Access each hyperparameter
learning_rate, batch_size, epochs = hyperparameters

print(f"Learning Rate: {learning_rate}, Batch Size: {batch_size}, Epochs: {epochs}")
# ```

# **Explanation:** By using a tuple, we ensure that the `hyperparameters` remain unchanged, which is critical for consistency during model training.

# ---

# ### 3. **Set**

# A `set` is an unordered collection of unique elements. 
# Sets are used in AI to handle collections of distinct items, 
# like vocabulary terms in NLP or unique labels in classification tasks.

# #### Basic Example
# ```python
# unique_labels = {0, 1, 2}
# ```

# #### Advanced Example: Extracting Unique Words from a Text Corpus
# Sets are ideal for extracting unique vocabulary from text data in NLP since they automatically discard duplicates.

# ```python
corpus = ["AI is transforming", "transforming the world", "world of AI"]
unique_words = set()

for sentence in corpus:
    words = sentence.lower().split()  # Split and convert to lowercase
    unique_words.update(words)  # Add words to the set

print("Unique vocabulary:", unique_words)
# ```

# **Explanation:** Using a set, we can extract the unique vocabulary from a text corpus, which is useful for building vocabulary for word embeddings or tokenization.

# ---

# ### 4. **Dictionary**

# A `dictionary` is an unordered collection of key-value pairs. Dictionaries are widely used in AI to store mappings, like word frequencies, class labels, and configurations.

# #### Basic Example
# ```python
# config = {'learning_rate': 0.01, 'batch_size': 32}
# ```

# #### Advanced Example: Word Frequency Count in NLP
# Counting word frequencies in a text corpus is essential in NLP for analyzing and encoding text data.

# ```python
# corpus = ["AI is transforming", "transforming the world", "world of AI"]
# word_count = {}

# for sentence in corpus:
#     words = sentence.lower().split()  # Split and convert to lowercase
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1  # Count each word

# print("Word frequencies:", word_count)
# ```

# **Explanation:** This code counts word frequencies using a dictionary, which is often a preliminary step in NLP tasks like TF-IDF computation or vocabulary building.

# ---

# ### Advanced Collections from the `collections` Module

# Python’s `collections` module provides additional data structures that are useful in AI tasks.

# ---

# ### 5. **Counter**

# `Counter` is a subclass of `dict` used for counting elements, which is particularly useful in NLP for word frequency analysis.

# #### Example: Word Frequency Count Using `Counter`
# ```python
# from collections import Counter

# corpus = ["AI is transforming", "transforming the world", "world of AI"]
# words = [word.lower() for sentence in corpus for word in sentence.split()]
# word_count = Counter(words)

# print("Word frequencies:", word_count)
# ```

# **Explanation:** `Counter` provides a convenient way to count word occurrences, simplifying the code needed for frequency analysis.

# ---

# ### 6. **defaultdict**

# `defaultdict` is a subclass of `dict` that provides default values for non-existent keys. This is useful in AI for grouping data or initializing complex data structures.

# #### Example: Grouping Data by Label
# In classification tasks, `defaultdict` can help group data points by their labels.

# ```python
# from collections import defaultdict

# # Sample labeled data
# data = [(0, [0.1, 0.2]), (1, [0.3, 0.4]), (0, [0.5, 0.6]), (1, [0.7, 0.8])]
# grouped_data = defaultdict(list)

# # Group data points by label
# for label, features in data:
#     grouped_data[label].append(features)

# print("Grouped data:", dict(grouped_data))
# ```

# **Explanation:** `defaultdict` simplifies the code for grouping data points by their labels, which is useful in pre-processing for classification.

# ---

# ### 7. **deque**

# `deque` (double-ended queue) allows for fast appends and pops from both ends, making it ideal for tasks that require efficient, flexible data storage.

# #### Example: Sliding Window for Time Series Data
# In AI, a sliding window is often used in time series analysis to capture sequences of data points.

# ```python
# from collections import deque

# # Sample time series data
# data = [1, 2, 3, 4, 5, 6]
# window_size = 3
# window = deque(maxlen=window_size)

# # Process data in a sliding window
# for point in data:
#     window.append(point)
#     if len(window) == window_size:
#         print("Current window:", list(window))
# ```

# **Explanation:** `deque` efficiently manages a sliding window of data points, which is useful in time series analysis for AI applications like anomaly detection or trend analysis.

# ---

# ### Summary Table

# | Collection   | Description                      | Example Use in AI                                                   |
# |--------------|----------------------------------|----------------------------------------------------------------------|
# | **List**     | Ordered, mutable                 | Storing data batches, processing in loops                           |
# | **Tuple**    | Ordered, immutable               | Storing hyperparameters, fixed data structures                      |
# | **Set**      | Unordered, unique elements       | Extracting unique words in NLP, storing unique labels               |
# | **Dictionary** | Key-value pairs               | Configuration storage, word frequency counts                        |
# | **Counter**  | Specialized dict for counting    | Word or label frequency analysis in NLP                             |
# | **defaultdict** | Dict with default values     | Grouping data by label, initializing nested structures              |
# | **deque**    | Double-ended queue               | Sliding window for time series data                                 |

# These collections and their specialized counterparts enable efficient data handling and management, which is crucial in AI for data preprocessing, model configuration, and analysis tasks.AI field.

# ---

# ### 1. **List**

# A `list` is an ordered, mutable collection that allows duplicate elements. 
# Lists are commonly used in AI for storing datasets, managing data batches, and keeping track of model predictions.

# #### Basic Example
# ```python
# numbers = [1, 2, 3, 4, 5]
# ```

# #### Advanced Example: Storing and Managing Batches of Data
# In machine learning, data is often processed in batches to make training more efficient. A `list` can be used to store these batches.

# ```python
# # Sample data
# data = [0.5, 0.6, 0.8, 0.9, 0.2, 0.3, 0.4, 0.7]

# # Split data into batches of size 3
# batch_size = 3
# batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

# # Process each batch
# for batch in batches:
#     print("Processing batch:", batch)
# ```

# **Explanation:** This code divides the `data` list into smaller batches of size 3, 
# which is a common preprocessing step in machine learning training pipelines.

# ---

# ### 2. **Tuple**

# A `tuple` is an ordered, immutable collection that allows duplicate elements.
# Tuples are often used in AI to represent fixed sets of data, such as model hyperparameters, coordinates, or dimensional shapes, where immutability is beneficial.

# #### Basic Example
# ```python
# point = (2.5, 3.5)
# ```

# #### Advanced Example: Storing Model Hyperparameters
# Tuples are suitable for storing model hyperparameters since they should not be modified after initialization.

# ```python
# # Hyperparameters for a neural network model
# hyperparameters = (0.01, 32, 50)  # (learning_rate, batch_size, epochs)

# # Access each hyperparameter
# learning_rate, batch_size, epochs = hyperparameters

# print(f"Learning Rate: {learning_rate}, Batch Size: {batch_size}, Epochs: {epochs}")
# ```

# **Explanation:** By using a tuple, we ensure that the `hyperparameters` remain unchanged,
# which is critical for consistency during model training.

# ---

# ### 3. **Set**

# A `set` is an unordered collection of unique elements.
# Sets are used in AI to handle collections of distinct items, like vocabulary terms in NLP or unique labels in classification tasks.

# #### Basic Example
# ```python
# unique_labels = {0, 1, 2}
# ```

# #### Advanced Example: Extracting Unique Words from a Text Corpus
# Sets are ideal for extracting unique vocabulary from text data in NLP since they automatically discard duplicates.

# ```python
# corpus = ["AI is transforming", "transforming the world", "world of AI"]
# unique_words = set()

# for sentence in corpus:
#     words = sentence.lower().split()  # Split and convert to lowercase
#     unique_words.update(words)  # Add words to the set

# print("Unique vocabulary:", unique_words)
# ```

# **Explanation:** Using a set, we can extract the unique vocabulary from a text corpus,
# which is useful for building vocabulary for word embeddings or tokenization.

# ---

# ### 4. **Dictionary**

# A `dictionary` is an unordered collection of key-value pairs. 
# Dictionaries are widely used in AI to store mappings, like word frequencies, class labels, and configurations.

# #### Basic Example
# ```python
# config = {'learning_rate': 0.01, 'batch_size': 32}
# ```

# #### Advanced Example: Word Frequency Count in NLP
# Counting word frequencies in a text corpus is essential in NLP for analyzing and encoding text data.

# ```python
# corpus = ["AI is transforming", "transforming the world", "world of AI"]
# word_count = {}

# for sentence in corpus:
#     words = sentence.lower().split()  # Split and convert to lowercase
#     for word in words:
#         word_count[word] = word_count.get(word, 0) + 1  # Count each word

# print("Word frequencies:", word_count)
# ```

# **Explanation:** This code counts word frequencies using a dictionary, 
# which is often a preliminary step in NLP tasks like TF-IDF computation or vocabulary building.

# ---

# ### Advanced Collections from the `collections` Module

# Python’s `collections` module provides additional data structures that are useful in AI tasks.

# ---

# ### 5. **Counter**

# `Counter` is a subclass of `dict` used for counting elements,
# which is particularly useful in NLP for word frequency analysis.

# #### Example: Word Frequency Count Using `Counter`
# ```python
# from collections import Counter

# corpus = ["AI is transforming", "transforming the world", "world of AI"]
# words = [word.lower() for sentence in corpus for word in sentence.split()]
# word_count = Counter(words)

# print("Word frequencies:", word_count)
# ```

# **Explanation:** `Counter` provides a convenient way to count word occurrences, 
# simplifying the code needed for frequency analysis.

# ---

# ### 6. **defaultdict**

# `defaultdict` is a subclass of `dict` that provides default values for non-existent keys.
# This is useful in AI for grouping data or initializing complex data structures.

# #### Example: Grouping Data by Label
# In classification tasks, `defaultdict` can help group data points by their labels.

# ```python
# from collections import defaultdict

# # Sample labeled data
# data = [(0, [0.1, 0.2]), (1, [0.3, 0.4]), (0, [0.5, 0.6]), (1, [0.7, 0.8])]
# grouped_data = defaultdict(list)

# # Group data points by label
# for label, features in data:
#     grouped_data[label].append(features)

# print("Grouped data:", dict(grouped_data))
# ```

# **Explanation:** `defaultdict` simplifies the code for grouping data points by their labels, 
# which is useful in pre-processing for classification.

# ---

# ### 7. **deque**

# `deque` (double-ended queue) allows for fast appends and pops from both ends,
# making it ideal for tasks that require efficient, flexible data storage.

# #### Example: Sliding Window for Time Series Data
# In AI, a sliding window is often used in time series analysis to capture sequences of data points.

# ```python
# from collections import deque

# # Sample time series data
# data = [1, 2, 3, 4, 5, 6]
# window_size = 3
# window = deque(maxlen=window_size)

# # Process data in a sliding window
# for point in data:
#     window.append(point)
#     if len(window) == window_size:
#         print("Current window:", list(window))
# ```

# **Explanation:** `deque` efficiently manages a sliding window of data points, 
# which is useful in time series analysis for AI applications like anomaly detection or trend analysis.

# ---

# ### Summary Table

# | Collection   | Description                      | Example Use in AI                                                   |
# |--------------|----------------------------------|----------------------------------------------------------------------|
# | **List**     | Ordered, mutable                 | Storing data batches, processing in loops                           |
# | **Tuple**    | Ordered, immutable               | Storing hyperparameters, fixed data structures                      |
# | **Set**      | Unordered, unique elements       | Extracting unique words in NLP, storing unique labels               |
# | **Dictionary** | Key-value pairs               | Configuration storage, word frequency counts                        |
# | **Counter**  | Specialized dict for counting    | Word or label frequency analysis in NLP                             |
# | **defaultdict** | Dict with default values     | Grouping data by label, initializing nested structures              |
# | **deque**    | Double-ended queue               | Sliding window for time series data                                 |

# These collections and their specialized counterparts enable efficient data handling and management,
# which is crucial in AI for data preprocessing, model configuration, and analysis tasks.

# fruits=['apple', 'orange','banana','lemon','apple','orange','banana','orange']
# fruits_new=[]
# for fruit in fruits:
#     if fruit.startswith("o"):
#         fruits_new.append(fruit)


# # print(help(fruits))

# # loop=[fruits[i] for i in range(len(fruits))]
# print(fruits_new)


# Packages lists

#  |  append(self, object, /)
#  |      Append object to the end of the list.
#  |  
#  |  clear(self, /)
#  |      Remove all items from list.
#  |  
#  |  copy(self, /)
#  |      Return a shallow copy of the list.
#  |  
#  |  count(self, value, /)
#  |      Return number of occurrences of value.
#  |  
#  |  extend(self, iterable, /)
#  |      Extend list by appending elements from the iterable.
#  |  
#  |  index(self, value, start=0, stop=9223372036854775807, /)
#  |      Return first index of value.
#  |      
#  |      Raises ValueError if the value is not present.
#  |  insert(self, index, object, /)
#  |      Insert object before index.
#  |  
#  |  pop(self, index=-1, /)
#  |      Remove and return item at index (default last).
#  |      
#  |      Raises IndexError if list is empty or index is out of range.
#  |  
#  |  remove(self, value, /)
#  |      Remove first occurrence of value.
#  |      
#  |      Raises ValueError if the value is not present.
#  |  
#  |  reverse(self, /)
#  |      Reverse *IN PLACE*.
#  |  
#  |  sort(self, /, *, key=None, reverse=False)
#  |      Sort the list in ascending order and return None.
#  |      
#  |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
#  |      order of two equal elements is maintained).
#  |      
#  |      If a key function is given, apply it once to each list item and sort them,
#  |      ascending or descending, according to their function values.
#  |      
#  |      The reverse flag can be set to sort in descending order.