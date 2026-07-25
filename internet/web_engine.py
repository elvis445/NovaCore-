import requests
import webbrowser


def internet_status():
    try:
        requests.get("https://google.com",
                     timeout=5)
        return True
    except:
        return False


def check_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return "Internet connection is  working."
    except:
        return {"No internet connection"}


def search_google(query):

    webbrowser.open("https://www.google.com/search?q="+query)


def open_website(site):
    webbrowser.open("https://"+site)

def quick_info(query):
    """
    Simple online info fech(basic AI improvement)
    """
    try:
        url=f"https//en.wikipidea.org/api/rest_v1/page/summary/{query}"
        response = requests.get(url)

        if response.status_code==200:
            data = response.json
            return data.get("extract","I couldn't find information")
        else:
            return"No info found online."
    except:
        return"Internet error"        