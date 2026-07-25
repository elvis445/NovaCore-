#import pyautogui as pg
#import mouseinfo

#import pywhatkit
import wikipedia
import os
import sys
from brain.learning import learn, ask
from knowledge.knowledge import search_knowledge
from plugins.time_tools import get_time
from plugins.calculator import calculate
from engine.files import create_file, read_file, delete_file
from internet.web_engine import search_google, open_website, quick_info
from memory.memory import remember, recall, save_chat, load_chat
from brain.smart import smart_reply

def search_googhle(query):
    #Uses your inernet module instead of pywhatkit
    return"Searching Google...."



def play_vedio(topic):
    #A-safe return response for the cloud server
    return 'Playing vedio on YouTube'

def think(user):
    user = user.lower()

    if user.startswith("learn"):
        text = user.replace("learn", "")

        if "=" in text:

            question, answer = text.split("=", 1)

            learn(question.strip(), answer.strip())

            return "I learned something new!"

        saved = ask(user)
        if saved:
            return saved

        knowledge_response = search_knowledge(user)
        if knowledge_response is not None:
            return knowledge_response
        
    if user.startswith("wiki"):
        query=user.replace("wiki","")
        return wikipedia.summary(query,sentences=2)

    if user.startswith("create file"):
        filename = user.replace("create file", "")
        return create_file(filename)

    if user.startswith("read file"):
        filename = user.replace("read file", "")
        return read_file(filename)

    if user.startswith("delete file"):
        filename = user.replace("delete file", "")
        return delete_file(filename)

    if user.startswith("search"):
        query = user.replace("search", "")
        search_google(query)
        return "Searching Google for"+query

    elif user.startswith("open website"):
        site = user.replace("open website", "")
        open_website(site)
        return "Opening"+site
    
    elif user.startswith("play "):
        topic=user.eplace("play","")
        return play_vedio(topic)

    if user.startswith("remember"):
        text = user.replace("remember", "").strip()

        if "is" in text:
            key, value = text.split(" is ", 1)
            remember(key.strip(), value.strip())
            return "Okay, I will remember that."
        else:
            return "Please use the format;remember [item] is [value]"

    elif user.startswith("what is"):
        key = user.replace("what is", "").replace("?", "").strip()
        return recall(key)

   
    elif user.startswith("calculate"):
        expression = user.replace("calculate", "")
        return calculate(expression)

    elif "time" in user:
        return "The time is"+get_time()
  

    elif "who is" in user or "what is" in user:
        cleaned = user.replace("who is", "")
        cleaned = cleaned.replace("what is", "").strip()
        if len(cleaned.split()) <= 3:
            return quick_info(cleaned)

    chat_history = load_chat

    for chat in chat_history[-10]:
        if user in chat['user']:
            return chat["bot"]

    return smart_reply(user)
