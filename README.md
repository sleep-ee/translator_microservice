# Translator Microservice

## Description
A microservice to translate text from the detected language it is in to a new language as specified. 

## How to Use
### Requirements
1. Python 3
### Installation
```
git clone https://github.com/sleep-ee/translator_microservice.git
cd translator_microservice
pip install -r requirements.txt
```
### Usage
```
python translate.py
```
The application will start running on https://127.0.0.1:5004/translate
ctrl+c will kill this process

## API Reference
HTTP URL
```
http://127.0.0.1:5004/translate
```
ROUTES
```
POST /translate
```
This microservice takes a POST HTTP request with request JSON body structured as follows:
```
{
  'text': 'hola, como estas',
  'language': 'english'
}
```
The response will be in JSON and be structured like the following:
```
{
  'text': 'hi, how are you'
}
```
