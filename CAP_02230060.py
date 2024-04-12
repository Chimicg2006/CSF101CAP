################################
# Name: Chimi Gyeltshen
# Deparment: Electrical Deparment
# STudent ID no: 02230060
################################
# REFERENCES
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://youtu.be/Qcefu1jVPds?si=C_9lLKrclFxobfCj
# https://youtu.be/Uh2ebFW8OYM?si=jDO41HwoF_gv2zbm
################################
# SOLUTION
# Your Solution Score: 50054
# Put your number here: 0
################################
def read_input():
    return open('CSF101CAP/input_0_cap1.txt','r')

def calculate_score(textfile):
    store= {'A X': 2, 'A Y': 4, 'A Z': 9, 'B X': 1, 'B Y': 5, 'B Z': 7, 'C X': 1, 'C Y': 6, 'C Z': 7} 
    score = 0
    for text in textfile:
        value = text.strip()
        if value in store:
            score += store[value]
    print("total value: ",score)

calculate_score(read_input())
