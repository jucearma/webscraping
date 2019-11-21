from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.python.org/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")
    if res.title is None:
        print("Tag not found")
    else:
        print(res.title)

    tags = res.findAll("h2", {"class": "widget-title"})
    #Para filtrar una lista de etiquetas, reemplaza la línea resaltada del ejemplo anterior con la siguiente línea:
    tags = res.findAll("span", "a" "img")
    #Extraer etiquetas que tengan estas clases:
    tags = res.findAll("a", {"class": ["url", "readmorebtn"]})
    #Filtrar el contenido en función del texto interno, utilizando el argumento text de esta manera:
    tags = res.findAll(text="Python Programming Basics with Examples")

    for tag in tags:
        print(tag.getText())
