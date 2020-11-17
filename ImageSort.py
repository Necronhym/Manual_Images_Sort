import os
import re
from tkinter import *
from PIL import Image, ImageTk
#Fetch images and folders:
def getImagesAndFolders():
	DirList = os.listdir()
	imgRegEx = re.compile('(.png$|.jpg$|.jpeg$|.gif$)')
	folderRegEx = re.compile('(\.)')
	Folders = list()
	Images = list()
	for i in DirList:
		if(folderRegEx.search(i)):
			if(imgRegEx.search(i)):
				Images.append(i)
			else:
				continue;
		else:
			Folders.append(i)

	return Images, Folders;

#Image move function:
def moveImageToFolder(Folder):
	global Images
	os.rename(str(Images[0]), Folder+"/"+str(Images[0]));
	Images.pop(0);
	if not Images:
		imageName=Label(window, text="No images found", fg="black")
		imageName.place(x=50,y=15);
		c.delete("all")
		window.unbind();
		window.bind("<KeyPress>", exit)
	else:
		showImage(Images[0])

#Bind keys:

#Show Image:
def showImage(ImagePath):
	#Image Name:
	imageName=Label(window, text=ImagePath, fg="black")
	imageName.place(x=50,y=15);
	#Show Image:
	I = Image.open(ImagePath)
	I = I.resize((300,300))
	pH=ImageTk.PhotoImage(I)
	c.image=pH
	c.create_image(150,150, image=pH)

def showFolders(Folders):
	folderLabels = list()
	yP=50;
	j=1;
	for i in Folders:
		imageName=Label(window, text=str(j) +"  " + i, fg="black")
		imageName.place(x=370,y=yP);
		yP=yP+25
		#Bind Keygs
		window.bind(str(j), lambda x, f=Folders[j-1]: moveImageToFolder(f))	
		j=j+1
window=Tk()
window.title("Image Sort")
window.geometry("600x400")
Images,Folders = getImagesAndFolders()
if not Images:
	print("no images where found")
	exit()
if not Folders:
	print("no folders where found")
	exit()
c=Canvas(window, width=300, height=300)
c.place(x=50, y=50)
showImage(Images[0])
showFolders(Folders)
#Folders and keybindings:
#Image/Images
window.mainloop()
