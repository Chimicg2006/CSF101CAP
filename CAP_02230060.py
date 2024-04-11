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
# Read the input.txt file
def read_input():
    f = open('input_0_cap1.txt', 'r')
    print(f.read())
    f.close()

# code here to read your input file
# solution
def calculate_score():
    read=open('input_0_cap1.txt', 'r')
    reader=read.read()
    score=0
    for i in reader: 
        if i=="A":
            score+=1 # 1 for rock
        elif i== "B":
            score+=2 # 2 for paper
        elif i=="C":
            score+=3 # 3 for scissor
        elif i=="X":
            score+=0 # 0 for lossing the round
        elif i=="Y":
            score+=3 # 3 for end have having draw
        elif i=="Z":
            score+=6 # 6 for winning the round
    print("score is",score)
calculate_score()

# implement your solution here.
# print your solution to output as:"the total score is: <score>"
# Other parts of code here to run your functions and printing of the input.

