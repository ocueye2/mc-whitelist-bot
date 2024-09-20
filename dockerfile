FROM ubuntu:22.04


RUN apt-get update && apt-get install -y python3 python3-pip


COPY start.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV KEY=KEY
ENV HOST=HOST
ENV PORT=PORT
ENV PASSWORD=PASSWORD


CMD ["python3", "start.py"]
