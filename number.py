def isPhonenumber(text):
    if len(text)!=10:
        return False
    for i in range(0,10):
        if not text[i].isdecimal():
            return False
    return True
            
    
#print(isPhonenumber("7899492248"))
#print(" is moshi moshi is phone number")
#print(isPhonenumber("moshi moshi"))

#message="my phone number 7899492248 and another one 8277083440"
#from docx import Document
message="""A random data generator  1234567891 can 
be useful if you re doing cross-browser testing. 
For example,
 if you need to write tests that fill forms
 9586432196 with random data (such 
as random strings or random zip codes), 576101
 then you can use this program to generate as many 
 random data elements as you need and put them in
 your test cases. 1646394689 You can independently 
 generate random strings of any length made out of lowercase or uppercase characters, including single-character strings. You can also generate 9876543210  random numbers and random text snippets from a custom alphabet. 9632659631 The generated data can also be used for random file names or random IDs in tests.
Looking for more web developer tools? Try these!

A random data generator  1234567891 can be useful 
if youre doing cross-browser testing. For example,
 if you need to write tests that fill forms 9586432196
 with random data (such as random strings or random 
zip codes), 576101 then you can use this program to
 generate as many random data elements as 
 you need and put them in your test cases. 
 1646394689 You can independently generate
 random strings of any length made out of lowercase or
 uppercase characters, including single-character strings.
 You can also generate 9876543210  random numbers and 
 random text snippets from a custom alphabet. 9632659631
 The generated data can also be used for random file
 names or random IDs in tests.
Looking for more web developer tools? Try these!"""



for i in range(len(message)):
    chunk=message[i:i+10]
    if isPhonenumber(chunk):
        print("phone number found: "+chunk)

print("done")