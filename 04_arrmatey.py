import sys

def main():
    arguments = sys.argv
    for i in range(len(arguments)):
        print("Argv of {} is {}".format(i, arguments[i]))

    arguments.sort(reverse=True, key=len)
    for i in range(len(arguments)):
        print(arguments[i])
main()