import requests
from inscriptis import get_text
class Eel_Py:
    def register(name, link):
        requests.get(link + "/register" + "/" +  name + "/python")
    def deregister(index, link):
        requests.get(link + "/deregister" + "/" + index)
    def registered(link):
        r = requests.get(link)
        registered = []
        text = get_text(r.content)
        text_split = text.split()
        i = 0
        while i != len(text_split):
            registered.append([i[0], i[1]])
            i += 2
        return registered
            
        
