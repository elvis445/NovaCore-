

def smart_reply(user): 
    user = user.lower().strip()

    if "hello" in ['hi',"hello","hey"]:
        return "Hello! Nice to meet you today?  ."

    if "how are you" in user:
        return "I am doing well, thank you for asking."

    if "who are you" in user:
        return "My name is NovaCore,your personal AI assistance."

    if "who created you" in user:
        return "I was created by Elvis Sedem Brown."

    if "what can you do" in user:
        return "I can chat,answer quesions,speak, and I am improving every day."

    if "good night" in user:
        return "Good night.Sleep well and keep dreaming."

    if "goodbye" in user:
        return "Goodbye! See you next time"
    

    if "thank":
        return "You'r welcome!"
  
