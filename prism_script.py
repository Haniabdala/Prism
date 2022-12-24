import fileinput
import pyfiglet
import mimetypes
import hashlib
from VT_requests import VT_post_file

print(pyfiglet.figlet_format("PRISM", font = "slant"))
print ("PRISM is a malware analysis tool that is based on VirusTotal API.\nWhat you would like to check \n 1) File \n 2) Under_Dev")

API_KEY = "0" #Replace 0 with your VirusTotal API key 

Chosen_path = input()
if Chosen_path == "1":
    file_path = input("Please enter the file path (make sure the path is not too long).\n")
    file_type = mimetypes.MimeTypes().guess_type(file_path)[0]
    VT_post_file.Post_file(file_path,file_type,API_KEY)
elif Chosen_path == "2":
    print("Under_Dev")
else:
    print("Please re-run and choose a valid option.\n")