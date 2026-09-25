from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

SUPPORTED_PAIRS = [
    "EUR/USD", "USD/JPY", "CAD/JPY", "AUD/CAD", 
    "GBP/USD", "EUR/JPY", "AUD/JPY", "AUD/USD", 
    "EUR/GBP", "AUD/CHF", "EUR/CAD", "GBP/CAD"
]

@app.get("/", response_class=HTMLResponse)
async def read_chart(request: Request, pair: str = "EUR/USD", symbol: str = None):
    req_symbol = symbol if symbol else pair
    req_symbol = req_symbol.upper().strip()

    if "/" not in req_symbol and len(req_symbol) == 6:
        req_symbol = f"{req_symbol[:3]}/{req_symbol[3:]}"

    is_supported = req_symbol in SUPPORTED_PAIRS
    display_symbol = req_symbol if is_supported else "EUR/USD"

    html_content = f"""
    
    
    
      
      
      {display_symbol} - Dark Secret Chart
      
      
    
    
{display_symbol}

👑 DARK SECRET 👑

SIGNAL: --

"""
return html_content
