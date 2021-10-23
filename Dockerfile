FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./app /app
WORKDIR /app
RUN pip install sklearn joblib pandas numpy fastapi uvicorn
CMD ["uvicorn", "fast_app:app", "--host", "0.0.0.0"]

# After this build docker and then just create container from terminal
# docker build -t myimage .
# docker run -d --name mycontainer -p 8000:8000 myimage