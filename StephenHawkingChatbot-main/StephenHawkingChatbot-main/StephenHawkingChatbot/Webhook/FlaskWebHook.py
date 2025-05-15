from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS 
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import requests
import uuid

app = Flask(__name__)
CORS(app)  

genai.configure(api_key="AIzaSyB7lo0uoNFjrJFbFEu_-8JghvWHRXxQwso")

# System instruction to set the chatbot personality
sys_instruct = "You are an astrophysicist. Your name is Stephen Hawking."

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=sys_instruct
)

PROJECT_ID = "stepehnhawkingchatbot"
KEY_FILE_PATH = "StephenHawkingChatbot/Webhook/authkey.json"

def get_access_token():
    credentials = service_account.Credentials.from_service_account_file(
        KEY_FILE_PATH, scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    return credentials.token

def send_message_to_dialogflow(message, session_id):
    url = f"https://dialogflow.googleapis.com/v2/projects/{PROJECT_ID}/agent/sessions/{session_id}:detectIntent"
    print(url)
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }
    payload = {"queryInput": {"text": {"text": message, "languageCode": "en"}}}

    response = requests.post(url, headers=headers, json=payload)
    print(response)
    return response.json()["queryResult"]["fulfillmentText"] if response.status_code == 200 else "Error connecting to Dialogflow"

@app.route("/chat", methods=["POST"])
def chat():
    req = request.get_json()
    user_message = req.get("message", "")
    session_id = req.get("session", str(uuid.uuid4()))  # Keep session for context
    bot_response = send_message_to_dialogflow(user_message, session_id)
    return jsonify({"response": bot_response})


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    user_input = req["queryResult"]["queryText"]

    response = model.generate_content([user_input])
    bot_reply = response.text

    return jsonify({"fulfillmentText": bot_reply})

if __name__ == '__main__':
    app.run(port=5000)
