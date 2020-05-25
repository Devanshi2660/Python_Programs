from collections import Counter
s = input('Enter string:')
c = Counter(s)
res = ''
for item in c.most_common(len(s)):
    res = res + item[0]*item[1]
print(res)

