from unicodedata import category
import requests
import time

class Player:

    def __init__(self):
        self.correctAnswer = 0

    def question(self):
        difficultyLevel = input("What difficulty? [lower case letters only]  ")
        questionAmount = int(input("How many questions do you want?  "))
        while questionAmount < 1 or questionAmount > 50:
            questionAmount = int(input("How many questions do you want?  "))
            
        #if difficultyLevel != 'easy' or difficultyLevel != 'medium' or difficultyLevel != 'hard':
        #    print('Difficulty not available')
        categoryDict = requests.get('https://opentdb.com/api_category.php').json()
        for i in range(24):
            categoryName = categoryDict["trivia_categories"][i]['name']
            categoryId = categoryDict["trivia_categories"][i]['id']
            if categoryId in [10, 13, 14, 18, 20, 25, 26, 28, 29, 30, 31, 32]:
                continue
            print(str(categoryName) + ' - ' + str(categoryId))
        categoryChoice = input("What category do you want to choose?  ")

        response = requests.get('https://opentdb.com/api.php?amount=' + str(questionAmount) + '&category=' + categoryChoice + '&difficulty=' + difficultyLevel + '&type=multiple')
        q = response.json()
        for i in q['results']:
            questio = i['question'].replace('&quot;', '\"').replace('&#039;', '\'')

            time.sleep(1)
            if i == 9:
                print("Last question!  ")
            print(questio)
            self.answer(q, i)

    choices = i['incorrect_answer']
    choices = choices.append(i['correct_answer'])


    def answer(self, q, i):
        answer = input('Your answer: ')
        if answer == i['correct_answer']:
            print("Correct answer!")
            self.correctAnswer += 1
        else:
            print("Incorrect answer!")
            print('The correct answer is ' + i['correct_answer'])
        print(str(self.correctAnswer) + '/10')

player_1 = Player()
player_1.question()