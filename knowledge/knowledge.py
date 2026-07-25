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

    return None