def search_knowledge(text):
    text = text.lower()

    # 💻 ICT / COMPUTING
    if "what is python" in text:
        return "Python is a programming language used for building apps, games, websites, and AI systems."

    if "what is computer" in text:
        return "A computer is an electronic device that processes data and performs tasks."

    if "what is ai" in text:
        return "AI (Artificial Intelligence) is technology that allows machines to think, learn, and make decisions."

    if "what is internet" in text:
        return "The internet is a global network that connects computers worldwide."

    if "what is software" in text:
        return "Software is a set of instructions that tells a computer what to do."

    if "what is hardware" in text:
        return "Hardware is the physical parts of a computer like keyboard, mouse, and screen."

    # 🔬 SCIENCE BASIC
    if "what is water" in text:
        return "Water is a liquid made of hydrogen and oxygen (H2O) and is essential for life."

    if "what is photosynthesis" in text:
        return "Photosynthesis is the process where plants make food using sunlight."
    
    if "founder biography" in text or "who is elvis" in text or "what is your founder biography" in text:
        return """Elvis is a young student from Ghana with a strong passion for technology, programming, and artificial intelligence. He enjoys learning Python, building software, and exploring how AI can solve real-world problems.

He is the founder of NovaCore AI, a project focused on creating an intelligent assistant that helps users learn, answer questions, and perform useful tasks through both web and desktop applications.

    return None
Elvis believes that learning never stops. His goal is to continue improving NovaCore AI into a powerful and innovative AI platform that can help people around the world.

Mission: To build intelligent technology that makes learning easier and inspires others to create amazing software."""
    return None
