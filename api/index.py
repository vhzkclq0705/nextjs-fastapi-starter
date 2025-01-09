from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/ageCalculator/{birthday}")

def age_calculator(birthday: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :return: 생년월일 및 만나이, 띠 를 포함한 JSON 응답
    """
    zodiac_animals = [
    "쥐띠 🐀 ", 	# 자 - 쥐
    "소띠 🐂",      	# 축 - 소
    "호랑이띠 🐅",    	# 인 - 호랑이
    "토끼띠 🐇",   	# 묘 - 토끼
    "용띠 🐉",   	# 진 - 용
    "뱀띠 🐍",    	# 사 - 뱀
    "말띠 🐎",    	# 오 - 말
    "양띠 🐐",     	# 미 - 양
    "원숭이띠 🐒",  	# 신 - 원숭이
    "닭띠 🐓",  	# 유 - 닭
    "개띠 🐕",     	# 술 - 개
    "돼지띠 🐖"       	# 해 - 돼지
    ]

    today = date.today()
    birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
    age  = today.year - birth_date.year
    
    # TODO 띠 계산
    zodiac_animal = zodiac_animals[(today.year - 1900) % 12]

    # FiX 생일 지난 여부 확인
    if (birth_date.month > today.month) or (birth_date.month == today.month and birth_date.day > today.day):
        age -= 1

    return {
            "birthday": birthday,
            "age": f"만 {age}세, {zodiac_animal}",
            "basedate": str(today),
            "message": "Age calculated successfully!"
            }
