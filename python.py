

lst = [5, 2, 8, 5, 7, 3, 9, 10, 6, 1,15]

dic = {}

for i in range(0,len(lst),2):
    try:
        dic[lst[i]] = [lst[i + 1]]
    except:
        dic[lst[i]] = 0

print(dic)
#

# lst = [5, 2, 8, 5, 7, 3, 9, 10, 6, 1,44]
# # d={lst[i]:lst[i+1] if lst[i+1:] else None for i in range(0, len(lst),2)}
# # print(d)
# for x in range(len(lst)):
#        for y in range(i+1, len(lst)):
#               if l[x]<l[y]:
#                      l[x],l[y]=l[y],l[x]
# print[lst[-2]]






# list1=[1,2,3,4,4,5,6,78,8,10,11]
# d1={}
# for x in range(0,len(list1),2):
#  if list1[x+1:]:
#      d1[list1[x]] = list1[x+1]
#  else:
#      d1[list1[x]]=None
#
# print(d1)

# d1={1: 2, 3: 4, 4: 5}
# d2={1: 9, 3: 8, 4: 0}
# d3={key:d1[key]+d2[key] for key,value in d1.items()}
# print(d3)


# for key in d1:
#     if key in d2:
#         d1[key]=d1[key]+d2[key]
#     else:
#         pass
# print(d1)



# for x,y in d1.items():
#     for i,j in d2.items():
#         if x==i:
#             d3[x]=d1[x]+d2[i]
# print(d3)

# class Student:
#    def __init__(self,name,rollno,marks):
#     self.name=name
#     self.rollno=rollno
#     self.marks=marks
#
#    def method(self):
#         print("Hello My Name is:",self.name)
#         print("My Rollno is:",self.rollno)
#    def method2(self):
#         print("My Marks are:", self.marks)
# c=Student('charan', 22, 55)
# c.method()
# c.method2()



#
# k=[1,2,3,4,5,6,7]
# d={}
# for x in range(0,len(k),2):
#     if k[x+1:]:
#       d[k[x]]=k[x+1]
#     else:
#         d[k[x]]=None
# print(d)
#
#
# # d={k[x]:k[x+1] for x in range(0,len(k),2)}
# # print(d)
#
#
#
#
list=[3,4,5,7,8,95,4]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
# print(list[-2])
# list=[8,2,5,6,7,3]x
# l=[]
# for x in range(len(list)):
#     for y in range(x+1, len(list)):
#         if list[x]+list[y]==10:
#             l.append([list[x],list[y]])
# print(l)

a = 'stranger'
# print(len(a))
# print(a[2])
# print(a[1:5])
# print(a[1:6:2])
print(a[1:-3])
print(a[::-2])






# print(a[-1])
# print(a[1])

# def func(ls):
#     for x in ls:
#         print(x**2,end=',')
# ls = [1,5,2,3,6]
# func(ls)

# ls = [1,2,7,2]
# s=list(map(lambda x:x*x,ls))
# print(s)
# print(sum(s))

# def func(*n):
#       return [x**2 for x in n]
# print(func(2,3,4,5))


s='abc'
res_lst = []
for x in range(0, len(s), 2):
    if s[x + 1:]:
        res_lst.append(s[x] + s[x + 1])
    else:
        res_lst.append(s[x] + '_')
print(res_lst)



# l=[[1,2],[3,4]]
# l1=[]
# l2=[]
# for x in l:
#     l1.append(x[0])
#     l2.append(x[1])
# print(l1)
# print(l2)



f=[3,3,5,7,8,9]
k=[]
o=[]
for x, y in enumerate(f):
    if x % 2 == 0:
        k.append(f[x])
    else:
        o.append(f[x])

print(k)
print(o)








l3=[1,2,3,4,5,6,7]
d={}
for x in range(0,len(l3),2):
    try:
     d[l3[x]]=l3[x+1]
    except:
     d[l3[x]]=None
print(d)

# maximum value
j=[0,4,34,55,5,6,9]
# print(max(j))
# for i in range(len(j)):
#   for f in range(i+1,len(j)):
#       if j[i]>j[f]:
#           j[i],j[f]=j[f],j[i]
# print(j)
# print(j[-2])

k=[3,4,5,6,89,0]
h=k[0]
for i in k:
    if i>h:
        h=i
print(h)

def art(val, list=[4,5,8]):
    list.append(val)
    return list


list12 = art(10)
# list2 = art(123, [])
# list3 = art('a')
print("list12 = " , list12)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)





























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































