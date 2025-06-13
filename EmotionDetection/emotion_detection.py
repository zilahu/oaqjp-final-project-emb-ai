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
    response_text = json.loads(response.text)

    if response.status_code == 200:
        emotions = response_text['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        output = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion,
        }
    elif response.status_code == 400:
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

    return output


def main():
    print(json.dumps(emotion_detector("I'd like to go to the wilderness, and never come back!"), indent=2))

if __name__ == "__main__":
    main()