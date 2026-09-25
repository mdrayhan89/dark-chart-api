from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Templates directory link
templates = Jinja2Templates(directory="templates")

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

    return templates.TemplateResponse("index.html", {
        "request": request,
        "symbol": display_symbol
    })
