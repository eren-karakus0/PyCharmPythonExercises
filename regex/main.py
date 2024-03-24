import re

pattern = r"python"
text = "Python programlama dilinde Python regex kullanmak eğlencelidir."

result = re.search(pattern, text)
if result:
    print("Eşleşme bulundu:", result.group())
else:
    print("Eşleşme bulunamadı.")
