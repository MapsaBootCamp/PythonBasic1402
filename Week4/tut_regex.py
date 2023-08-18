# regular expression ===> RegEx  ===> هر ریجکسی یه سری کارکتر که با استفاده از آن یه پترنی را در استرینگ می یابد.

import re
# * zero or more samte chapi
# + one or more samte chapi
# ? zero or one samte chapi
# MetaCharacters =====>  [] . ^ $ * + ? {} () \ |


sample_txt = "welghewlihgeiwlghe309121234563welehgliehgliewhg0912433293287847eihgjkewbgjb"
# print(re.findall(r"\D(09\d{9})\D", sample_txt))


sample_txt = "salam \n ashkan@test.com eihgewihgiewh gholam..mapsa.n@gmail.com"
email_pattern = r"((\w+\.?\w+)+@\w+\.[a-z]{2,3})"
print(re.findall(email_pattern, sample_txt))
print(re.search(email_pattern, sample_txt))
print(re.match(email_pattern, sample_txt, ))
print(re.sub(email_pattern, "++++", sample_txt))
print(re.split(email_pattern, sample_txt))