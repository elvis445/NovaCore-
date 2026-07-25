learned= {}

def learn(question,answer):
    learned[question] = answer

def ask(question):
    return learned.get(question)