import re

text = "Aşağıdaki örnek, 50 öğe kapasitesine sahip bir ArrayList oluşturur. Daha sonra ArrayList'e dört öğe eklenir."

# 4 harften fazla olan kelimeleri bulma
matches = re.findall(r'\b\w{5,}\b', text)

# Bulunan kelimeleri ekrana yazdırma
for match in matches:
    print(match)
