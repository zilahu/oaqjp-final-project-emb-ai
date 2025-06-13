import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = { 
        "raw_document": { 
            "text": text_to_analyse 
        } 
    }
    response = requests.post(url, json = myobj, headers=header)
    
    return response.text

def main():
    print(emotion_detector("I'd like to go to the wilderness, and never come back!"))

if __name__ == "__main__":
    main()