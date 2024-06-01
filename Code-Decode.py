import random as r
import string as s

def letters():
  str = ''
  for i in range(3):
    str += r.choice(s.ascii_letters)
  return str

def coding(msg):
  words = msg.split(" ")
  nwords = []

  for word in words:
    if(len(word) >= 3):
      nword = letters()+ word[1:] + word[0] + letters() 
      nwords.append(nword)
    else:
      nwords.append(word[::-1])

  nmsg = " "
  print(nmsg.join(nwords)) 

def decoding(msg):
  words = msg.split(" ")
  nwords = []

  for word in words:
    if(len(word) >= 3):
      nword = word[-4] + word[3:-4]
      nwords.append(nword)
    else:
      nwords.append(word[::-1])

  nmsg = " "
  print(nmsg.join(nwords))  

def main():
  print("Transform Your Messages with Coding and Decoding Magic! \nSo, let's dive into the fun!! \n")
  
  while(True):
    choice = input("Enter 'C' for Coding or 'D' for Decoding : ")
    print()
    
    if choice == 'C':
      msg = input("Enter the message to be coded : \n")
      print("Your coded message is : ") 
      coding(msg)
    
    elif choice == 'D':
      msg = input("Enter the message to be decoded : \n")
      print("Your decoded message is : ") 
      decoding(msg)
  
    else:
      print("Incorrect Entry, Try Again ..")

    print()
    value = int(input("Enter 0 to Exit or 1 to Continue : "))
    if(value == 0):
      exit()

main()