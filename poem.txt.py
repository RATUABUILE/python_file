# f=open("poem.txt","r")
# u=f.readline()
# print(u)
# f.close

# a=open("ratua.txt","r")
# l=a.read()
# c=0
# for i in l:
#     if i>="A" and i<="Z":
#         c=c+1
# print(c)
# a.close

# a=['a','B','C','d','O',"T"]
# i=0
# c=0
# while i<len(a):
#     if a[i]>="a" and a[i]<="z":
#         c=c+1
#     i+=1
# print(c)

# a=open("ratua.txt","r")
# l=a.read()
# c=0
# for i in l:
#     if i>="a" and i<="z":
#         c=c+1
# print(c)
# a.close

# n=int(input("enter any number:"))
# a,i,s=n,0,0
# while i<=n:
#     r=n%10
#     s=s+r
#     n=n//10
#     i+=1
# if a%s==0:
#     print("harshad")
# else:
#     print("not harshad")

# w="python"
# a=w[::-1]
# print(a)

# from pathlib import Path
# m= Path('ratua.txt').stat()
# r= Path('ratua.txt').stat().st_size
# print("File size- ", r)