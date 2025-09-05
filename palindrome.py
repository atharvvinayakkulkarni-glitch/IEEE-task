s = input()
# segregating each word 
words = s.split()
ok=''
for j in words:
  for i in range(len(j)):
    ok=''
    # for as long as opposite letters in word is same ok is yes and whenever it fails ok is no and loop breaks
    if(j[i]==j[len(j)-1-i]):
     ok='yes'
    else:
     ok='no'
     break
  # if ok is yes word is palindrome and is printed
  if(ok=='yes'):
    print(j,end=' ')
