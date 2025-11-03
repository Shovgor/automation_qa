# 🧪 Automation QA Home Test

### 🧩 Overview
Unified automation project containing both **API** and **UI** test coverage using **Pytest** and **Playwright**.

---

## ⚙️ Installation

Before running the tests, set up your environment:

```bash
# 1️⃣ Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# 2️⃣ Install all dependencies
pip install -r requirements.txt

# 3️⃣ Install Playwright browsers (only once)
playwright install
```

---

## 🚀 How to Run

### API Tests
```bash
pytest tests/api
```

### UI Tests
```bash
pytest tests/ui --headed --browser chromium
```

## 🎬 Demo

Here’s a quick look at the automated test in action:

![Automation Demo](./demo.gif)