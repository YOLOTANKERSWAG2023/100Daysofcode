snumber= input("Type the secret number: ")
print(snumber+"\n")


foundNumber=False
guesses= 0
while foundNumber==False:
  
  
  
  guess= input("What is your guess?: ")
  
  guesses+=1
  
  if int(snumber)==int(guess):
    foundNumber=True 
    print()
    print("Correct!")
    print()
    if guesses==1:
      print("Took you",guesses,"time")
    else: print("Took you",guesses,"times")
  elif int(guess) > int(snumber):
   print('Too high',"\n")
  elif int(guess) <0:
    print(guess)
    exit()
  elif int(guess) < int(snumber):
    print('Too low',"\n")
  elif guess != int():
    print("guess niet gelijk aan int")
  

    
#if snumber

