# In Python, string indexing allows you to access specific characters within a string by their position. This can be very useful in AI, especially in fields like Natural Language Processing (NLP), where it’s often necessary to manipulate and analyze text at the character level. Python uses zero-based indexing, meaning the first character has an index of 0, the second character has an index of 1, and so on. Negative indexing starts from the end of the string, with `-1` referring to the last character.

# ### Basic String Indexing

# Given a string `s = "AI is transforming the world"`, we can access characters as follows:

# - `s[0]`: First character (`'A'`)
# - `s[-1]`: Last character (`'d'`)
# - `s[3:7]`: Substring from index 3 to 6 (`'is t'`)

# ### Advanced Use Cases of String Indexing in AI

# 1. **Character-Level Tokenization**

#    In NLP, character-level tokenization breaks down a word or sentence into individual characters. This is especially useful for languages with complex character structures or when building character-based language models.

#    ```python
text = "AI"
char_tokens = [text[i] for i in range(len(text))]
print(char_tokens)  # Output: ['A', 'I']
#    ```

# 2. **Reversing a String**

#    String reversal can be achieved using slicing with negative indexing, which can sometimes be useful in sequence generation tasks, like palindrome detection.

#    ```python
text = "Seid Mengistu"
reversed_text = text[::-1]
print(reversed_text)  # Output: "IA"
#    ```

# 3. **Extracting Prefixes and Suffixes**

#    Prefixes and suffixes are useful for analyzing word morphology in NLP. 
# You can use slicing to extract specific parts of a word, such as the root or ending.

#    ```python
word = "processing"
prefix = word[:4]  # First 4 characters
suffix = word[-4:]  # Last 4 characters
print("Prefix:", prefix)  # Output: "proc"
print("Suffix:", suffix)  # Output: "sing"
#    ```

# 4. **Analyzing Palindromes**

# In AI applications like text classification, 
# you may need to determine if a string is a palindrome (reads the same forwards and backwards). 
# Using indexing and slicing helps check this efficiently.

#    ```python
word = "madam"
is_palindrome = word == word[::-1]
print("Is palindrome:", is_palindrome)  # Output: True
#    ```

# 5. **Character Replacement for Data Augmentation**

#    Replacing or augmenting characters in specific positions can be used to simulate typos or variations in text data, which is beneficial in NLP for building robust models.

#    ```python
text = "Artificial Intelligence"
index_to_replace = 11
augmented_text = text[:index_to_replace] + "X" + text[index_to_replace + 1:]
print(augmented_text)  # Output: "Artificial Xntelligence"
#    ```

# 6. **Extracting Words Based on Character Patterns**

#    In tasks like named entity recognition (NER), you might want to extract substrings based on certain patterns or positions. String indexing and slicing allow you to search for patterns within text data.

#    ```python
text = "In 2023, AI will continue to grow."
year = text[3:7]  # Extracts the year
print("Year:", year)  # Output: "2023"
#    ```

# 7. **Iterating Over Characters in Reverse Order**

#    Sometimes, analyzing text from the end (e.g., checking suffixes or matching character sequences) is useful.
# Negative indexing and slicing provide an efficient way to iterate backwards.

#    ```python
text = "Transformer"
for i in range(len(text) - 1, -1, -1):
    print(text[i], end=" ")  # Output: r e m r o f s n a r T
#    ```

# 8. **Finding and Slicing Substrings Dynamically**

#    Extracting parts of a string based on specific keywords is often required in text mining. For instance, you might want to find a keyword and retrieve a portion of the text before or after it.

#    ```python
text = "Deep learning and machine learning are core AI fields."
keyword = "learning"
start_index = text.find(keyword)
end_index = start_index + len(keyword)
context = text[start_index - 5:end_index + 5]  # Extract context around the keyword
print("Context:", context)  # Output: "Deep learning and m"
#    ```

# 9. **Selective Character Removal Using Indexing**

#    Removing specific characters based on their position in the string can be useful in text cleaning or data augmentation.

#    ```python
text = "AI,ML,DL"
# Removing comma at index 2
cleaned_text = text[:2] + text[3:]
print(cleaned_text)  # Output: "AIML,DL"
#    ```

# 10. **Checking Character Sequences in N-Grams**

#     N-grams are sequences of `n` characters or words, used in NLP to analyze text. String indexing helps create these sequences.

#     ```python
text = "deep learning"
n = 3
n_grams = [text[i:i + n] for i in range(len(text) - n + 1)]
print(n_grams)  # Output: ['dee', 'eep', 'ep ', 'p l', ' le', 'lea', 'ear', 'arn', 'rni', 'nin', 'ing']
#     ```

# ### Summary

# String indexing provides a flexible way to access and manipulate text data at the character level, which is essential in AI, especially in NLP. 
# By mastering string indexing and slicing, you can build customized solutions for tasks like data augmentation, tokenization, and pattern extraction.


name=input("Enter your name: ")

while name == "":
    print("Name cannot be empty.")
    name=input("Enter your name: ")


age = int(input("Enter your age: "))

while age <0:
    print("Age cannot be empty.")
    age=int(input("Enter your age: "))
print(f"You are {age} years old")