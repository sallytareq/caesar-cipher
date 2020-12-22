import re

letters ={
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

def encrypt(en_str , key):
    while key >= 26:
        key -= 26
    result = []
    for x in en_str.lower():
        not_apha = re.findall("[a-z]",x)
        if len(not_apha) == 0:
            result.append(x)
        else:
            y = letters[x]+key
            while y > 26:
                y -= 26
            if y == 0: y = 1
            # print(y)
            for l in letters:
                # print(letters[l])
                if letters[l] == y: result.append(l)
    return "".join(result)

def decrypt(de_str, key = "none"):
    if key != "none":
        result = []
        for x in de_str.lower():
            # print(x)
            not_apha = re.findall("[a-z]",x)
            if len(not_apha) == 0: result.append(x)
            else:
                y = letters[x]-key
                # print(y)
                if y < 0: y = 26 + y
                while y > 26: y -= 26
                if y == 0: y = 1
                for l in letters: 
                    if letters[l] == y: result.append(l)
        return "".join(result)
    else:
        

    

if __name__ == "__main__":
    # x = encrypt('abc' , 1)
    # x = encrypt('    !#||;067219$@11y%^&*()P{hElLo WorlD}|:"<>?,./;[]    ' , 90)
    # x = encrypt('abc' , 27)
    x = decrypt('bcd' , 27)
    print(x)