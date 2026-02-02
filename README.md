# Rule-Based Chatbot using Python & Regex

## 📌 Project Description
This project implements a **Rule-Based Conversational Chatbot** using **Python** and **Regular Expressions (Regex)**.  
The chatbot works on **pattern-matching rules** to recognize user intent and respond accordingly without using any machine learning models.

It is designed as a beginner-friendly NLP project focusing on **intent recognition using keyword mapping**.

---

## 🎯 Features
- Rule-based conversation flow
- Intent recognition using **Regex patterns**
- Keyword-to-intent mapping
- Fallback response for unknown inputs
- Supports multiple conversation topics
- Simple and lightweight implementation

---

## 🗣️ Supported Conversation Topics
1. **Greetings** (Hi, Hello, Hey)
2. **Education / College Queries**
3. **Weather-related Queries**
4. **Help & Exit Commands**

---

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Concepts Used:**  
  - Regular Expressions (Regex)  
  - Basic NLP concepts  
  - Conditional logic  
  - Pattern matching  

---

## 📂 Project Structure
regx_chatbot/
│
├── main.py # Chatbot implementation
├── README.md # Project documentation

---

## ⚙️ How It Works
1. User enters a message
2. Input is converted to lowercase
3. Regex patterns are matched with predefined intents
4. Corresponding response is returned
5. If no pattern matches, a fallback message is shown

---

## ▶️ How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/AlokRoyal/regx_chatbot.git
```
2. Navigate to the project directory:
```
cd regx_chatbot
```
3. Run the chatbot:
```
python main.py
```

