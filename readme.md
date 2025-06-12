# Internship FAQ Chatbot

An AI-powered chatbot to answer frequently asked questions about internships.

## Features
- Answers common internship-related questions
- Maintains conversation context
- Deployable on website, WhatsApp, and Telegram
- Logs unanswered questions for improvement

## Installation
1. Clone the repository
2. Install requirements: `pip install rasa fastapi uvicorn sqlite3`
3. Train the model: `rasa train`
4. Run the action server: `rasa run actions`
5. Run the Rasa server: `rasa run --enable-api --cors "*"`
6. Run the FastAPI server: `python deploy.py`

## Adding New FAQs
1. Add new intents and examples to `data/nlu.yml`
2. Add corresponding responses to `domain.yml`
3. Add rules for new intents in `data/rules.yml`
4. Retrain the model: `rasa train`

## Deployment Options
- **Website**: Use the provided web interface
- **WhatsApp**: Configure Twilio webhook
- **Telegram**: Set up Telegram bot webhook
- **API**: Use the `/chat` endpoint for custom integrations

## Monitoring and Improvement
- Review logs in `question_logs.db`
- Analyze unanswered questions
- Add new training examples based on real user queries