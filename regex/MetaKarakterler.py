import re

pattern = r"^Python"
text = "Python programlama dilinde Python regex kullanmak eğlencelidir."

result = re.search(pattern, text)
if result:
    print("İfade başlangıcı bulundu.")
else:
    print("İfade başlangıcı bulunamadı.")
