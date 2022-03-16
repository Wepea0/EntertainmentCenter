import dbm
from tabulate import tabulate
db = dbm.open("High score", "c")

def PlayQuiz():
    def get_questions(all_info, category, no_questions):
        category_list = []
        for line in all_info:
            if line ==  category:
                select_index = all_info.index(line) + 1
                end = select_index + no_questions 
                for t in range(select_index, end):
                    category_list.append(all_info[t])
        return category_list

    def get_answers(all_info, category, no_questions):
        list1 = []
        final_answer_list = []
        for line in all_info:
            if line == category:
                get_index = all_info.index(line) + 1
                end = get_index + no_questions
                for t in range(get_index, end):
                    list1.append(all_info[t])
        for i in list1:
            final_answer_list.append(i.split(","))
        return final_answer_list
    
    def show_answers(answer_list, question_number):
        question_number -= 1
        letters = ["A", "B", "C", "D"]
        correct_answer = []
        i = 0
        for answer in answer_list[question_number]:
            if answer in letters:
                correct_answer.append(answer[i])
            else:
                print("{} -- {}".format(letters[i], answer))
                i += 1
            
        return correct_answer
#This functions prints out questions and checks if the user answer if correct
    def check_answer(category_questions, category_answers, number_of_questions):
        user_score = 0
        count = 1
        while count <= number_of_questions:
            print(category_questions[count - 1])
            answer = show_answers(category_answers, count)
            user_answer = input("What is the answer to this question [A, B, C, D] >> ")
            print(" ")
            
            if user_answer.upper() not in ("A", "B", "C", "D"):
                print("Please enter a valid answer")        
            elif user_answer.upper() == answer[0]:
                print("Yayy! Your answer is correct\n")
                count += 1
                user_score += 1
            else:
                print(f"Sorry. Your answer is incorrect. The correct answer is {answer[0]}\n")
                
                count += 1
        total = number_of_questions
        print("You got {} out of {}!!".format(user_score, total))
        if user_score == total:
            print("Brilliant work, you got a perfect score!!")
        elif float(user_score) > 0.8 * total:
            print("Well done!! You got a very good score")
        elif float(user_score) > 0.5 * total:
            print("Nice job. This was a decent attempt")
        elif float(user_score) < 0.5 * total:
            print("Hmm we know you can do better than that. Better luck next time!")
        print("\n")
        return user_score
            
    def take_input():
        valid_option = ["1", "2", "3"]
        category_list = ["placeholder", "Geography", "History", "Sports"]
        print("Welcome to the quiz! There are three categories you can choose from.")
        number_selection = input("Enter:\n1 for Geography \n2 for History\n3 for Sports \n >> ")
        while number_selection not in valid_option:
            print("\nPlease enter a valid category number")
            print("Welcome to the quiz! There are three categories you can choose from.")
            number_selection = input("Enter:\n1 for Geography \n2 for History\n3 for Sports \n >> ")
        user_category = category_list[int(number_selection)]
        print("\n")
        return user_category
   
#Used as the key for the sorting of scores and names in the high score database
    def sorting_logic(item):
        score = item[1]
        name = item[0]
        return (score, name)

    def high_score(name, user_score):
        final_dictionary = {}
        final_list = []
        db[str(name)] = str(user_score)
        db[str(name)] = str(user_score)
        print("The high scores are as follows.")
        for value in db.keys():
#Since db values are of the byte type the next few lines changes the types of the values and removes the byte signature 'b'
            final_name = str(value)
            final_name = final_name.strip("b") 
            final_score = int(db[value])
            final_dictionary[final_name] = final_score
#Next few lines sorts the dictionary with the highest scores first and uses tabulate to print the names and scores        
        sorted_final_dictionary = sorted(final_dictionary.items(), reverse = True, key = sorting_logic)
        for name_score in sorted_final_dictionary:
            final_list.append([name_score[0], name_score[1]])
        print(tabulate(final_list, headers = ["Name", "Score"]))
        db.close()
    
#Checks if the name a user enters already exists in the database                
    def CheckName(database, name):
        if name in database:
            return True
        

#Opens question file
    with open("Questions4.txt", "r", encoding="utf8") as f:
        a = f.readlines()
        for i in range(len(a)):
            a[i] = a[i].strip()
        
        user_name = input("Hello! Welcome to the Very Fun Quiz game. Please enter your preferred nickname >> ")
        while len(user_name) == 0:
            user_name = input("Hello! Please enter your preferred nickname >> ")
        while CheckName(db, user_name):
            user_name = input("Hello! Please enter a different nickname >> ")
            

        Geography_questions = get_questions(a, "Geography", 10)
        History_questions = get_questions(a, "History", 10)
        Sports_questions = get_questions(a, "Sports", 10)
        Geography_answers = get_answers(a, "Geography Answers", 10)
        History_answers = get_answers(a, "History Answers", 10)
        Sports_answers = get_answers(a, "Sports Answers", 10)
        
        
        user_category = take_input()
         
        if user_category == "Geography":
            print("Welcome to the Geography section. Best of luck!\n")
            user_score = check_answer(Geography_questions, Geography_answers, 10)
            
            
        if user_category == "History":
            print("Welcome to the History section. Best of luck!\n")
            user_score = check_answer(History_questions, History_answers, 10)
            
        if user_category == "Sports":
            print("Welcome to the Sports section. Best of luck!\n")
            user_score = check_answer(Sports_questions, Sports_answers, 10)
        
        
        high_score(user_name, user_score)
            
if __name__ == '__main__':
    PlayQuiz()
                      

