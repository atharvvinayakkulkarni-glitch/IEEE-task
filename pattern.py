n=int(input())
for i in range(n):
  # printing spaces for inverted triangle
  for j in range(i,n-1):
      print(" ",end='')
    # printing triangle of asterisks
  for j in range(i+1):
      print('*',end='')
  print('')
