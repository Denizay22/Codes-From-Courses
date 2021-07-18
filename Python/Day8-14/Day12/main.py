# you can access global variables from functions BUT you can't change them directly
globalVar = 1


def changeGlobalVar():
    globalVar = 2  # <---- IDE already says there is a problem
    print(globalVar)  # prints 2


changeGlobalVar()
print(globalVar)  # prints 1


# but you can use Global keyword to change it. but it is not recommended to use. use return function instead
def changeGlobalVar2():
    global globalVar
    globalVar = 2
    print(globalVar)  # prints 2


changeGlobalVar2()
print(globalVar)  # prints 2


def changeGlobalVar3():
    return globalVar + 1


globalVar = changeGlobalVar3()
print(globalVar)

# constants (finale) variables usually written as all caps.
PI = 3.1415
URL = "https://www.google.com"


liste = [False]*50 + [True]*50
print(liste)
