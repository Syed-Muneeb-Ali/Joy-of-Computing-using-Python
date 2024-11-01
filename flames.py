import string

a = input('Enter 1st name: ')
a = a.lower()
a = a.replace(' ','')
b = input('Enter 2nd name: ')
b = b.lower()
b = b.replace(' ','')

a = ''.join(sorted(a))
b = ''.join(sorted(b))

i = 0
j = 0
count = 0
while(i<len(a) and j<len(b)):
    if(a[i] == b[j]):
        i += 1
        j += 1
        count += 1
    else:
        if(a[i] > b[j]):
            j += 1
        else:
            i += 1

steps = (len(a) + len(b) - 2*count)
flames = ['F','L','A','M','E','S']

while(len(flames) > 1):
    idx = 0
    for i in range(steps):
        idx += 1
        if(idx == len(flames)): idx = 0
    flames.pop(idx)
    # print(flames)

res = flames[0]

# FLAMES
if(res == 'F'): print('Friendship')
elif(res == 'L'): print('Love')
elif(res == 'A'): print('Affection')
elif(res == 'M'): print('Marriage')
elif(res == 'E'): print('Enemy')
else: print('Sex Buddy')
