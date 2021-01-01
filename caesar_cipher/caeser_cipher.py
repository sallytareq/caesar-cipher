import re
import nltk

nltk.download('words')
words_list = nltk.corpus.words.words()
# print(type(words_list))
# print(len(words_list))

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
    while key >= 26: key -= 26
    result = []
    for x in en_str.lower():
        not_apha = re.findall("[a-z]",x)
        if len(not_apha) == 0: result.append(x)
        else:
            y = letters[x]+key
            while y > 26: y -= 26
            if y == 0: y = 1
            for l in letters: 
                if letters[l] == y: result.append(l)
    return "".join(result)

def decrypt(de_str, key = "none"):
    if key != "none":
        result = []
        for x in de_str.lower():
            not_apha = re.findall("[a-z]",x)
            if len(not_apha) == 0: result.append(x)
            else:
                y = letters[x]-key
                if y < 0: y = 26 + y
                while y > 26: y -= 26
                if y == 0: y = 1
                for l in letters: 
                    if letters[l] == y: result.append(l)
        return "".join(result)
    else:
        options = []
        for key in range(1,27):
            result = []
            for x in de_str.lower():
                not_apha = re.findall("[a-z]",x)
                if len(not_apha) == 0: result.append(x)
                else:
                    y = letters[x]-key
                    if y < 0: y = 26 + y
                    while y > 26: y -= 26
                    if y == 0: y = 1
                    for l in letters: 
                        if letters[l] == y: result.append(l)
            checker = "".join(result)
            options.append([key , checker])

        dec_key = get_key(options)
        return f"Key: {dec_key} \nDecrypted message: {decrypt(de_str , dec_key)}"

def get_key(options): 
    totals = []
    counter = 0
    key = 0
    for option in options:
        counter = 0
        # print(option)
        words = option[1].split()
        # print(words)
        for word in words:
            # print(word)
            if word in words_list or word.lower() in words_list or word.upper() in words_list:
                counter += 1
        totals.append([option[0] , counter])
    
    for sets in totals:
        if sets[1] >= counter:
            counter = sets[1]
            key = sets[0]
    
    return key

    

if __name__ == "__main__":
    # x = encrypt('abc' , 1)
    x = encrypt(' Hi  !#||;067219$@11y%^&*()P{hElLo WorlD}|:"<>?,./;[] ' , 90)
    x = encrypt('Hello' , 30)
    print(x)
    y = decrypt('QEB NRFZH YOLTK CLU GRJMP LSBO QEB ALD')
    print(y)
    # print(z)