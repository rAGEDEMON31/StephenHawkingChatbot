import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [messages, setMessages] = useState([{ sender: "bot", text: "Enter text for me to respond to." }]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { sender: "user", text: input };
    setInput(""); // Clear input field
    setMessages([...messages, userMessage]); // Add user message to chat

    try {
      const response = await axios.post("http://localhost:5000/chat", { message: input });
      const botMessage = { sender: "bot", text: response.data.response };

      setMessages([...messages, userMessage, botMessage]); // Add bot response to chat
    } catch (error) {
      console.error("Error:", error);
    }


  };

  return (
    <div>
      {/* <h1 class="bg-gray-900 text-gray-400">Stephen Hawking AI Chatbot</h1> */}
    <div class="flex h-screen">
        <aside class="w-1/5 bg-gray-800 p-4 flex flex-col">
            <button class="w-full bg-gray-700 text-white py-2 rounded-lg mb-4">+ New Chat</button>
            <div class="space-y-2 overflow-auto flex-1">
                <div class="bg-gray-700 p-2 rounded-lg cursor-pointer">Chatbot Session</div>
            </div>
        </aside>

        {/* <!-- Main Chat Window --> */}
        <main class="flex-1 flex flex-col bg-gray-900 p-3">

            {/* <!-- Chat Messages --> */}
            <div id="chat-box" class="flex-1 overflow-y-auto p-4 space-y-4">
                <div class="text-center text-gray-400">
                {messages.map((msg, index) => (
            <div
              key={index}
              className={`flex ${msg.sender === "user" ? "justify-end" : "justify-start"} my-4`}
            >
              <p
                className={`p-3 rounded-lg max-w-5xl ${
                  msg.sender === "user"
                    ? "bg-blue-500 text-white self-end"
                    : "bg-gray-600 text-white"
                }`}
              >
                {msg.text}
              </p>
            </div>
          ))}
                </div>
            </div>

            {/* <!-- Chat Input --> */}
            <div class="p-4 border-t border-gray-700 flex">
            <input
            type="text"
            className="flex-1 p-2 bg-gray-800 text-white rounded-l focus:outline-none"
            placeholder="Ask me something..." 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === "Enter" && sendMessage()}
          />
          <button
            className="bg-blue-500 px-4 py-2 rounded-r text-white hover:bg-blue-600 transition"
            onClick={sendMessage}
          >
            Send
          </button>
            </div>
        </main>
    </div>
    </div>
  );
};

export default Chatbot;
