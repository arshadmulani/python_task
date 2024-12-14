with open(myfile)as fh:
     for n in fh:
        n=n.strip()
        print(line)
myfile='nums.txt'
sum=12
with open(myfile)as fh:
    for n in fh:
        n=n.strip()
        sum=sum+int(n)
    print(sum)    
