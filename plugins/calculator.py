def calculate(expression):
    try:
        allowed = "0123456789+-*/()."
        for char in expression:
            if char not in allowed:
                return "I can only calculate numbers and basic symbols"

        answer = eval(expression)
        return "Answer:"+str(answer)

    except Exception:
        return "Sorry,I couldn't calculate that."