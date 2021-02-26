test1 = "(())"
test2 = "({()()}[()])"
test3 = "{[}()]"

def isOpen(character):
    return True if (character in ['(','{','['] ) else  False
def closes(characterA, characterB):
    pairs = {'(':')','[':']','{':'}'}
    return pairs[characterA] == characterB

def validate(text):
    stack = []
    for character in text:
        if(isOpen(character)):
            stack.append(character)
        else:
            topChar = stack.pop()
            if not closes(topChar,character):
                return False
    return (len(stack) == 0)
print(validate(test1))
print(validate(test2))
print(validate(test3))