def myFunction():
    '''
    Write a Python function that return the sum of every digit of your student ID
    And print the answer before you return
    You can write in python2 or python3 :D
    '''
    id=input("Enter your id:")
    sum=0
    for i in range(len(id)):
        sum+=int(id[i])
    print(sum)




    return sum


if __name__ == '__main__':
    myFunction()

