from unicodedata import category
import requests
import time

def question():
    difficultyLevel = input("What difficulty? [lower case letters only]  ")
    #if difficultyLevel != 'easy' or difficultyLevel != 'medium' or difficultyLevel != 'hard':
    #    print('Difficulty not available')
    categoryDict = requests.get('https://opentdb.com/api_category.php').json()
    for i in range(24):
        categoryName = categoryDict["trivia_categories"][i]['name']
        categoryId = categoryDict["trivia_categories"][i]['id']
        print(str(categoryName) + ' - ' + str(categoryId))
    response = requests.get('https://opentdb.com/api.php?amount=10&difficulty='+ difficultyLevel +'&type=multiple')
    q = response.json()
    for i in range(10):
        questio = q['results'][i]['question'].replace('&quot;', '\"')
        questio = questio.replace('&#039;', '\'')

        time.sleep(1)
        if i == 9:
            print("Last question!  ")
        print(questio)
        answer(q, i)


def answer(q, i):
    correctAnswer = 0
    answer = input('Your answer: ')
    if answer == q['results'][i]['correct_answer']:
        print("Correct answer!")
        correctAnswer += 1
    else:
        print("Incorrect answer!")
        print('The correct answer is ' + q['results'][i]['correct_answer'])
    print(str(correctAnswer) + '/' + str(i+1))
question()
