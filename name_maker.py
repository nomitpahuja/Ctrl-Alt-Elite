import csv
import re
from random import *
'''with open('comp.csv') as file_csv:
    csv_reader=csv.reader(file_csv)
    for line in csv_reader:
        a= line[0]
        a=re.sub("[ ?()-.,]","",a)
        print(a)'''     
global letter_count 
letter_count = 0 # Track how many letters have been created.
class letter():
    # Each letter has a lowercase character, an uppercase character, and
    # identifiers as vowel or consonant.
    def __init__(self, lowerchar, upperchar, is_vowel, is_consonant):
        global letter_count
        self.upperchar = upperchar
        self.lowerchar = lowerchar
        self.is_vowel = is_vowel
        self.is_consonant = is_consonant
        self.num = letter_count # Record letter's place in the alphabet.
        letter_count += 1

# Define the alphabet.
global alphabet
alphabet = [letter('a','A',True,False),
            letter('b','B',False,True),
            letter('c','C',False,True),
            letter('d','D',False,True),
            letter('e','E',True,False),
            letter('f','F',False,True),
            letter('g','G',False,True),
            letter('h','H',False,True),
            letter('i','I',True,False),
            letter('j','J',False,True),
            letter('k','K',False,True),
            letter('l','L',False,True),
            letter('m','M',False,True),
            letter('n','N',False,True),
            letter('o','O',True,False),
            letter('p','P',False,True),
            letter('q','Q',False,True),
            letter('r','R',False,True),
            letter('s','S',False,True),
            letter('t','T',False,True),
            letter('u','U',True,False),
            letter('v','V',False,True),
            letter('w','W',False,True),
            letter('x','X',False,True),
            letter('y','Y',True,True),
            letter('z','Z',False,True)
            ]

# Read in probability matrix.
# prob[i][j] = probability that letter j comes after letter i
global prob
file_name = 'fprob.csv' # Change to file that contains the probability matrix you wish to use.
prob = []
with open(file_name, newline='',encoding='utf-8') as csvfile:
    prob_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in prob_reader:
        prob.append([])
        for num in row:
            prob[len(prob)-1].append(float(num))

# Normalize the probabiliyt matrix so that the sum of each row is 1.
for i in range(0,len(alphabet)):
    total = 0
    for j in range(0,len(alphabet)):
        total += prob[i][j]
    for j in range(0,len(alphabet)):
        prob[i][j] /= total

def uniform(x1,x2):
    # Generate a random floating-point number between x1 and x2.
    r = x1 + random()*(x2-x1)
    return r
    
def rand_int(x1,x2):
    # Generate a random integer number between x1 and x2.
    r = int( int(x1) + random()*(int(x2)-int(x1)) )
    return r

def make_name():
    # Determine name length.
    lmin = 3 # Minimum length.
    lmax = 10 # Maximum length.
    name_length = rand_int(lmin,lmax)
    
    # Initialize string.
    my_name = ""
    
    prev_vowel = False # Was the previous letter a vowel?
    prev_consonant = False # Was the previous letter a consonant?
    prev2_vowel = False # Were the previous 2 letters vowels?
    prev2_consonant = False # Were the previous 2 letters consonants?
    prev_num = 0 # Number of the previous letter.
    # Generate letters for name.
    for i in range(0,name_length):
        if (i == 0):
            a = alphabet[rand_int(0,25)]
            my_name = my_name + a.upperchar
        else:
            a = get_letter(prev_num,prev2_vowel,prev2_consonant)
            my_name = my_name + a.lowerchar
        prev2_vowel = (a.is_vowel and prev_vowel)
        prev2_consonant = (a.is_consonant and prev_consonant)
        prev_vowel = a.is_vowel
        prev_consonant = a.is_consonant
        prev_num = a.num
    return my_name
        
        
def get_letter(prev_num,need_consonant,need_vowel): 
    global alphabet
    # Select the next letter.
    done = False
    while (not done):
        a = pick_letter(prev_num)
        if ((need_consonant and a.is_vowel) or (need_vowel and a.is_consonant)):
            done = False
        else:
            done = True
    return a

def pick_letter(i):
    # Pick a letter based on the probability matrix.
    global prob
    r = random()
    total = 0 # Sum of entries thus far in the ith row of prob.
    for j in range(0,len(alphabet)):
        total += prob[i][j]
        if( r <= total or j == len(alphabet) ):
            return alphabet[j]
    print("problem!") # Code *shouldn't* reach this point.
    return alphabet(25)
for i in range(20):       
    name1 = make_name()
    print(name1)
   
        
