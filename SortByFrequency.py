from collections import Counter
s = input('Enter string:')
c = Counter(s)
res = ''
freq = ['' for i in range(max(c.values())+ 1)]
for ch in c:
    freq[c[ch]] += c[ch] * ch
for j in range(len(freq)-1, -1, -1):
    res += freq[j]
print(res)
