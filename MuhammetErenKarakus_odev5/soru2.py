import re

text = "A^^şağıdaki örnek, 50 öğe kapasitesine sahip bir ArrayList oluşturur. Daha sonra ArrayList'e dört öğe eklenir."

# Boşlukları ve noktalama işaretlerini ":" ile değiştirme
modified_text = re.sub(r'[ \.,\']', ':', text)

print(modified_text)
