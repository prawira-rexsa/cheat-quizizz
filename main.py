import requests
import re

def remove_html_tags(text):
    return re.sub(r'<[^>]*>', '', text)

def fetch_quiz_answers(pin):
    url = f"https://api.quizit.online/quizizz/answers?pin={pin}"

    response = requests.get(url)
    print(response.json())

    if response.status_code == 200:
        data = response.json()

        if "data" in data and "answers" in data["data"]:
            answers = data["data"]["answers"]

            for item in answers:
                question_text = item["question"]["text"]
                answer_text = item["answers"][0]["text"]

                question_text = remove_html_tags(question_text)
                answer_text = remove_html_tags(answer_text)
                
                print("Question:", question_text)
                print("Answer:", answer_text)
                print("-" * 50)
        else:
            print("Data tidak ditemukan dalam respons API.")
    else:
        print(data)
        print(f"Request gagal dengan status code {response.status_code}")

pin_input = input("Masukkan PIN: ")

fetch_quiz_answers(pin_input)
