import re

file_names = ["document.txt", "image.jpg", "data.csv", "script.py", "README.md"]

pattern = r"\.txt$|\.md$"

text_files = [file for file in file_names if re.search(pattern, file)]
print("Metin dosyaları:", text_files)
