#l=[2,3,5,8]
#output
#[4,9,25,64]
#you have to find it out the number which one
#divisible by 5 in the range of 5 to 30
#word=['python','php',java','json','c']
#output -> ['java','json']

'''L= [2, 3, 5, 8]
output = [x**2 for x in L]
print(output)'''


'''output = [x for x in range(5, 31) if x % 5 == 0]
print(output)'''


words = ['python', 'php', 'java', 'json', 'c']

output = [x for x in words if x.startswith('j')]

print(output)
