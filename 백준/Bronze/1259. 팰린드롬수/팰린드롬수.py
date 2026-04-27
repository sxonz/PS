boolean = []
while True:
  sum = list(input())
  if sum == ['0']: break
  if sum == list(reversed(sum)):boolean.append('yes')
  else:boolean.append('no')
for i in boolean:
  print(i)