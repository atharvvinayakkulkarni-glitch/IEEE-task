# both my lists
list1=[2,3,5,7,6,3,2,9]
list2=[5,7,4,8,0,1,3]
list3=[]
for i in list1:
  if(i in list2):
  # if ith element of list 1 in 2 append to 3
    list3.append(i)
# set function to remove repeated values
list3=list(set(list3))
print(list3)
