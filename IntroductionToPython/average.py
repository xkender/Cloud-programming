#avg2.py
# A Simple program to average two exam scores
# Illustrates use of multiple input

def main():
    print ("This program computes the average of two exam scores.")

    score1, score2 = eval(input("Enter two scores seperated by a comma: ")) #What is user enters text or single value?
    # We could also use
    # score1 = eval(input("Enter the first score "))
    # score2 = eval(input("Enter the second s core "))
    average = (score1 + score2) / 2

    print ("The average of the scores is:", average)

main()
# calling the script from idle or python:
# import average or average.main()
