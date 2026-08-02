from pypdf import PdfWriter
import os 
merger=PdfWriter()
try:
    pdf=int(input("enter the number of pdf you want to merge :"))
    for i in range(pdf):
        a=input(f"path of {i+1} pdf :").strip("'\"")
        merger.append(a)
    output_pdf=os.path.join(r"C:\Users\acer\Desktop","merged.pdf")
    merger.write(output_pdf)
    merger.close()
    print("saved at:",os.path.abspath(output_pdf))
except FileNotFoundError:
    print("pls check the path of given pdfs")
except ValueError:
    print("pls enter the no of pdfs you want to merge")
except Exception as e:
    print(f'An error occured:{e}')
input("press anywhere to exit")

