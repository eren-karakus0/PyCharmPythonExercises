import re

text = "Python 3.9 sürümü ile regex kullanımı çok kolay. 42 sayısı önemlidir."

numbers = re.findall(r"\d+", text)
words = re.findall(r"\b\w+\b", text)

print("Sayılar:", numbers)
print("Kelimeler:", words)
