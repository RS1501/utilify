import React, { useState, useEffect } from 'react';
import './option1Page.css';

const Option1Page = () => {
  const [messages, setMessages] = useState([]);
  const [currentInput, setCurrentInput] = useState('');

  useEffect(() => {
    // Display welcome message when the component is mounted
    const welcomeMessage = { text: 'Hi! Welcome to the assistance for the phone services.', type: 'bot' };
    const welcomeMessage2 = { text: 'Please send your responses to these questions with a comma.', type: 'bot' };
    const welcomeMessage3 = { text: 'How much do you want to spend monthly? How many minutes of international calling do you want? Do you want benefits?', type: 'bot' };
    setMessages([welcomeMessage, welcomeMessage2, welcomeMessage3]);
  }, []);

  const handleInputChange = (event) => {
    setCurrentInput(event.target.value);
  };

  const handleSendMessage = async () => {
    if (currentInput.trim() === '') return;

    // Save user's message
    const newUserMessage = { text: currentInput, type: 'user' };
    setMessages([...messages, newUserMessage]);
    setCurrentInput('');

    // Send user's message to the FastAPI endpoint
    try {
      const response = await fetch('http://127.0.0.1:8000/api/sendMessage', {
        
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: currentInput }),
      });

      const responseData = await response.json();
      const botResponseMessage = { text: responseData.botResponse, type: 'bot' };

      // Update messages with the bot's response
      setMessages([...messages, botResponseMessage]);
    } catch (error) {
      console.error('Error sending message to server:', error.message);
    }
  };

  return (
    <div className="container">
      <h1>Chatbot</h1>
      <div className="chatbox">
        {messages.map((message, index) => (
          <div key={index} className={message.type === 'user' ? 'user-message' : 'bot-message'}>
            {message.type === 'user' ? (
              <div>
                <span className="user">User:</span> {message.text}
              </div>
            ) : (
              <div>
                <span className="bot">Chatbot:</span> {message.text}
              </div>
            )}
          </div>
        ))}
      </div>
      <div className="input-box">
        <input
          type="text"
          value={currentInput}
          onChange={handleInputChange}
          placeholder="Type your message..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Option1Page;
