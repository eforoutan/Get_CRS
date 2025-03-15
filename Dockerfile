FROM python:3.9-slim

RUN pip install geopandas

WORKDIR /app

COPY get_crs.py /app/get_crs.py

ENTRYPOINT [ "python3", "/app/get_crs.py" ]