import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)

uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(65,90))
lowercaseLetter2=chr(random.randint(65,90))
lowercaseLetter3=chr(random.randint(65,90))
lowercaseLetter4=chr(random.randint(65,90))
punctuationSign1 = "!"
punctuationSign2 = "%"
punctuationSign3 = "*"

password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + punctuationSign1 + punctuationSign2 + punctuationSign3
password = shuffle(password)

print(password)