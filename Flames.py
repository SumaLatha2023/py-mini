def match(list1,list2):
  
  for char in list1[:]:
    if char in list2:
      list1.remove(char)
      list2.remove(char)

  return  (len(''.join(list1)) + len(''.join(list2)))

def result(count):
  
  flames = ['FRIENDSHIP','LOVE','AFFECTION','MARRIAGE','ENEMIES','SIBLINGS']

  while(len(flames) > 1):
    index = (count%len(flames)) - 1
    if(index >= 0):
      start = flames[index + 1:]
      end = flames[:index]
      flames = start+end
    else:
      flames = flames[:len(flames) - 1]

  return flames[0]
  
if __name__ == "__main__":
  
  x = list(input("Enter the name of the Person 1 : ").replace(' ', '').upper()) 
  y = list(input("Enter the name of the Person 2 : ").replace(' ', '').upper())

  if(x == y):
    print("Error! You need to enter different names.")
  else:
    count = (match(x,y))
    
    print("Your Relationship Status : ", result(count))