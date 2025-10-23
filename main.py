from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
import os
from openai import OpenAI
from dotenv import load_dotenv
import uvicorn

# Load environment variables
load_dotenv()

app = FastAPI(title="NoPickles MVP")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "sk-test-key"))

# Menu configuration (from original nopickles)
MENU = {
    "prices": {
        "coffee": 1.50,
        "cappuccino": 2.50,
        "iced coffee": 2.00,
        "iced capp": 2.25,
        "latte": 2.00,
        "tea": 1.50,
        "hot chocolate": 2.25,
        "french vanilla": 2.25,
        "white chocolate": 2.25,
        "mocha": 2.25,
        "espresso": 1.00,
        "americano": 2.25,
        "extra shot": 0.25,
        "soy milk": 0.30,
        "whipped topping": 1.00,
        "dark roast": 0.20,
        "turkey bacon club": 3.00,
        "blt": 2.90,
        "grilled cheese": 4.00,
        "chicken wrap": 3.50,
        "soup": 2.80,
        "donut": 1.50,
        "double double": 1.50,
        "triple triple": 1.50,
        "muffin": 2.40,
        "bagel": 3.00,
        "timbits": 3.00,
        "panini": 2.40,
        "croissant": 3.00
    },
    "price_multiplier": {
        "small": 1.0,
        "medium": 1.2,
        "large": 1.4,
        "extra large": 1.6
    }
}

# System prompt for the AI assistant
SYSTEM_PROMPT = f"""You are a friendly AI assistant for NoPickles, a fast food restaurant. Your job is to help customers place orders.

Available menu items and prices:
{chr(10).join([f'- {item.title()}: ${price:.2f}' for item, price in MENU['prices'].items()])}

Size multipliers (for beverages):
{chr(10).join([f'- {size.title()}: {mult}x price' for size, mult in MENU['price_multiplier'].items()])}

Guidelines:
1. Greet customers warmly
2. Help them browse the menu
3. Take their orders clearly
4. Confirm items and quantities
5. Calculate totals accurately
6. Be helpful with questions about menu items
7. When you calculate a price, show your work
8. Keep responses concise and friendly

When a customer places an order, acknowledge each item and provide the running total.
"""

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class ChatResponse(BaseModel):
    message: str
    total: Optional[float] = None

# In-memory session storage (simplified)
sessions: Dict[str, List[Dict]] = {}

@app.get("/")
async def read_root():
    """Serve the main HTML page"""
    return FileResponse("static/index.html")

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Handle chat messages and return AI responses"""
    try:
        # Convert Pydantic models to dicts for OpenAI
        messages = [msg.dict() for msg in request.messages]
        
        # Add system prompt if it's the first message
        if len(messages) == 1:
            messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        assistant_message = response.choices[0].message.content
        
        return ChatResponse(
            message=assistant_message,
            total=None  # Could implement order tracking here
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@app.get("/api/menu")
async def get_menu():
    """Return the complete menu"""
    return MENU

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "nopickles-mvp"}

if __name__ == "__main__":
    print("🍔 NoPickles MVP - Starting server...")
    print("📍 Access the application at: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
