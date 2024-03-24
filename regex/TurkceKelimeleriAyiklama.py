import re

text = "Python programlama dili ile düzenli ifadeler (regex) kullanmak eğlencelidir."

turkish_words = re.findall(r"\b[ğüşıöçĞÜŞİÖÇa-zA-Z]+\b", text)

print("Türkçe kelimeler:", turkish_words)
