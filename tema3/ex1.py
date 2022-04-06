def your_function(*args1,**args2):
    n = len(args1)
    sum = 0
    for i in range(n):
        if type(args1[i]) == int or type(args1[i]) == float:
            sum += args1[i]
    return sum
print(f"Your sum is: {your_function()}")


