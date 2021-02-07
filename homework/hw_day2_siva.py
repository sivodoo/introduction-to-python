# Day 2 Homework - Siva
#
# Question 1
#
my_list = []
ctr = 0
my_list_len = int(input("How many items will be in your list: "))
for i in range (my_list_len):
    list_item = input("Enter the list item: ")
    ctr += 1
    my_list.append(list_item)
    
print("List prior to Swap: ", my_list)

if my_list_len %2 == 0 :
    max_ctr = (my_list_len //2)-1
else:
    max_ctr = my_list_len // 2
    
ctr = 0
while ctr <= max_ctr:
        my_list[ctr], my_list[max_ctr+ctr+1] = my_list[max_ctr+ctr+1], my_list[ctr]
        ctr += 1
        if my_list_len%2 != 0 and ctr == max_ctr:
            break
  
print(my_list)

# Question 2
#
while True :
    try :
        n = int(input("Please enter a single digit positive number: "))
    except :
        print("It should be a number.. try again..")
        continue

    if n<0 or n > 9 :
        print("Ensure you enter a single digit positive number...try again...")
    else:
        break
even_list = []
for i in range(n) :
    if i%2 == 0:
        even_list.append(i)

print("Even numbers from 0 to ", n, " are ", even_list)

