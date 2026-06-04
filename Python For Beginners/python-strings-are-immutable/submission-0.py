def remove_fourth_character(word: str) -> str:
    w1 = word[0:] # neetcode
    four_char = word[0:3]# "nee"
    else_char = word[4:]# "code"
    new_word = four_char + else_char
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
