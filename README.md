픽픽 캡쳐 프로그램을 설치 후
옵션에서 [자동저장]에 들어가서 main.py 가 존재하는 디렉토리에서 img 폴더를 자동저장 폴더로 지정한다

지정 후 [단축키] 에서 '고정된 사각 영역을 캡처하기' 의 단축키를 Shift + s 로 설정한다.

그 후 고정된 사각 영역을 캡처하기 로 캡쳐하려는 영역을 지정한 후 한번 클릭하여 영역을 확정시켜준다.
그 후 픽픽을 끄지말고 아래로 내리고 main.py 를 실행하여 콘솔에 복제하려는 페이지 수를 입력한 후 
복제하려는 이미지 위에 마우스를 올리고 키보드 's' 키를 누른 후 복제가 완료될때까지 기다린다.

복제가 완료되면 main.py가 존재하는 디렉토리에 output.pdf 파일이 생성된다.

재사용하려면 img 폴더에 있는 이미지만 삭제 후 재사용하면 된다.


[!] 이 프로그램은  yes24를 기준으로 만들었기에 다른 ebook의 경우 호환이 되지 않을 수 있음

[!] 이 프로그램을 사용하여 저작권법에 위배되는 행위를 하는 경우는 책임지지않으며 개인의 책임임을 고지함 

[!!] 사용시 메인 디렉토리에 book, img, img_pdf 폴더를 생성해야함


--수정--

glob 라이브러리의 glob.glob은 경로의 위치를 가져오는데 문자열 형식으로 가져오기에 파일의 이름이 숫자로 1~200일때 리스트 형식에서 문자열인 숫자를 셀때는 1 100 101 102 순으로 정렬하기에 
glob.glob 을 사용할때 sorted(glob.glob("./img_pdf/*.pdf"), key=os.path.getctime) 같이 sorted 함수를 사용한다. 여기에 파라미터로 os.path.getctime은 파일의 생성순서대로 가져온다는 뜻이다.
