import math
import re

pattern = r"[a-z]+rem"

text = '''
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of lorem type and scrambled it to make a type specimen book.lorem Ipsum survived not only five enturies, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
'''

# match = re.search(pattern,text)

matches = re.finditer(pattern,text)

for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])    
print(match)