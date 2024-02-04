from python:3.9.0
expose 8501
RUN apt-get update && \
    apt-get install -y gcc make apt-transport-https ca-certificates build-essential
CMD mkdir -p /app
WORKDIR /app
copy requirements.txt ./requirements.txt
run pip install -r requirements.txt
copy ["app.py","logger.py","exception.py","movie_dict.pkl","similarity.pkl","Data_modification.py","./"]
RUN ls /
ENTRYPOINT ["streamlit", "run", "app.py"]
CMD ["app.py"]

