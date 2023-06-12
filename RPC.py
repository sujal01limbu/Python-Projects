import random
while True:
    y = input("Enter choice:")
    if (y == 'rock' or y == 'paper' or y == 'scissor'):
        
        break
    else:
         y = input("Enter choice:")

computer = ['rock','paper','scissor']
x =  random.choice(computer)
print("Computer choice:",x)


if (x == 'rock' and y == 'scissor'):
      print('result =You Lose!')

elif (x == 'rock' and y == 'paper'):
      print('result = You Win:)') 

elif (x == 'paper' and y == 'rock'): 
      print('result = You Lose!')     

elif (x == 'paper' and y == 'scissor'):     
     print('result = You Win:)') 

elif (x == 'scissor' and y == 'paper'):  
     print('result = You Lose!')

elif (x == 'scissor' and y == 'rock'): 
     print('result = You Win:)')   
else:
     print('result = You Draw!')        