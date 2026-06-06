# 🏠 AI House Planning Assistant

An AI-powered chatbot that helps users plan their house by generating layout ideas, cost estimates, and material requirements based on minimal input.

---

## 🚀 Features

- 🧠 AI-generated house planning suggestions  
- 📐 Basic layout recommendations  
- 💰 Cost estimation (based on Indian standards)  
- 🧱 Material requirement calculation  
- 🎨 Interior design ideas  
- ⚡ Fast and simple user interaction  

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)  
- **AI Integration:** OpenRouter (Claude 3 Haiku / GPT-based models)  
- **Frontend:** HTML, CSS, JavaScript  
- **API Handling:** REST APIs  

---

## ⚙️ How It Works

1. User enters plot size (e.g., 1000 sq ft)  
2. Frontend sends request to FastAPI backend  
3. Backend processes input and sends prompt to AI model  
4. AI generates layout and design suggestions  
5. Backend calculates cost and materials using logic  
6. Final structured response is returned to user  

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


2. Create virtual environment

    python3 -m venv .venv
    source .venv/bin/activate   # Mac/Linux
    .venv\Scripts\activate      # Windows

3. Install dependencies
    pip install -r requirements.txt

4. Add environment variables
    Create a .env file:
    OPENROUTER_API_KEY=your_api_key_here\

5. Run backend server
    uvicorn main:app --reload

6. Run frontend
    python3 -m http.server 8000