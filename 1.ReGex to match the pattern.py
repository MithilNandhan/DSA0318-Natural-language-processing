import re
text="narayanareddyml4110.sse@saveetha.com The moon is Ebarth's only permaanent natural 20-02-2003 satellite 7730817844 8074804987 https://chatgpt.com/c/9d7e80f5-127e-45a3-9b25-7af54aac5857"
print("Original Text : ",text)
Matched=re.match(r'The',text)
if Matched:
    print("Matched word : ",Matched.group())
else:
    print("Not Matched")
Search=re.search(r'is',text)
if Search:
    print("Word Found : ",Search.group())
else:
    print("Not found!")
find_a=re.findall(r'[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}',text)
print(find_a)
