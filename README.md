# Brutally Honest Indian Car Advisor

A command-line tool that gives you **zero-filter, straight-to-the-point** advice on whether the car you're eyeing is actually worth it for the average Indian buyer — powered by GPT-4.1 and OpenAI function calling.

---

## What It Does

You tell it which car you're considering. It tells you the truth — no sugarcoating.

- ✅ Good value car under ₹20 lakhs? It'll hype you up.
- ❌ Eyeing a used BMW for ₹18 lakhs? It'll roast you for the maintenance bills you're about to inherit.
- 💸 Anything above ₹20 lakhs? It'll tell you to reconsider, respectfully (or not).

---

##  Tech Stack

- **Python 3.x**
- **OpenAI Python SDK** (`openai`)
- **GPT-4.1** via OpenAI Chat Completions API
- **Function Calling / Tool Use** for structured output

---

##  Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/indian-car-advisor.git
cd indian-car-advisor
```

### 2. Install dependencies

```bash
pip install openai
```

### 3. Add your OpenAI API key

Open the script and replace the empty string with your key:

```python
openai_client = OpenAI(api_key="your-api-key-here")
```

> **Tip:** Use an environment variable instead of hardcoding:
> ```python
> import os
> openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
> ```

---

##  Usage

```bash
python car_advisor.py
```

You'll be prompted:

```
Which car are you looking for?
> Maruti Suzuki Swift
```

**Example outputs:**

```
Good job, thats a great car choice!!
Solid pick! The Swift is reliable, fuel-efficient, and has excellent resale value. Spare parts are cheap and available everywhere. Keep going!
fin.
```

```
Oh no, Re-evaluate your choices you broke man!
A used E-Class under 20 lakhs? Bro, the annual maintenance alone will eat your salary. Walk away. NOW.
fin.
```

---

##  How It Works

The script uses **OpenAI function calling** (tool use) to force the model to return structured output — a boolean verdict and a blunt message — instead of freeform text.

```
User Input
    │
    ▼
GPT-4.1 (with tool: buget_indian_cars)
    │
    ▼
{ budget_friendly_car: bool, note_to_user: string }
    │
    ▼
Verdict + Roast printed to terminal
```

---

##  Project Structure

```
indian-car-advisor/
├── car_advisor.py   # Main script
└── README.md
```

---

## ⚠️ Disclaimer

This tool is for entertainment and general guidance only. Always do your own research before making any actual car purchase. The AI does not know your specific financial situation, location, or negotiation skills.

---

## 📄 License

MIT
