import random

x = random.choice(range(0,100))


Guess = 0

while True:
    Guess+=1
    y = int(input("Guess the number:"))
    if (x < y):
        print("You guessed high 🙁")
    elif (x > y):
        print("You guessed Low 🙁")
    else:
       x = print(f"You guessed correct in {Guess} times 🙂")
       break    
   
    

        
    
      

