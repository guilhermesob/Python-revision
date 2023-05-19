def test():
    print("This is the function")
    print("Another statement....")

test()

def para(name, age):
    print("Hi "+name)
    print("your age is "+str(age))

para("Faisal Jafri", 20)

# one arguemnt 

# def func(language):
#     print("Interested lang = "+language)

# func("Python")

# two argument or multiple arg
def func1(val1, val2):
    print("Addition of two number = "+str(val1+val2))

func1(10,20)

# keyword argument
def func2(name, age):
    print("Name = "+name)
    print("Age = "+str(age))

func2(age = 39, name ="Faisal")

# Position Argument
def func2(name, age):
    print("Name = "+name)
    print("Age = "+str(age))

func2("Faisal", 30)

