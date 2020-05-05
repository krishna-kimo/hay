FROM python:3.7.4-stretch

WORKDIR /home/user

# install as a package
#COPY setup.py requirements.txt README.rst /home/user/
#RUN pip install -r requirements.txt
#RUN pip install -e .
# install haystack
RUN git clone https://github.com/deepset-ai/haystack.git
WORKDIR haystack
RUN pip install .

WORKDIR /home/user
RUN pip install fastapi
RUN pip install uvicorn

# copy code
COPY . /home/user

# copy saved FARM models
COPY models/roberta /home/user/models

EXPOSE 8000

# cmd for running the API
CMD ["gunicorn", "fapi:app",  "-b", "0.0.0.0", "-k", "uvicorn.workers.UvicornWorker", "--workers", "2", "--timeout", "0"]
