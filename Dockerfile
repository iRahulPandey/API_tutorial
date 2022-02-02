
# Specify your base image
FROM python:3.7.3-stretch
# create a work directory
RUN mkdir /app
# navigate to this work directory
WORKDIR /app
#Copy all files
COPY . .
# Install dependencies
RUN pip install sklearn joblib pandas numpy fastapi uvicorn Flask flask_restful
# Run
CMD ["python","app.py"]