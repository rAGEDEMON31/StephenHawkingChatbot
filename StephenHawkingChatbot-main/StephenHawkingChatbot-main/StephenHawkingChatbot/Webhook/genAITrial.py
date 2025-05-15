import google.generativeai as genai

# Set API Key (Replace "YOUR_API_KEY" with your actual API key)
genai.configure(api_key="AIzaSyB7lo0uoNFjrJFbFEu_-8JghvWHRXxQwso")

# System instruction to set the chatbot personality
sys_instruct = "You are an astrophysicist. Your name is Stephen Hawking."

# Initialize the model and include system instruction in GenerationConfig
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=sys_instruct
)

user_input = input("Enter a prompt: ")

# Generate response correctly without unexpected keyword arguments
response = model.generate_content([user_input])

# Print the chatbot's response
print(response)