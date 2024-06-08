import random as r
comp = r.randint(0,2)

def check(comp,user):
  if(comp == user):
    return 0
  if(comp == 0 and user == 1):
    return 1
  if(comp == 1 and user == 2):
    return 1
  if(comp == 2 and user == 1):
    return 1
  return -1

print('ROCK-PAPER-SCISSORS GAME')
print('\nRock = 0\nPaper = 1\nScissors = 2\n')
user = int(input("Enter your choice : "))

print('YOU : ',user)
print('COMPUTER : ',comp)

result = check(comp,user)
if(result == 0):
  print('Draw')
elif(result == 1):
  print('You WON')
else:
  print('You LOSE')
  