import random


def check_letters(word, letter):
    letter_positions = []
    for i in range(len(word)):
        if word[i] == letter:
            letter_positions.append(i)
    return letter_positions

def replace_dash(hang_word, index_list, letter):
    new_word = ""
    hang_word = list(hang_word)
    for i in index_list:
        hang_word[i] = letter
    for i in hang_word:
        new_word += i
    return new_word

def take_input():
    user_letter = input("Enter your guess >> ").lower()
    print("\n")
    return user_letter
    


def PlayHangman():
    with open("words.txt", "r") as fin:
        words = fin.readlines()
        correct_word = random.choice(words).strip()
        
        count = len(cord)
        tries = count+(len(correct_word)//2)
#number of tries is equal to 150% of length of the word because user uses up a try even if the guess is correct
        hold_tries = tries
        hang_word = "-"*count
        selected_letters = set()
        
        user_start = input(("Welcome to Hangman! \n" 
        "You have a specific number of tries to guess the hidden word.\nHowever, you can only guess one letter at a time. "
        "Enter 'Yes' to continue >> ")).capitalize()
        print("\n") #spacer
        
        
        if user_start == "Yes":
            while tries != 0:
                print("This is your word {}. It has {} letters. You have {} guesses to go. You have used these letters {}\n".format(hang_word, count, tries, selected_letters))
                user_letter = take_input()
                
                if len(user_letter) != 1:
                    print("Please enter a valid letter")
                    
                elif user_letter in selected_letters:
                    print("You have already selected this letter")
                    
                elif user_letter in correct_word:
                    tries -= 1
                    positions = check_letters(correct_word, user_letter)
                    hang_word = replace_dash(hang_word, positions, user_letter)
                    selected_letters.add(user_letter)
                    
                    #Check if complete word has been completely guessed properly
                    if hang_word == correct_word:
                        print("Congratulations!! You guessed {} right. It took you {} tries".format(hang_word, hold_tries - tries))
                        return 
                    else:
                        print("You guessed right! The word now looks like this {}\n".format(hang_word))
    
                    
                
                elif user_letter not in correct_word:
                    print("Wrong!")
                    tries -= 1
                    selected_letters.add(user_letter)
                    
                
            print("Sorry, you were unsuccessful. The right word was {}\n".format(correct_word))                                                                                                                             
                      

if __name__ == '__main__':
    PlayHangman()


    
    

        
    
    

        
    
    
#print(replace_dash("------", [5], "e"))




#print(check_letters("bob", "e"))
    
