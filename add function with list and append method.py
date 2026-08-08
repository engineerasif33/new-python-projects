def add(n1,n2):
    return n1 + n2
list_of_numbers=[]

for a in range(2):
   num1=int(input("enter first number:"))
   list_of_numbers.append(num1)
  
   #total = add(num1,num2)
print ("total is :", add(list_of_numbers[0], list_of_numbers[1]))
print()