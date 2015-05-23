str = 'X-DSPAM-Confidence: 0.8475'
colpos = str.find(':')
num = str[colpos+1: ]
num = num.lstrip()
num = float(num)
print num
