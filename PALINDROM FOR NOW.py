def palindrom(s) -> str:
    if s == s[::-1]:
        return True
    return False
s = input()
print(palindrom(s))