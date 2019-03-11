from name_maker import make_name
import sys
from MLGen import generator

def giveNames(num = 12):
    return {"names": (make_name(num) + generator(num))}

if __name__ == "__main__":
    word = input("Enter word: ")
    names = giveNames()["names"]
    prefix = names[:12]
    postfix = names[12:24]
    for i in range(9):
        print(word + prefix[i])
    for i in range(9, 12):
        print(prefix[i][:-len(prefix[i]) // 2] + word + prefix[i][len(prefix[i]) // 2 : ])
    for i in range(0,12):
        print(postfix[i] + word)