# Stephen Hawking Chatbot

## Overview
This project is a Flask-based chatbot that simulates conversations with an AI modeled after Stephen Hawking. It integrates Google Generative AI (Gemini-2.0 Flash) for natural language generation and Dialogflow for intent detection. The chatbot is designed to provide responses as an astrophysicist, enhancing user interactions with scientific insights.

## Features
- Uses Google Generative AI (Gemini-2.0 Flash) for generating responses.
- Integrates with Dialogflow for intent-based responses.
- Flask-based API with CORS support.
- Secure authentication using Google Service Account credentials.
- Webhook endpoint for handling incoming requests.

## Installation
### Prerequisites
- Python 3.8+
- Flask
- Flask-CORS
- Google Generative AI SDK
- Google Authentication Library
- Requests

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/stephen-hawking-chatbot.git
   cd stephen-hawking-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Google Generative AI API key:
   Replace `api_key` in `genai.configure(api_key="YOUR_API_KEY")` with your actual API key.

4. Set up Google authentication:
   - Place your service account key file at `StephenHawkingChatbot/Webhook/authkey.json`.
   - Ensure your service account has Dialogflow permissions.

5. Run the application:
   ```bash
   python app.py
   ```
   The server will start on `http://127.0.0.1:5000/`.

## API Endpoints
### `/chat` (POST)
**Description:**
Handles user messages and retrieves responses from Dialogflow.

**Request Body:**
```json
{
  "message": "What is a black hole?",
  "session": "12345"
}
```

**Response:**
```json
{
  "response": "A black hole is a region of space where gravity is so strong that nothing can escape from it."
}
```

### `/webhook` (POST)
**Description:**
Handles webhook calls from Dialogflow and generates AI responses using Gemini-2.0 Flash.

**Request Body:**
```json
{
  "queryResult": {
    "queryText": "Tell me about wormholes."
  }
}
```

**Response:**
```json
{
  "fulfillmentText": "A wormhole is a theoretical passage through space-time that could create shortcuts for long journeys across the universe."
}
```

## Configuration
- **`PROJECT_ID`**: Set your Dialogflow project ID.
- **`KEY_FILE_PATH`**: Path to your service account JSON key.
- **`sys_instruct`**: Defines the chatbot's personality.

## Deployment
To deploy on a cloud service (e.g., Google Cloud, AWS, or Heroku), set up environment variables for API keys and configure authentication.

## License
This project is licensed under MIT License.

## Acknowledgments
- Google Generative AI
- Dialogflow
- Flask Community
