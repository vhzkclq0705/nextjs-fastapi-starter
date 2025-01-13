import korean_age_calculator as kac
from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict
import random
import sys

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/getOSVersion")
def get_os_version() -> Dict[str, str]:
    """
    OS의 종류와 버전을 받아오는 API
    
    :return: OS의 종류 및 버전을 포함한 JSON 응답
    """
    def get_macro():
        with open("/etc/os-release", "r") as f:
            for line in f:
	        if line.startswith("PRETTY_NAME="):
		    return line.split("=")[1].replace("\n", "").strip('"')
 	return None
    
    result = get_macro()

    return {
	"os_version": result if result else "",
	"message": "Got the OS version successfully!" if result else "Failed to get the OS version."
    }

@app.get("/api/py/ageCalculator/{birthday}")
def age_calculator(birthday: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :return: 생년월일 및 만나이, 띠 를 포함한 JSON 응답
    """

    zodiac_animals = [
        "🐀 Rat",      # 자 - 쥐
        "🐂 Ox",       # 축 - 소
        "🐅 Tiger",    # 인 - 호랑이
        "🐇 Rabbit",   # 묘 - 토끼
        "🐉 Dragon",   # 진 - 용
        "🐍 Snake",    # 사 - 뱀
        "🐎 Horse",    # 오 - 말
        "🐐 Goat",     # 미 - 양
        "🐒 Monkey",   # 신 - 원숭이
        "🐓 Rooster",  # 유 - 닭
        "🐕 Dog",      # 술 - 개
        "🐖 Pig"       # 해 - 돼지
    ]

    today = date.today()
    birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
    kage = kac.how_korean_age(year_of_birth=birth_date.year)
    age  = today.year - birth_date.year
    
    # 띠 계산
    zodiac = zodiac_animals[(birth_date.year - 1900) % 12]

    # 생일 지난 여부 확인
    if (birth_date.month > today.month) or (birth_date.month == today.month and birth_date.day > today.day):
        age -= 1

    return {
            "birthday": birthday,
            "age": str(age),
            "kage": str(kage),
            "speaker": "권오준",
            "zodiac": zodiac,
	    "version": sys.version,
            "basedate": str(today),
            "message": "Age calculated successfully!"
            }

@app.get("/api/py/randomStudent")
def random_student() -> Dict[str, str]:
    """
    랜덤으로 학생을 선택하는 API

    :return: 랜덤으로 선택된 학생이 포함된 JSON 응답
    """
    
    students = [
	"권오준",
	"조민규",
	"강현룡",
	"서민혁",
	"백지원",
	"전희진",
	"배형균",
	"안재영",
	"조성근"
    ]

    student = random.choice(students)

    return {
	"student": student,
	"version": sys.version,
	"message": "got a random student successfully!"
    }
