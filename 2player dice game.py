from sys import exit
import random
import time



#setting range of numbers for the die

min = 1 
max = 6 


player = 0
computer = 0

print
player_name = input ("Please enter your name: ")
Cap = player_name.upper()

roll_again = "yes"

while roll_again == "yes": 
   if roll_again == "no":
      exit(0)
   print
   print ("Your Turn")
   print
   time.sleep(1)
   print ("Rolling the die...")
      
   time.sleep (2)

   player = random.randint(min, max)
   computer = random.randint(min, max)
 
   def dice (m):
     if m == 1:
      print (""" 
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  """)
         
     elif m == 2:
      print  ("""
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  """)
      
     elif m == 3:
      print ("""
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  """) 
    
     elif m == 4:
      print ("""
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  """) 
    
    
     elif m == 5:
      print (""" 
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  """)
    
    
     elif m == 6:
      print ("""   
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  """) 
   

   dice (player)
   
   print
   time.sleep(1)
   print
   print ("Computer's Turn")
   time.sleep(1)
   print
   print ("Rolling the die")
   time.sleep(2)
    
   dice(computer)
   
   time.sleep(1)
   
   
   # condition of win, loss, draw
   
   
   if player == computer:
      print
      print ("It's a draw!")
      time.sleep(1)
      print
      print
      
   elif player > computer:
      print
      print ("Congrats! You Win"), Cap
      time.sleep(1)
      print 
      print
      
   elif player < computer:
      print
      print ("You Lost. Try again"), Cap
      time.sleep(1)
      print  
      print
     
   roll_again = input("Roll the die again? yes or no: ")
   
