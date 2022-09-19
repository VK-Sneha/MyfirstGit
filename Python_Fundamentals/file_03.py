Blood_group = input("Name the blood group available")

if Blood_group == "O -ve":

    print("Its the universal donar blood group")
    
elif Blood_group == "AB +ve":
    
    print("Its the universal recipient blood group,")

print("Thank you for visiting!, will let you know in case if we need blood from your blood group")

 
from PIL import Image
myImage = Image.open("../somebody-type.jpg")
myImage.show();   
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
   
#try: 
    #img  = Image.open("donate-for-life.jpg") 
#except IOError:
    #pass
# Use the above statement within try block, as it can 
# raise an IOError if file cannot be found, 
# or image cannot be opened.