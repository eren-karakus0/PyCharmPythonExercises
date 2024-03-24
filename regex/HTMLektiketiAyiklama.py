import re

html_text = "<p>Python, <b>programlama</b> dilidir.</p> <a href='http://www.example.com'>Example</a>"

tags = re.findall(r"<[^>]+>", html_text)
print("HTML Etiketleri:", tags)
