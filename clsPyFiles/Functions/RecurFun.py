def sumRecur(num): #O(n)
    if num==1:
        return num
    else:
        return num*sumRecur(num-1)


if __name__ == '__main__':
  print(sumRecur(5))