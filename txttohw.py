#pip install pywhatkit

import pywhatkit as pwt

#text to handwriting by message
pwt.text_to_handwriting("Hello WORLD 123","//Users//raunakkumar//Desktop//project//text_to_handwriting//hw1.png",[10,10,10]) #put double // in path
#can use .png or .jpeg

#text to handwriting by reading from a file
fo=open("/Users/raunakkumar/Desktop/project/text_to_handwriting/file1.txt","r")
str = fo.read()
pwt.text_to_handwriting(str,"//Users//raunakkumar//Desktop//project//text_to_handwriting//hw2.png",[20,20,20])
