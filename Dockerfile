FROM python:3.8-slim

WORKDIR /app

RUN pip install chatterbot==1.0.4 flask pytz

# Download NLTK data
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader punkt_tab
RUN python -m nltk.downloader punkt averaged_perceptron_tagger stopwords wordnet

COPY chatter.py .
COPY static/ ./static/

#Expose the port the app runs on
EXPOSE 5000

#Run the application
CMD ["python", "chatter.py"]
