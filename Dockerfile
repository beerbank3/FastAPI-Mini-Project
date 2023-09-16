FROM python:3.10.11

# Working directory 설정
WORKDIR /INTERVIEW_PROJECT

# requirements.txt 복사 및 설치
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# FastAPI 애플리케이션 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

