import re

text=input()
result = re.findall(r'abb|abbb', text)
print(result)