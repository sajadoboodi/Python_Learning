import re

str = 'Iran is in the middle-east.'
result = re.findall(r'iran',str)
print(result)

str = 'i am born in 1973. i am 20 years old now.'
result = re.findall(r'(\d+)',str)
print(result)

str = 'students for passing the exam must have more than 15 grade.'
result = re.findall(r'a*',str)
print(result.count('a') + result.count(''))

str = 'This is an advanced Python programming in School.'
result = re.sub(r'maktabkhooneh','university',str)
print(result)