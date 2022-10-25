from art import logo
from replit import clear
import random

def hot_cold():
  the_number = random.randint(1, 100)
  guesses_number = 0
  
  clear()
  print(logo)
  
  difficulty = input("Choose difficulty mode:\nEasy ≧◉ᴥ◉≦\n\nHard (ง︡'-'︠)ง\n\nInsane (҂◡̀_◡́)ᕤ\n").lower()
  if difficulty == "easy":
    guesses_number = 10
  elif difficulty == "hard":
    guesses_number = 6
  elif difficulty == "insane":
    guesses_number = 3
  else:
    print("Invalid Info!")

  end_of_game = False
  while guesses_number > 0 and end_of_game == False:
    print(f"You have {guesses_number} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > 100 or guess < 1:
      print("Invalid Info!")
    elif guess == the_number:
      print("You got it right 💪 (`▿´) 👊")
      end_of_game = True
    elif abs(guess - the_number) <= 5:
      print("Too hot 🔥")
      guesses_number -= 1
    elif abs(guess - the_number) <= 10:
      print("Hot 🌞")
      guesses_number -= 1
    elif abs(guess - the_number) <= 30:
      print("Cold ❄")
      guesses_number -= 1
    else:
      print("Too cold ⛄")
      guesses_number -= 1
 
  if guesses_number == 0:
    print("You're out of attempts. You lose ಥ_ಥ")
    print(f"And btw, the number is {the_number}\nGood luck next time")
  
  again = input("Do you wanna play another game of 'Hot / cold'? ツ\nType 'y' or 'n': ")
  if again == 'y':
    hot_cold()
  elif again == 'n':
    print("Understandable. Have a great day ╍●‿●╍")
  else:
    print("Invalid info!")
  
  
def instructions():
  clear()
  print(logo)
  input("Press 'Enter' to read the instructions one by one")
  input("\nIn this game, I will think of a random number between 1 and 100, and it's your job to try and guess this number (>‿◠)✌")
  input("\nEach time you give me a guess, I will give you one hint regarding how far/close your guess is from the actual number")
  input("\n'Too Hot' means that your guess is higher or lower than the actual number by 5 or less\n'Hot' means that your guess is higher or lower than the actual number by 10 or less\n'Cold' means that your guess is higher or lower than the actual number by 11-30\n'Too Cold' means that your guess is higher or lower than the actual number by more than 30")
  input("\nYou can choose between three difficulty modes:\nIn 'Easy Mode' you've got 10 attempts to guess the number\nIn 'Hard Mode' you've got 6 attempts to guess the number\nIn 'Insane Mode' you've got 3 attempts to guess the number ᕙ(`▿´)ᕗ")
  input("\nNow if you're ready, press 'Enter' to start the game.\nGood luck (̶◉͛‿◉̶)")
  hot_cold()


print(logo)
print("Welcome to 'Hot / cold' game ^-^")
start = input("Type '1' to play the game, or type '2' to read the game instructions: ")
if start == "1":
  hot_cold()
elif start == "2":
  instructions()
else:
  print("Invalid info *_*")