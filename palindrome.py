s = input()
words = s.split()
ok=''
for j in words:
  for i in range(len(j)):
    ok=''
    if(j[i]==j[len(j)-1-i]):
     ok='yes'
    else:
     ok='no'
     break
  if(ok=='yes'):
    print(j,end=' ')
