def show_menu():
    print('1. Ask questions')
    print('2. Add a question')
    print('3. Exit game')
    
    option = input('Enter option:')
    return option
    
    
# ---- Ask Question function    

def ask_question():
    questions =[]
    answers = []
    
    with open('questions.txt', 'r') as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)

    score = 0
            
    for question, answer in questions_and_answers:
        guess = input(question + '>')
        if guess == answer:
            score += 1
            print('correct!')    
            print('score: {0}' .format(score))
        else:
            print('wrong!')

    print('You got {0} correct out of {1}' .format(score, number_of_questions))    

    
#----- Add Question function
#  Then I will need to call this function in the game_loop funciton at option 2. at add question. 
def add_question():
    print('')
    question = input('Enter a question\n')
    
    print('')
    print('Ok then, tell me the answer')
    answer = input('{0}\n' .format(question))
    
    file = open('questions.txt', 'a')
    file.write(question + '\n')
    file.write(answer + '\n')
    file.close()

def game_loop():
    while True: # This means loop forever until a break
        option = show_menu()
        if option == '1':
            print('You selected "Ask questions"')
            ask_question() # This one from the funciton above. To review quesitons. 
        elif option == '2':
            print('You selected "Add a question"')
            add_question() # This comes from the function above. 
        elif option == '3':
            print('You selected "Exit game"')
            break
        else:
            print('Invalid option')
        print('')    # This blank line is to make things look a little bit nicer. 
        
game_loop()        
    
# print(show_menu())   