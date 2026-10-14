import re
text="aalie scored 95 in her first test and 88 in her second test"
m=re.search(r"\d",text)
print(m.group())
print(m.start(),m.end())
NUMS=re.findall(r"\d",text)
print(NUMS)