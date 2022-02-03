import requests

def question():
    difficulty = input("What difficulty?  ")
    response = requests.get('https://opentdb.com/api.php?amount=10&difficulty='+ difficulty +'&type=multiple')
    q = response.json()
    for i in range(10):
        questio = q['results'][i]['question'].replace('&quot;', '\"')
        questio = questio.replace('&#039;', '\'')
        print(questio)
        if i == 10:
            print("Last question!  ")
        answer(q, i)


def answer(q, i):
    r_answer = 0
    answer = input('')
    if answer == q['results'][i]['correct_answer']:
        print("Right answer!")
        r_answer += 1
    else:
        print("Wrong!")
        print(q['results'][i]['correct_answer'])
question()