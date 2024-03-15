
import requests    # requests라는 외부 라이브러리는 서버에 데이터를 전송할떄 사용한다.

api_url = "https://notify-api.line.me/api/notify"
token = "LYy0yPmrqjMc3rmvdQR2WcbCCVZkmFlf6FZBZGEkpYQ"

headers = {'Authorization':'Bearer '+token}

message = {
    "message" : "Hello world"
}

requests.post(api_url, headers= headers , data = message)
