FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./app /app
WORKDIR /app
RUN pip install sklearn joblib pandas numpy fastapi uvicorn
#EXPOSE 9696
#ENTRYPOINT ["uvicorn", "fast_app:app --reload"]
#CMD ["uvicorn", "fast_app:app", "--host", "0.0.0.0", "--port", "8002"]
#CMD ["uvicorn", "fast_app:app", "9696"]
#CMD ["python", "fast_app.py"]
CMD ["uvicorn", "fast_app:app", "--host", "0.0.0.0"]