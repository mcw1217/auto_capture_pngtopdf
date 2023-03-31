import os
from PyPDF2 import PdfFileReader, PdfMerger 
import glob
from PIL import Image
def countp(cnt):
    a= glob.glob("./img/*.png")
    print(f"책 페이지 수:{cnt} || 복제된 페이지수: {len(a)}")
    if int(cnt) == len(a):
        return 1
    print("책 페이지와 복제 페이지가 일치하지 않기에 종료됩니다!")
    return 0

def pngtopdf(co):
    if co == 0:
        return 0
    print("png파일을 pdf로 변경합니다!")
    list = glob.glob("./img/*.png")
    for i,imgs in enumerate(list):
        img = Image.open(imgs)
        img_pdf = img.convert('RGB')    
        img_pdf.save(f"./img_pdf/{i}.pdf", resolution=100)
    print("pdf로 변환완료! ===> pdf를 묶음으로 변환합니다!")
    list = glob.glob("./img_pdf/*.pdf")
    merger = PdfMerger()
    for pdf in list:
        merger.append(pdf)
    merger.write("output.pdf")
    merger.close()
    print("묶음으로 변환 완료!")
    
    
def self_pngtopdf():
    print("png파일을 pdf로 변경합니다!")
    list = glob.glob("./img/*.png")
    for i,imgs in enumerate(list):
        img = Image.open(imgs)
        img_pdf = img.convert('RGB')    
        img_pdf.save(f"./img_pdf/{i}.pdf", resolution=100)
    print("pdf로 변환완료! ===> pdf를 묶음으로 변환합니다!")
    list = glob.glob("./img_pdf/*.pdf")
    merger = PdfMerger()
    for pdf in list:
        merger.append(pdf)
    merger.write("output.pdf")
    merger.close()
    print("묶음으로 변환 완료!")
    
def self_countp():
    a= glob.glob("./img/*.png")
    print(f"복제된 페이지수: {len(a)}")
        
# self_pngtopdf()
# countp()

        
# 95쪽

