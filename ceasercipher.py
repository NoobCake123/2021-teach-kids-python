code = input("do you want to encode or decode? Press e for encode, or d for decode")
if (code == ("e")):
    message = input("what do you want to encode?")
    cipher = int(input("how many letters do you want to shift?"))
    message = message.upper()
    output = ""
    for letter in message:
        if letter.isupper:
            value = ((ord(letter) - 65 + cipher) % 26) + 65
            letter = chr(value)
            output += letter
    print("output message is", output)
if (code == ("d")):
   message = input("what is your encoded message?")
   cipher = int(input("how many letters is the message shifted by?"))
   message = message.upper()
   output = ""
   for letter in message:
       if letter.isupper:
           if ord(letter) < 65+cipher:
               value = 91 - cipher + (ord(letter)-65)
               letter = chr(value)
           else:
               value = ord(letter)-cipher
               letter = chr(value)
       output += letter
   print("your message is", output)




