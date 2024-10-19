
# print the elements from the string
s1 ="etlqa"

# Way 1
for ch in s1:
    print(ch)
#way 2
print("----------way 2-----------")
length = len(s1)   # number convert
print(length)
for idx in range(length):
    print(idx)     # number print
    print(idx,": ",s1[idx]) # idx - number print, s1[idx] charrector print

# way 3
print("----------way 3------------")
# s1 = "etlqa"
i = 0
length = len(s1) # 5
while (i < length):
    print(s1[i])
    i = i + 1

# How to revese the words in a string => WAY 1
print ("------How to revese the words in a string => WAY 1-----")

s1 ="etl qa labs"
# expetcted output : labs qa etl

l = s1.split()
# ['etl', 'qa', 'labs']
ans =""
length = len(l) -1 # 3-1 = 2
while length >=0:
    ans = ans + l[length]+" "  # 1st iteration  ans = ""+l[2] = labs
                               # 2nd iteration  ans = labs + l[1] = labs qa
                               # 3rd iteration  ans= labs qa + l[0] = labs qa etl
    length = length -1
print(ans)

# How to revese the words in a string => WAY 2

print("-----How to revese the words in a string => WAY 2-----")
s1 ="etl qa labs"
l = s1.split()
print(l)
# ['etl', 'qa', 'labs']
revlist = l[::-1]
revlist = l[::-1]
print(revlist," ",type(revlist))
print(" ".join(revlist)," ",type(revlist))

# How to sum the ascii values for the given string
# ASCII
s1 = "abc" # 65 + 25 = 90
sum = 0
for ch in s1:
    sum = sum +ord(ch)  # convert ascii value
print(sum)

s1 = "ETLQALABS"
# output => QALAB
startindex = s1.find('Q')
endtindex = s1.find('B')
ans = s1[startindex:endtindex+1:1]
print(ans)