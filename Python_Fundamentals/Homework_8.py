"""
Create a note-taking program. When a user starts it up, it should prompt them for a filename.

If they enter a file name that doesn't exist, it should prompt them to enter the text they want 
to write to the file. After they enter the text, it should save the file and exit.

If they enter a file name that already exists, it should ask the user if they want:

A) Read the file

B) Delete the file and start over

C) Append the file

If the user wants to read the file it should simply show the contents 
of the file on the screen. If the user wants to start over then the file should be deleted and another 
empty one made in its place. If a user elects to append the file, 
then they should be able to enter more text, and that text should be added to the existing text in the file. 

"""
 
import os 
file = input("Please enter the filename: ") 

if os.path.isfile(file):   

    print("Found it!")
    y = input("please choose the option below: \n 1) Read the file\n 2) Delete the file and start over\n 3) Append the file\n")
    if y == "1" :
        personalFile = open(file, "r")
        display = personalFile.read()
        print(display)

        personalFile.close()

    if y == "2" :
        print ("\n Starting the deletion of the file.....")
        os.remove(file)
        print ("\n File deletion is successfully completed.\n ")
        inputfile = open(file, "w")
        inputfile.write("")

        inputfile.close()

    if y == "3" :
        addContent = input("Please enter the content to be added to the file: \n")
        appendFile = open(file, "a")
        appendFile.write("\n" + addContent)

        appendFile.close()

else:

    print("This file doesn't exit ")
    text = input("Please enter your note: ")
    newfile = open(file, "w")
    newfile.write(text + " ")

    newfile.close()
