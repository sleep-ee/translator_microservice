# Translator Microservice

## Description
A microservice to translate text from its detected language to a new language as specified. 

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

## API Reference
HTTP URL/ Route
```
http://127.0.0.1:5004/translate
POST /translate
```
Sample POST Request
```
POST /translate HTTP/1.1
Accept: application/json
Content-Type: application/json
{ 
         'language' : “spanish” ,
         'text': “i like computers"
}

```
Sample Response
```
{
  'text': "me gusta computadoras"
}
```
