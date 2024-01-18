#import logo from art
from art import logo, vs
from game_data import data
import random 
# from replit import clear

#creating definition for format data
def format_data(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"


#print higher lower logo
score = 0
second_data = random.choice(data)
game_should_continue = True

while game_should_continue:

  #pick the random data from game_data as computer choosen
  first_data = second_data
  second_data = random.choice(data)
  print(f"compare A: {format_data(first_data)}")
  
  #print vs logo
  print(vs)
  
  #pick the random data from game_data as user choosen with 
  #input() who has more followers A or B :
  #make them as lower case
  print(f"compare B: {format_data(second_data)}")
  
  if first_data == second_data:
    second_data = random.choice(data)
  
  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  # if user_choosen == "a":
  #   if first_data['follower_count'] > second_data['follower_count']:
  #     print("you guessed correctly")
  #   else:
  #     if first_data['follower_count'] < second_data['follower_count']:
  #       clear()
  #       print(logo)
  #       print("you guessed wrong")
      
  # else: 
  #   if user_choosen == "b":
  #     if first_data['follower_count'] < second_data['follower_count']:
  #       print("you guessed correctly")
  #     else:
  #       if first_data['follower_count'] > second_data['follower_count']:
  #         clear()
  #         print(logo)
  #         print("you guessed wrong")
    
  
  def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
      return guess == "a"
    else:
      return guess == "b"

  # clear()  
  print(logo)

  
  
  first_data_followers = first_data["follower_count"]
  second_data_followers = second_data["follower_count"]
  is_correct = check_answer(user_guess, first_data_followers, second_data_followers)
  
  
  if is_correct:
    score += 1
    print(f"you guessed correctly. Your Current Score {score}")
  else:
    game_should_continue = False
    print(f"you guessed wrong. Your final score: {score}")


#print higher lower logo
#if user chooses wrong answer print message wrong answer and add the final score {final score}

#print higher lower logo 
#if user is right then print message right answer and add the current score {current score}
#next pick another random data computer choosen
#print vs logo
#pick the random data from game_data as user choosen 
#asks the user to choose A or B


#if user guess right then continues until user guess is wrong 
#starts compaing the question from the correct answer 
#if user answer is right the question asked to user is going to compare as computer choosen and it is compare to another question as user choosen



# Output:
compare A: Miley Cyrus, a Musician and actress, from United States

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

compare B: Billie Eilish, a Musician, from United States
Who has more followers? Type 'A' or 'B': a

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

you guessed correctly. Your Current Score 1
compare A: Billie Eilish, a Musician, from United States

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

compare B: Jennifer Lopez, a Musician and actress, from United States
Who has more followers? Type 'A' or 'B': b

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

you guessed correctly. Your Current Score 2
compare A: Jennifer Lopez, a Musician and actress, from United States

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

compare B: Virat Kohli, a Cricketer, from India
Who has more followers? Type 'A' or 'B': b

    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

you guessed wrong. Your final score: 2
