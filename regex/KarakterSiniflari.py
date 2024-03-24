import re

pattern = r"[aeioup .]"
text = "Python programlama dilinde regex kullanmak eğlencelidir."

result = re.findall(pattern, text)
print("Vokaller:", result)
