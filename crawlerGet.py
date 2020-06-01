from urllib.request import Request, urlopen

url = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go'
req = Request(url, headers={'User-Agent': 'XYZ/3.0'})


content = str(urlopen(req, timeout=20).read())
find = '"min-temp-1">'
posicao = int(content.index(find) + len(find))
minima = content[posicao : posicao + 2]

print("Mínima: " + minima)