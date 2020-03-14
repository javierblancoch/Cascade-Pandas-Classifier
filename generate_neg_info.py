from PIL import Image
import os, os.path

folders = ["neg"]
full_path = os.path.dirname(os.path.abspath(__file__))
valid_formats = [".jpg",".jpeg",".png"]

file_name_output = "neg.txt"

f= open(file_name_output,"w+")
for path in folders:
	for filename in os.listdir(path):
		ext = os.path.splitext(filename)[1]
		address = path+"/"+filename
		if ext in valid_formats:
			f.write(str(address+"\n"))
			print(address)
f.close()
