# def fun(num):
#     if(num>0): #base condition
#         fun(num-1)
#         print(num ,end=" ")
        

        
# #calling function        
# fun(4)

def sumOfNumbers(num):
    if num==1:
        return num
    else:
        return num+sumOfNumbers(num-1)


sumOfNumbers(4)