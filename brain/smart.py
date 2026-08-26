

def smart_reply(user): 
    user = user.lower().strip()

    if user in ['hi',"hello","hey"]:
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
        
    if "thank" in user:
        return "You'r welcome!"
        
    if "founder of NovaCore AI biography" in text or "who is Elvis Sedem Brown" in text or "what is your founder biography" in text:
        return """Elvis is a young student from Ghana with a strong passion for technology, programming, and artificial intelligence. He enjoys learning Python, building software, and exploring how AI can solve real-world problems.

He is the founder of NovaCore AI, a project focused on creating an intelligent assistant that helps users learn, answer questions, and perform useful tasks through both web and desktop applications.

    return None
Elvis believes that learning never stops. His goal is to continue improving NovaCore AI into a powerful and innovative AI platform that can help people around the world.

Mission: To build intelligent technology that makes learning easier and inspires others to create amazing software."""
    return None

  
