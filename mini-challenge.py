# TODAY'S CODING CHALLENGE:
# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# To print the result as a string as above:
sum = 0
firstTerm = True
string = ''
for list in [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]:
    if firstTerm:
        firstTerm = False
    else:
        string += ' + '
    string += '{}'.format(min(list))
    sum += min(list)
print('{} = {}'.format(string, sum))

# To just print the result:
sum = 0
for list in [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]:
    sum += min(list)
print(sum)
