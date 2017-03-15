s="['2','3','4']"
s=s.strip('[')
s=s.strip(']')
print(s)
s=s.strip("'")
print(s)
print(int(s.split("','")[0]))