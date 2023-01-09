FROM python:latest
WORKDIR /performa
COPY /app/requirements.txt requirements.txt
COPY /app/reviewReturn.py app.py
COPY /app/data.txt data.txt
ENV FLASK_APP=app.py
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]