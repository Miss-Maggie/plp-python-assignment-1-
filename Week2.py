# Description: This file contains the code for the Week 2 assignment.
#create an empty list
my_list = []
#append elements to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert value into list
my_list.insert(1, 15)
print(my_list)  
#extend list with another list
my_list.extend([50, 60, 70])
#remove last element from list
my_list.pop()
#sort list in ascending order
my_list.sort()
#find and print index of value 30 in list
index_of_30 = my_list.index(30)
print(index_of_30)

