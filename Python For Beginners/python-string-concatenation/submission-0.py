def concatenate(s1: str, s2: str) -> str:
    length = len(s1+s2)
    if length <= 10:
        return s1 + s2
    else:
       return "Too long!"




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
