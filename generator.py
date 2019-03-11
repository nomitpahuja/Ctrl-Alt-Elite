from name_maker import make_name
import sys
from MLGen import generator

def giveNames():
    return {"names": (make_name(10) + generator(10))}

if __name__ == "__main__":
    word = input("Enter word: ")
    names = giveNames()["names"]
    prefix = names[:10]
    postfix = names[10:20]
    for i in range(7):
        print(word + prefix[i])
    for i in range(7, 10):
        print(prefix[i][:-len(prefix[i]) // 2] + word + prefix[i][len(prefix[i]) // 2 : ])
    for i in range(3,10):
        print(postfix[i] + word)