import random

def main():
    categories_list = ["red objects", "green objects", "blue objects"]
    category = random.randint(0, 2)
    
    answers = []
    for i in range(10):
        temp = input(categories_list[category] + ": ")
        answers.append(temp)

    for i in range(10):
        print("{:^24s}".format(answers[i]))

main()