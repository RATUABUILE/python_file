# counting_o_letter
f=open("humpty.txt","r")
# m=f.write("\nit is impossible to lick your elbow")
m=f.read().split()
c=0
for i in m:
    a=list(i)
    for j in a:
        if j=="o":
            c=c+1
print(c)
f.close()