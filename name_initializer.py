import csv
global letter_count 
letter_count = 0

race_name = 'grippli'

class letter():
    # Each letter has a lowercase character, an uppercase character, and
    # identifiers as vowel or consonant.
    def __init__(self, lowerchar, upperchar, is_vowel, is_consonant):
        global letter_count
        self.upperchar = upperchar
        self.lowerchar = lowerchar
        self.is_vowel = is_vowel
        self.is_consonant = is_consonant
        self.num = letter_count
        letter_count += 1

def normalize(prob):
    # Normalize the probability matrix so that the sum of each row is 1.
    global alphabet
    new_prob = prob
    for i in range(0,len(alphabet)):
        total = 0
        for j in range(0,len(alphabet)):
            total += prob[i][j]
        if (total > 0):
            for j in range(0,len(alphabet)):
                new_prob[i][j] = prob[i][j]/total
        else:
            for j in range(0,len(alphabet)):
                new_prob[i][j] = len(alphabet)**(-1)
    return new_prob


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

# Initialize probability matrix.
# prob[i][j] = probability that letter j comes after letter i
global prob
file_name = 'defaultprob.csv' # Should initiatlize to all 0s.
prob = []
with open(file_name, newline='',encoding='utf-8') as csvfile:
    prob_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in prob_reader:
        prob.append([])
        for num in row:
            prob[len(prob)-1].append(float(num))

# Read list of pre-generated names. Names should be stored one per line in file.
file_name = 'comp.csv'
with open(file_name, newline='',encoding='utf-8') as csvfile:
    name_reader = csv.reader(csvfile, delimiter=',', quotechar='|') # Record file contents.
    for names in name_reader: # Loop over names in list.
        name = names[0]
        # Loop over letters in the current name.
        for i in range(0,len(name)-1):
            letter1 = name[i]
            letter2 = name[i+1]
            num1 = 0
            num2 = 0
            for i in range(0,len(alphabet)):
                if (letter1 == alphabet[i].lowerchar or letter1 == alphabet[i].upperchar):
                    num1 = alphabet[i].num
                if (letter2 == alphabet[i].lowerchar or letter2 == alphabet[i].upperchar):
                    num2 = alphabet[i].num
            # Add one to the number of times letter number i is followed by letter number i+1.
            prob[num1][num2] += 1

# Normalize the probability matrix.
prob = normalize(prob)

# Write probability matrix to file. This file will be read by the name generator.
file_name = 'fprob.csv'
with open(file_name, 'w', newline='',encoding='utf-8') as csvfile:
    prob_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0,len(alphabet)):
        prob_writer.writerow(prob[i])

import name_maker
