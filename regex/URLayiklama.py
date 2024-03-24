import re

text = "Ziyaret ettiğimiz web sitesi: http://www.example.com. Başka bir site: https://www.python.org"

urls = re.findall(r"https?://\S+", text)

print("URL'ler:", urls)
