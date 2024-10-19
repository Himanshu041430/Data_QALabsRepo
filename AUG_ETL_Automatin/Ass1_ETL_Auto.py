
"""
1. Given a string , write a python code to reverse the string using for loop and slice
operator both ways?
Input: city = "ETLQALabs"
expected output: “sbaL AQ LTE” """

name1 = "ETLQALabs"

name2 = name1[0:3]
name3 = name1[3:5]
name4 = name1[5:]
name5 = name2+" "+name3+" "+name4
print(name5)
rev_name = name5[::-1]
print(rev_name)
# ---------------------same-----------
print("---------------same-----------------")
Subject = "ETLQALabs"
reversed_string = ""

for char in Subject:
    reversed_string = char + reversed_string

print("Reversed using for loop:", reversed_string)

"""
2. Extract a substring form character "Q" and ends at "b"
Input: city = "ETLQALabs"
Expected O/P : QAlab  """

city = "ETLQALabs"

city1 = city[0:3]
city2 = city[3:5]
city3 = city[5:8].lower()

city = city2+city3
print(city)




"""3. Write a python code to check if the given list contains duplicate elements and print yes 
or no as per input
e.g. 
list1 =[1,2,3,4,3] => Yes
list2 =[1,2,3,4] => No """


def check_duplicates(input_list):
    if len(input_list) != len(set(input_list)):
        print("Yes")
    else:
        print("No")

list1 = [1, 2, 3, 4, 3]  # Contains duplicates
list2 = [1, 2, 3, 4, 5]     # No duplicates

check_duplicates(list1)  # Output: Yes
check_duplicates(list2)  # Output: No

"""
4. How would you use slicing to create a new list containing only the odd-indexed elements of a 
given list?
Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected output : [1, 3, 5, 7, 9] """


list_out = [ ]
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list:
    if i !=0 and i%2 != 0:
        list_out.append(i)
print("odd-indexed elements", list_out)

#-----------------OR-----------------
print("----------OR-----------")
Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output : [1, 3, 5, 7, 9]
list=[0,1,2,3,4,5,6,7,8,9]
list2=list[1:10:2]
print(f"The new list is: {list2}")

""" 5. How would you use slicing to create a new list containing only the even-indexed elements of a 
given list?
Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected output : [0, 2, 4, 6, 8] """


list_out1 = [ ]
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for e in list1:
    if e == 0 or e % 2 == 0:
        list_out1.append(e)
print("even-indexed elements", list_out1)

# ---------------OR ------------
print("----------OR-----------")
Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output : [0, 2, 4, 6, 8]

list=[0,1,2,3,4,5,6,7,8,9]
even_List=list[0:10:2]
print(f"even-indexed elements of the given list {list} is: {even_List}")