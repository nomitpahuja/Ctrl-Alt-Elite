from name_maker import make_name
import sys
sys.path.insert(0, '/home/ankit/Desktop/python/Hackgrid/new files/Ctrl-Alt-Elite/scripts/')
from MLGen import generator

def giveNames():
    return {"names": (make_name(10) + generator(10))}

if __name__ == "__main__":
    print(giveNames())
