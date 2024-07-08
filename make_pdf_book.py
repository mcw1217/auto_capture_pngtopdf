import os
from PyPDF2 import PdfFileReader, PdfMerger 
import glob
from PIL import Image
from datetime import datetime
import requests

now = datetime.now()

#라인 메시지 전송 / api_url, token을 자신의 line으로 변경해야 알림 확인 가능
api_url = "https://notify-api.line.me/api/notify"
token = "LYy0yPmrqjMc3rmvdQR2WcbCCVZkmFlf6FZBZGEkpYQ"

headers = {'Authorization':'Bearer '+token}





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
    list = sorted(glob.glob("./img_pdf/*.pdf"), key=os.path.getctime)
    merger = PdfMerger()
    for pdf in list:
        merger.append(pdf)
    merger.write("output.pdf")
    merger.close()
    print("묶음으로 변환 완료!")
    message = {
        "message" : "[PDF추출기 알림] : Ebook에 대한 PDF 추출이 성공적으로 완료되었습니다!"
    }
    requests.post(api_url, headers= headers , data = message)
    
    
def self_pngtopdf():
    print("png파일을 pdf로 변경합니다!")
    list = glob.glob("./img/*.png")
    for i,imgs in enumerate(list):
        img = Image.open(imgs)
        img_pdf = img.convert('RGB')    
        img_pdf.save(f"./img_pdf/{i}.pdf", resolution=100)
    print("pdf로 변환완료! ===> pdf를 묶음으로 변환합니다!")
    list = sorted(glob.glob("./img_pdf/*.pdf"), key=os.path.getctime)
    merger = PdfMerger()
    for pdf in list:
        merger.append(pdf)
    merger.write("output.pdf")
    merger.close()
    print("묶음으로 변환 완료!")
    
def self_countp():
    a= glob.glob("./img/*.png")
    print(f"복제된 페이지수: {len(a)}")
        
self_pngtopdf()
# countp()

        
# 95쪽

