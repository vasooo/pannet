FROM python:3

RUN apt-get update && \
    apt-get install -y python-pip git && \
    apt-get clean && \
    git clone https://github.com/csparpa/pyowm.git

# Update pip and install dev requirements

RUN pip install setuptools pip && \
    pip install pyowm && \
    pip install git+https://github.com/csparpa/pyowm.git@v2.9-LTS && \
    pip install -r /pyowm/dev-requirements.txt
    

COPY getweather.py /pyowm

WORKDIR /pyowm

CMD ["python", "./getweather.py"]
