a = input("Enter a list elements separated by space ")
list = a.split()
even=0;
odd=0;
for x in list:
    if x % 2 == 0: 
        even_count += 1
  
    else: 
        odd_count += 1
print("number of even numbers = ", even)
print("number of odd numbers = ",odd)
