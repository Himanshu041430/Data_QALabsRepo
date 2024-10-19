# Assignments
# 1. Write a function to return the grade based on percentage

def gradpercentage(marks):
    if marks > 79:
        print("Grad : A+")
    elif marks > 69 or marks > 79:
        print("Grad : A")
    elif marks >49 or marks > 69:
        print("Grad : B")
    elif marks >35 or marks > 49:
        print("Grad : c")
    else:
        print("Fail")

gradpercentage(79.5)


# 2. Write a function that return a list of common elements from two different sets
def common_elements(set1, set2):
    # Use the intersection operation to find common elements
    common = set1.intersection(set2)
    # Convert the resulting set to a list and return
    return list(common)

# Example usage:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = common_elements(set1, set2)
print("Common elements:", result)

#----------second way----
print("-------second way----without intersection ----"  )

def common_elements(set1, set2):
    # Iterate through each element in set1 and check if it's in set2
    common = [element for element in set1 if element in set2]
    return common

# Example usage:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = common_elements(set1, set2)
print("Common elements:", result)

# Convert a String to a List of Character

s1 = "The Better India News is an Indian digital media platform focused on positive stories"

words = s1.split()

print(words)

#-------same---

string = "Hello "
char_list = list(string)
print(char_list)

# 4. Write a function to check if list contains any duplicate element and return True or False as applicable
def has_duplicates(input_list):
    # Create an empty set to keep track of seen elements
    seen_elements = set()

    # Iterate over each element in the list
    for element in input_list:
        # If the element is already in the set, it's a duplicate
        if element in seen_elements:
            return True
        # Otherwise, add the element to the set
        seen_elements.add(element)

    # If no duplicates were found, return False
    return False

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 2]

print(has_duplicates(list1))  # Output: False (No duplicates)
print(has_duplicates(list2))  # Output: True (Duplicates present)
"""
5. Given a list, write a function that provide the occurrence of element against each element in 
the list.
e.g. List = [1,2,3,4,5,1,3] 
Expected Output: 
1:2
2:1
3:2
4:1
5:1
"""
def element_occurrences(input_list):
    occurrence_dict = {}
    for element in input_list:
        if element in occurrence_dict:
            occurrence_dict[element] += 1
        else:
            occurrence_dict[element] = 1
    return occurrence_dict

# Example usage
input_list = [1, 2, 3, 4, 5, 1, 3]
occurrences = element_occurrences(input_list)

# Printing the output in the desired format
for element, count in occurrences.items():
    print(f"{element}:{count}")

#----------Same 5-------------
print("--------------Same 5-----------------------")
List = [1,2,3,4,5,1,3]

def ele_occurrences(List):
    counts = {}

    for num in List:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

List = [1,2,3,4,5,1,3]
result = ele_occurrences(List)
print("first Type Result: ", result)

print("Second Type Result: ")

for num,count in  result.items():
    print(f"{num}:{count}")
"""
6. Write a function return a substring where it starts from 2rd occurrence of ‘a’ and end at occurrent of ‘b’
e.g. s = "abracadabra"
start_char = 'a' 
end_char = 'b'
Expected output: acadab 
"""

def substring_between_chars(s, start_char, end_char):
    # Find the index of the 2nd occurrence of start_char
    start_index = -1
    occurrence_count = 0
    for index, char in enumerate(s):
        if char == start_char:
            occurrence_count += 1
            if occurrence_count == 2:
                start_index = index
                break

    # If the start_char does not occur twice, return an empty string
    if start_index == -1:
        return ""

    # Find the index of the first occurrence of end_char after start_index
    end_index = s.find(end_char, start_index)

    # If end_char is not found, return an empty string
    if end_index == -1:
        return ""

    # Return the substring from start_index to end_index (inclusive)
    return s[start_index:end_index + 1]


# Example usage
s = "abracadabra"
start_char = 'a'
end_char = 'b'
result = substring_between_chars(s, start_char, end_char)
print(result)  # Output: acadab
