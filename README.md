# NoPickles MVP - Conversational AI Ordering System

A simplified MVP version of [NoPickles](https://github.com/iota-tec/nopickles) - an AI-powered conversational ordering system for fast food chains.

## Features

- 💬 **Conversational Ordering**: Natural language ordering powered by OpenAI GPT
- 🍔 **Menu Management**: Pre-configured menu with items and pricing
- 💰 **Price Calculation**: Automatic order total calculation
- 🌐 **Web Interface**: Simple, clean chat interface for ordering
- 🤖 **Intent Recognition**: Basic order processing and confirmation

## Tech Stack

- **Backend**: FastAPI (Python 3.11+)
- **AI**: OpenAI GPT-3.5/GPT-4
- **Frontend**: HTML/CSS/JavaScript (vanilla)
- **Styling**: Modern CSS with custom design

## What's Different from the Parent Project?

This MVP simplifies the original NoPickles project by:
- ❌ No face recognition or biometric authentication
- ❌ No speech-to-text / text-to-speech
- ❌ No BERT-based NER/Intent classification
- ❌ No age/gender/ethnicity detection
- ❌ No MySQL database (in-memory storage)
- ✅ Text-based chat interface instead of voice
- ✅ Direct OpenAI integration for conversations
- ✅ Simple web UI instead of Windows IoT kiosk

## Setup

### Prerequisites

- Python 3.11 or higher
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/gitmvp-com/nopickles-mvp-app.git
cd nopickles-mvp-app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### Running the Application

1. Start the FastAPI server:
```bash
python main.py
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

3. Start ordering through the chat interface!

## Project Structure

```
nopickles-mvp-app/
├── main.py                 # FastAPI application and routes
├── static/
│   ├── index.html         # Chat interface
│   ├── style.css          # Styling
│   └── script.js          # Frontend logic
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Usage

1. Open the application in your browser
2. Type your order in natural language (e.g., "I'd like a large coffee and a donut")
3. The AI will confirm your order and calculate the total
4. Continue adding items or confirm your order

## Menu Items

The MVP includes a sample menu with:
- ☕ Beverages: Coffee, Cappuccino, Latte, Tea, etc.
- 🥪 Food: Sandwiches, Wraps, Donuts, Bagels, etc.
- 📏 Sizes: Small, Medium, Large, Extra Large (with price multipliers)

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required for AI conversations)

## Future Enhancements

To make this MVP production-ready, consider adding:
- User authentication
- Order history and persistence
- Payment processing
- Admin dashboard for menu management
- Multi-language support
- Voice interface integration

## License

MIT License - See LICENSE file for details

## Credits

Based on [NoPickles](https://github.com/iota-tec/nopickles) by iota-tec
