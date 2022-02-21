from unicodedata import category
import requests
import time
import random

class Player:

    def __init__(self):
        self.correctAnswer = 0
        self.questionCount = 0

    def question(self, difficultyLevel, questionAmount, categoryChoice):           
        response = requests.get('https://opentdb.com/api.php?amount=' + str(questionAmount) + '&category=' + str(categoryChoice) + '&difficulty=' + difficultyLevel + '&type=multiple')
        q = response.json()
        for i in q['results']:
            questio = i['question'].replace('&quot;', '\"').replace('&#039;', '\'')

            time.sleep(.5)
            if i == (questionAmount - 1):
                print("Last question!  ")
            print(questio)
            time.sleep(1)
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

class Bot():
    def __init__(self):
        self.correctAnswer = 0
        self.questionCount = 0

    def question(self, difficultyLevel, questionAmount, categoryChoice):           
        response = requests.get('https://opentdb.com/api.php?amount=' + str(questionAmount) + '&category=' + str(categoryChoice) + '&difficulty=' + difficultyLevel + '&type=multiple')
        q = response.json()
        print('The bots turn')
        time.sleep(0.2)
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

            self.randomGuessing(i, choices)

    def randomGuessing(self, i, choices):
        guess = random.randint(1,4)
        if choices[(guess-1)] == i['correct_answer']:
            self.correctAnswer += 1
            self.questionCount += 1
            print("The bot answered: " + choices[(guess-1)])
            print('The bot got the question right')
        else:
            print("The bot answered: " + choices[(guess-1)])
            time.sleep(1.6)
            print('The bot got the question wrong')
            time.sleep(1.6)
            print('The correct answer is ' + i['correct_answer'])
            self.questionCount += 1
            time.sleep(1.6)
        print(str(self.correctAnswer) + '/' + str(self.questionCount))

player_1 = Player()
bot_1 = Bot()

def main():
    difficultyLevel = input("What difficulty? [lower case letters only]  ")
    questionAmount = int(input("How many questions do you want?  "))
    
    categoryDict = requests.get('https://opentdb.com/api_category.php').json()
    for i in range(24):
        categoryName = categoryDict["trivia_categories"][i]['name']
        categoryId = categoryDict["trivia_categories"][i]['id']
        if categoryId in [10, 13, 14, 18, 20, 25, 26, 28, 29, 30, 31, 32]:
            continue
        print(str(categoryName) + ' - ' + str(categoryId))
        time.sleep(0.3)
    categoryChoice = int(input("What category do you want to choose?  "))
    while questionAmount < 1 or questionAmount > 50:
        questionAmount = int(input("How many questions do you want?  "))
    
    player_1.question(difficultyLevel, questionAmount, categoryChoice)
    bot_1.question(difficultyLevel, questionAmount, categoryChoice)
    if bot_1.correctAnswer > player_1.correctAnswer:
        print("The bot won and got " + str(bot_1.correctAnswer) + "/" + str(bot_1.questionCount) + " while you got " + str(player_1.correctAnswer) + "/" + str(player_1.questionCount))
    elif player_1.correctAnswer > bot_1.correctAnswer:
        print("You won and got " + str(player_1.correctAnswer) + "/" + str(player_1.questionCount) + " while the bot got " + str(bot_1.correctAnswer) + "/" + str(bot_1.questionCount))
    elif player_1.correctAnswer == bot_1.correctAnswer:
        print("You drew with the bot, both got " + str(player_1.correctAnswer) + "/" + str(player_1.questionCount))
main()
