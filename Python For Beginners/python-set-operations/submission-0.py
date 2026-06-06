from typing import List

def count_unique_words(words: List[str]) -> int:
    my_set = set(words)
    my_unique_list = list(my_set)
    length = len(my_unique_list)
    if length > 0 : return length
    else: return 0

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
