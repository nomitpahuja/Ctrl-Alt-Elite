from name_maker import make_name
import sys
from MLGen import generator

def giveNames(num = 12):
    return {"names": (make_name(num) + generator(num))}

def givebacknames(word = ""):
    names = giveNames()["names"]
    prefix = names[:12]
    postfix = names[12:24]
    gen = []
    gen += word + prefix[i]
    gen += prefix[i][:-len(prefix[i]) // 2] + word + prefix[i][len(prefix[i]) // 2 : ]
    gen += postfix[i] + word
    return gen