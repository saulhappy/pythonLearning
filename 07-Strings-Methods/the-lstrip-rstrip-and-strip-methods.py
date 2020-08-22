text = "   here   is   some text           "

print(len(text))

print(len(text.rstrip()))
print(len(text.lstrip()))
print(len(text.strip()))

url = "www.iris.org"

print(url.rstrip(".org"))
print(url.strip("worg."))
print(url.lstrip("w."))
