import re

text = "Aşağıdaki örnek, 50 öğe kapasitesine sahip bir ArrayList  oluşturur. Daha sonra ArrayList'e dört öğe eklenir.1 2 3 6 "

# Cümledeki sayıları ve konumlarını bulma
matches = re.findall(r'\b\d+\b', text)

for i, number in enumerate(matches, start=1):
    print(f"{i}. sayı: {number}")

# Çıktı: 1. sayı: 50, 2. sayı: 1 ...
