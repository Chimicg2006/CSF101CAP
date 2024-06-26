################################
# Name: Chimi Gyeltshen
# Deparment: Electrical Deparment
# STudent ID no: 02230060
################################
# REFERENCES
# https://youtu.be/Qcefu1jVPds?si=C_9lLKrclFxobfCj
# https://youtu.be/Uh2ebFW8OYM?si=jDO41HwoF_gv2zbm
################################
# Score: 49894
# std number = 02230060
################################
def read_input():
    return open('input_0_cap1.txt','r') # Reads the file that we have put

def calculate_score(textfile):
    store= {'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z':9, 'C X':2, 'C Y':6, 'C Z':7} # It is a dict that stores specific key for specific values
    score = 0
    for text in textfile:
        value = text.strip()
        if value in store:
            score += store[value]
    print("total value: ",score) 

calculate_score(read_input()) # Gives us the total score of the input file

