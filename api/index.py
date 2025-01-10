from fastapi import FastAPI
from datetime import datetime, date
from typing import Dict

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/ageCalculator/")

def age_calculator(birthday: str, reference_date: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :reference_date: 기준일 (형식: YYYY-MM-DD)
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

    birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
    ref_date = datetime.strptime(reference_date, "%Y-%m-%d").date()
    age  = ref_date.year - birth_date.year
    
    # TODO 띠 계산
    zodiac = zodiac_animals[(birth_date.year - 1900) % 12]

    # FiX 생일 지난 여부 확인
    if (birth_date.month > ref_date.month) or (birth_date.month == ref_date.month and birth_date.day > ref_date.day):
        age -= 1

    return {
            "birthday": birthday,
            "reference_date": reference_date,
            "age": str(age),
            "zodiac": zodiac,
            "basedate": str(today),
            "message": "Age calculated successfully!"
            }
