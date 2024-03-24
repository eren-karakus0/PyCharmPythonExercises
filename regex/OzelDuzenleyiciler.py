import re

pattern = r"\d+"
text = "Python 3.88 77 123 sürümü kullanıyorum."

result = re.findall(pattern, text)
print("Rakamlar:", result)
