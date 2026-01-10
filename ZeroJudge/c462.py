tlist = list(input().strip())
t2list = [t.isupper() for t in tlist]
for key, value in enumerate(t2list):
    t2list[key] = int(value)
print(t2list)
   
