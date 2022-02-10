from unicodedata import category
import requests
import time
import random

class Player:

    def __init__(self):
        self.correctAnswer = 0
        self.questionCount = 0

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

            time.sleep(.5)
            if i == 9:
                print("Last question!  ")
            print(questio)

            choices = i['incorrect_answers']
            choices.append(i['correct_answer'])
            random.shuffle(choices)
            time.sleep(2.5)
            for n in range(4):
                time.sleep(.3)
                print(str(n+1) + '. ' + choices[n])

            self.answer(i, choices)


    def answer(self, i, choices):
        answer = int(input('Your answer: '))
        if choices[(answer-1)] == i['correct_answer']:
            print("Correct answer!")
            self.correctAnswer += 1
            self.questionCount += 1
        else:
            print("Incorrect answer!")
            print('The correct answer is ' + i['correct_answer'])
            self.questionCount += 1
        print(str(self.correctAnswer) + '/' + str(self.questionCount))

class Bot(Player):
    def __init__(self):
        self.correctAnswer = 0
        self.questionCount = 0

    def randomGuessing(self, i, correctAnswer, questionAnswer):
        guess = random.randint(1,4)
        if guess == i['correct_answer']:
            correctAnswer += 1
            questionAnswer += 1
            print('The bot got the question right')
        else:
            print('The bot got the question wrong')
            questionAnswer += 1

player_1 = Player()
player_1.question()
bot_1 = Bot()
bot_1.randomGuessing()