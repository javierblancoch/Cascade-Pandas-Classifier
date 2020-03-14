from PIL import Image
import os, os.path

folders = ["pos"]
full_path = os.path.dirname(os.path.abspath(__file__))
valid_formats = [".jpg",".jpeg",".png"]

file_name_output = "pos.info"

def get_dimentions(image_path):
	img = Image.open(image_path)
	width, height = img.size
	result = str(width)+" "+str(height)
	return result

f= open(file_name_output,"w+")
for path in folders:
	for filename in os.listdir(path):
		ext = os.path.splitext(filename)[1]
		address = path+"/"+filename
		aditional = "1 0 0"
		information = str(address+" "+aditional+" "+get_dimentions(os.path.join(full_path,path,filename)))
		if ext in valid_formats:
			f.write(str(information+"\n"))
			print(information)
f.close()

