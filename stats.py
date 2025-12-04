def count_word(words):
    lst = words.split()
    return len(lst)

def count_char(words):
    words = list(words)
    char = {}
    try:
        for i in words:
            i = i.lower()
            if i.isalpha() and i in char:
                char[i] += 1 
            elif i.isalpha() and i not in char:
                char[i] = 1
            else:
                continue
    except Exception as e:
        print(e)
    return char
