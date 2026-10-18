import hashlib
from pathlib import Path
def options():
    print("""
          1. Generate Hash File
          2. Verify File Integrity
          3. Exit
""")
    return input("\n > ")

def generate_hash():
    path = Path(input("Please Enter the file path here : "))
    b_path = path.read_bytes()
    h_path = Path("Hashed.txt")
    h_path.write_text(hashlib.sha256(b_path).hexdigest())
    print("Hashed file Created Succesfully!")


def verify():
    path = Path(input("Please Enter the file path here : "))
    b_path = path.read_bytes()
    h_path = Path("Hashed.txt")
    if(hashlib.sha256(b_path).hexdigest() ==  h_path.read_text()):
        print("Great, the file hasn't been modified:)")
    else:
        print("Warning! : The File has been modified!!")
         

#Main Program ,,,

while(True):
    choise = options()
    if choise == '1':
        try :
            generate_hash()
        except FileNotFoundError:
            print("File Not Found , Plese try Again !!")
    elif choise == '2':
        try :
            verify()
        except FileNotFoundError:
            print("File Not Found , Plese try Again !!")
    elif choise == '3':
        print("Bye Bye!")
        break
    else :
        print("Please Enter A valid number (1,2,3)!")
        
       
