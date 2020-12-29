# winning_number = 20

# print("This is gussing game")
# input_number =int(input("Guess your number between 1 to 100 : "))

# guess = 1
# game_over = False

# while not game_over:
#     if(winning_number == input_number):
#         print(f"You wined !!!, and you guess number in {guess} time ")
#         game_over = True
#     else:
#         if(winning_number > input_number):
#             print("Your have guess to low number!")
#             guess += 1
#             input_number = int(input("Guess again..."))
#         else:
#             print("you have Guess to high number")
#             guess += 1
#             input_number = int(input("Guess again..."))


# Win_Number = 18
# Number_of_guesses = 1
# print("-----------------Number of guesses is limit. you can choose 9 times-----------------------")
# while(Number_of_guesses <= 9):
#     guesses_number = int(input("Guess the number :"))
#     if(guesses_number < 18):
#         print("you entered less number, please try again")
#     elif(Number_of_guesses > 18):
#         print("you entered Greter number, please try again")
#     elif(guesses_number == Win_Number):
#         print("you won....!")
#         print(Number_of_guesses,"no. of guess he took to finish")
#     else:  
#         break
#     print(9-Number_of_guesses,"no. of guess left")
#     Number_of_guesses = Number_of_guesses + 1

# if(Number_of_guesses > 9):
#     print("Game Over")



# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
  




