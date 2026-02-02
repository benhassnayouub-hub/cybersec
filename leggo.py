def main():
    # import sys 

  nomefile = "logfile.txt"
  try:
      f=open(nomefile, "r" , encoding='utf-8')
      right=f.readlines()
      for riga in  righe:
          print(riga, end="")
  expect FilenotFoundError as e:
         print(f"[-] errore blocante:{str(e)}")

if __name__=="__main__":
     main() 
  
