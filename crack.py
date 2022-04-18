import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("relax_enc").__key__()
   except Exception as e:
       exit(str(e))
