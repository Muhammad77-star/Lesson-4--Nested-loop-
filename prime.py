lower= int(input("Enter a lower range:"))
upper= int(input("Enter a upper range:"))
print("Prime numbers between", lower, "and", upper, "are: ")
for num in range(lower, upper+1):
    if num > 1:
         for i in range(2,num):
             if (num % 1)== 0:
                 break
         else:
            print(num)
