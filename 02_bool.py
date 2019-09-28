boolean_list_1 = [False,True,True,None,True,None,None,False,False,None,True,False]
condition_list = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]
boolean_list_2 = [False,False,None,None,True,True,False,True,None,False,True,None]

for i in range(10):
    string = str(boolean_list_1[i]) + " " + condition_list[i] + " " + str(boolean_list_2[i])
    print(string, end = " => ")
    print(eval(string))