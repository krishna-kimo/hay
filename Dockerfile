FROM python:3.7.4-stretch

WORKDIR /home/user

# install as a package
COPY setup.py requirements.txt README.rst /home/user/
RUN pip install -r requirements.txt
RUN pip install -e .
# install haystack
RUN git clone https://github.com/deepset-ai/haystack.git
WORKDIR haystack

# copy code
COPY haystack /home/user/haystack

# copy saved FARM models
COPY models /home/user/models

EXPOSE 8000

# cmd for running the API
CMD ["gunicorn", "haystack.api.application:app",  "-b", "0.0.0.0", "-k", "uvicorn.workers.UvicornWorker", "--workers", "2"]
