from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

SUPPORTED_PAIRS = [
    "EUR/USD", "USD/JPY", "CAD/JPY", "AUD/CAD", 
    "GBP/USD", "EUR/JPY", "AUD/JPY", "AUD/USD", 
    "EUR/GBP", "AUD/CHF", "EUR/CAD", "GBP/CAD"
]

@app.get("/", response_class=HTMLResponse)
async def read_chart(request: Request, pair: str = "EUR/USD", symbol: str = None):
    # Determine requested pair (handling ?pair=EUR/USD or ?symbol=EURUSD)
    req_symbol = symbol if symbol else pair
    req_symbol = req_symbol.upper().strip()

    # Format slash if missing (e.g. EURUSD -> EUR/USD)
    if "/" not in req_symbol and len(req_symbol) == 6:
        req_symbol = f"{req_symbol[:3]}/{req_symbol[3:]}"

    is_supported = req_symbol in SUPPORTED_PAIRS

    return templates.TemplateResponse("index.html", {
        "request": request,
        "symbol": req_symbol if is_supported else "UNSUPPORTED PAIR",
        "is_supported": is_supported,
        "supported_list": ", ".join(SUPPORTED_PAIRS)
    })