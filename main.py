from fastapi import FastAPI, HTTPException, Query
import random
import os

app = FastAPI()

# Load API key from Railway environment variables
API_KEY = os.getenv("FASTAPI_SECRET_KEY")

# Ensure API_KEY is set, otherwise raise an error
if not API_KEY:
    raise RuntimeError("❌ FASTAPI_SECRET_KEY is not set in the environment!")

# List of side hustles
side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
]

# List of money-related quotes
money_quotes = [
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don't find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Don't stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It's not about having lots of money. It's about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]

def validate_api_key(api_key: str):
    """Validates the API key and raises an exception if invalid"""
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="❌ Invalid API key!")

@app.get("/side_hustles", summary="Get a random side hustle idea")
def get_side_hustle(api_key: str = Query(..., description="🔑 API key for authentication")):
    validate_api_key(api_key)
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes", summary="Get a random money quote")
def get_money_quote(api_key: str = Query(..., description="🔑 API key for authentication")):
    validate_api_key(api_key)
    return {"money_quote": random.choice(money_quotes)}
