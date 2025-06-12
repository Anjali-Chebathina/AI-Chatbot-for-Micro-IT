# AI-Chatbot-for-Micro-IT

# 🤖 AI FAQ Chatbot for Internship Queries

**Made with ❤️ to Micro IT Services (MITS)**
## 🎯 Overview

An intelligent chatbot built using **Rasa** to answer frequently asked questions about **internships**, **application processes**, **organization details**, and more. This project aims to automate responses to common queries and enhance the user support experience.

An AI-powered chatbot to answer frequently asked questions about internships.
 
 ---
## UI preview

![Screenshot 2025-06-12 195604](https://github.com/user-attachments/assets/fb91123e-68c3-4e31-8443-ec1c0a380f16)

![Screenshot 2025-06-12 195637](https://github.com/user-attachments/assets/a130a091-2a75-4f7a-a1e6-a63cd39e7c6d)

## 📝 Features

- ✅ Answers to common internship-related FAQs
- 🧠 Natural Language Understanding (NLU) with Rasa
- 🔄 Multi-turn conversations with context
- ⚠️ Fallbacks for unclear or unsupported questions
- 🌐 Deployable on web, Telegram, or other platforms
- 🔧 Easy to retrain with new questions/answers

---

## 🧰 Tech Stack

| Component     | Technology          |
|---------------|---------------------|
| Chatbot Engine | Rasa (Open Source) |
| Programming Language | Python |
| NLP Model     | Rasa NLU Pipeline |
| Interface     | Terminal / Web Widget / Telegram |
| Deployment    | Localhost / Heroku / Render |

---

## 📁 Project Structure

```
faq-chatbot/
├── actions/ # Custom action scripts
│ └── actions.py
├── data/ # Training data
│ ├── nlu.yml
│ ├── rules.yml
│ └── stories.yml
├── models/ # Trained models
├── domain.yml # Intents, responses, slots, actions
├── config.yml # NLP pipeline and policies
├── endpoints.yml # Action server and webhook config
├── credentials.yml # Channel credentials
└── README.md # Project overview
```

---

## 🚀 Getting Started

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/faq-chatbot.git
cd faq-chatbot

### 2. **Install Dependencies**
 ```bash

pip install rasa

 ```
### 3. **Train the Bot**

```
rasa train

```
### 4. **Talk to the Bot**
```
rasa shell

```
### 5. **Run on Web Chat Interface** 

```
rasa run actions
rasa run -m models --enable-api --cors "*"

```
---

---

## 🧠 Example Intents

- greet: "Hi", "Hello", "Hey"

- ask_internship_eligibility: "Who is eligible for the internship?"

- ask_application_deadline: "When is the last date to apply?"

- ask_organization_info: "Tell me about your organization."

- ask_contact_info: "How can I contact you?"

---

## 📊 Future Improvements

- Add dynamic responses via APIs

- Enable multilingual support

- Collect user feedback to retrain NLU


## 👥 About Micro IT Services (MITS)

Micro IT Services (MITS) is dedicated to bridging the gap between students and industry through innovative technology solutions. Our mission is to empower the next generation of tech professionals with the tools and opportunities they need to succeed.

## 📞 Support

For support, please contact :
- Email: anjalichebathina@gmail.com


---

**Made with ❤️ to Micro IT Services (MITS)**
