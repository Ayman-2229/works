# 💰 Expense Explainer Bot v2

An AI-powered tool to **understand**, **analyze**, and **forecast** personal or business expenses from CSV files — all running **locally** without OpenAI API keys.

---

## 🧠 Goal

Help users (especially freelancers, students, or small business owners) gain insights into their spending habits, detect recurring charges, and prepare for upcoming expenses using lightweight, explainable AI.

---

## 💡 How It Works

1. Upload a CSV file with columns: `date`, `description`, and `amount`.
2. The app:
   - Categorizes transactions using rule-based NLP with keyword matching.
   - Detects recurring patterns (e.g., subscriptions like Netflix, Rent, EMI).
   - Generates a sentiment-based summary of spending using Hugging Face sentiment models.
   - Forecasts future expenses using rolling averages and time-series trend analysis.
   - Exports a clean and informative PDF report summarizing the analysis.

---

## 🧩 Core Components

- **main.py**: Streamlit UI handling user interactions and displaying results.
- **components/ai_engine.py**: Core AI logic including expense explanation, categorization, forecasting, and summary generation.
- **components/ai_categorizer.py**: Rule-based NLP categorization of expenses.
- **components/budget_coach.py**: Provides budget insights and spending analysis.
- **components/pdf_export.py**: Generates PDF reports of the expense summaries.
- **components/file_parser.py**: Parses uploaded CSV files and extracts relevant data.
- **components/recurring_detector.py**: Detects recurring expenses from transaction data.
- **components/file_merger.py**: Supports merging multiple CSV files for consolidated analysis.
- **utils/**: Utility functions for visuals, database interactions, and configuration.
- **styles.css**: Custom CSS for dark mode and UI styling.

---

## 🧩 Features

| Feature | Description |
|--------|-------------|
| 📤 CSV Upload | Accepts user-defined transaction data with date, description, and amount columns. |
| 💬 AI-Powered Summary | Uses Hugging Face sentiment models to provide sentiment analysis on transactions. |
| 🏷️ Smart Categorization | Rule-based NLP tags expenses into categories like Food, Transport, Shopping, Utilities, Entertainment. |
| 🔁 Recurring Detector | Flags subscriptions and recurring charges for better expense tracking. |
| 📈 Expense Forecasting | Predicts future spending trends using rolling averages and time-series analysis. |
| 📎 PDF Export | Generates professional summary reports in PDF format. |
| 🌙 Dark Mode | Sleek UI using custom Streamlit CSS for better user experience. |
| 🧠 Low-Spec Optimized | Runs efficiently on systems with ~4GB RAM. |
| 🗃 Multi-file Support | Ability to merge and analyze multiple CSV files. |
| 🧑‍💼 User Profiles (v3) | Planned feature to support user-specific history and personalized insights. |

---

## 🗂 Folder Structure

```
expense-explainer-bot/
├── main.py                 # Streamlit UI
├── components/             # Core AI and app components
│   ├── ai_engine.py        # AI logic: explanation, categorization, forecasting, summary
│   ├── ai_categorizer.py   # Rule-based NLP categorization
│   ├── budget_coach.py     # Budget insights and analysis
│   ├── pdf_export.py       # PDF report generation
│   ├── file_parser.py      # CSV parsing
│   ├── recurring_detector.py # Recurring expense detection
│   ├── file_merger.py      # Multi-file merging support
├── utils/                  # Utility modules for visuals, database, config
├── styles.css              # Custom CSS for UI styling and dark mode
├── assets/                 # UI assets like banner images
├── data/                   # Sample CSV files (optional)
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files
└── README.md               # Project documentation
```

---

## 🖥️ Technologies Used

- **Python 3.9+**
- **Streamlit** – Interactive web UI
- **Pandas** – CSV and data wrangling
- **Hugging Face Transformers** – Sentiment analysis and summarization
- **SentencePiece** – Lightweight tokenizer (optional)
- **FPDF** – PDF generation

---

## 📃 Sample CSV Input

```csv
date,description,amount
2024-06-01,Swiggy Order,450
2024-06-02,Netflix Subscription,500
2024-06-03,Zomato Gold,299
```

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/expense-explainer-bot.git
cd expense-explainer-bot

# 2. Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run main.py
```

---

## 📤 Optional .env Support

You can optionally include a `.env` file for future enhancements (e.g., API keys, DB configs):

```ini
API_KEY=your_optional_key
DB_URI=sqlite:///expenses.db
```

---

## 📝 License

**MIT** – Free to use for personal or educational projects.

---

## 👤 Made by Ayman

📧 [YourEmail@example.com]  
🌐 [YourPortfolioLink]

---

> Want to deploy this to Hugging Face Spaces or Replit? Let me know — it's fully compatible!
>>>>>>> cc0242d (Initial commit)
=======
=======
# 💰 Expense Explainer Bot v2

An AI-powered tool to **understand**, **analyze**, and **forecast** personal or business expenses from CSV files — all running **locally** without OpenAI API keys.

---

## 🧠 Goal

Help users (especially freelancers, students, or small business owners) gain insights into their spending habits, detect recurring charges, and prepare for upcoming expenses using lightweight, explainable AI.

---

## 💡 How It Works

1. Upload a CSV file with columns: `date`, `description`, and `amount`.
2. The app:
   - Categorizes transactions using rule-based NLP with keyword matching.
   - Detects recurring patterns (e.g., subscriptions like Netflix, Rent, EMI).
   - Generates a sentiment-based summary of spending using Hugging Face sentiment models.
   - Forecasts future expenses using rolling averages and time-series trend analysis.
   - Exports a clean and informative PDF report summarizing the analysis.

---

## 🧩 Core Components

- **main.py**: Streamlit UI handling user interactions and displaying results.
- **components/ai_engine.py**: Core AI logic including expense explanation, categorization, forecasting, and summary generation.
- **components/ai_categorizer.py**: Rule-based NLP categorization of expenses.
- **components/budget_coach.py**: Provides budget insights and spending analysis.
- **components/pdf_export.py**: Generates PDF reports of the expense summaries.
- **components/file_parser.py**: Parses uploaded CSV files and extracts relevant data.
- **components/recurring_detector.py**: Detects recurring expenses from transaction data.
- **components/file_merger.py**: Supports merging multiple CSV files for consolidated analysis.
- **utils/**: Utility functions for visuals, database interactions, and configuration.
- **styles.css**: Custom CSS for dark mode and UI styling.

---

## 🧩 Features

| Feature | Description |
|--------|-------------|
| 📤 CSV Upload | Accepts user-defined transaction data with date, description, and amount columns. |
| 💬 AI-Powered Summary | Uses Hugging Face sentiment models to provide sentiment analysis on transactions. |
| 🏷️ Smart Categorization | Rule-based NLP tags expenses into categories like Food, Transport, Shopping, Utilities, Entertainment. |
| 🔁 Recurring Detector | Flags subscriptions and recurring charges for better expense tracking. |
| 📈 Expense Forecasting | Predicts future spending trends using rolling averages and time-series analysis. |
| 📎 PDF Export | Generates professional summary reports in PDF format. |
| 🌙 Dark Mode | Sleek UI using custom Streamlit CSS for better user experience. |
| 🧠 Low-Spec Optimized | Runs efficiently on systems with ~4GB RAM. |
| 🗃 Multi-file Support | Ability to merge and analyze multiple CSV files. |
| 🧑‍💼 User Profiles (v3) | Planned feature to support user-specific history and personalized insights. |

---

## 🗂 Folder Structure

```
expense-explainer-bot/
├── main.py                 # Streamlit UI
├── components/             # Core AI and app components
│   ├── ai_engine.py        # AI logic: explanation, categorization, forecasting, summary
│   ├── ai_categorizer.py   # Rule-based NLP categorization
│   ├── budget_coach.py     # Budget insights and analysis
│   ├── pdf_export.py       # PDF report generation
│   ├── file_parser.py      # CSV parsing
│   ├── recurring_detector.py # Recurring expense detection
│   ├── file_merger.py      # Multi-file merging support
├── utils/                  # Utility modules for visuals, database, config
├── styles.css              # Custom CSS for UI styling and dark mode
├── assets/                 # UI assets like banner images
├── data/                   # Sample CSV files (optional)
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files
└── README.md               # Project documentation
```

---

## 🖥️ Technologies Used

- **Python 3.9+**
- **Streamlit** – Interactive web UI
- **Pandas** – CSV and data wrangling
- **Hugging Face Transformers** – Sentiment analysis and summarization
- **SentencePiece** – Lightweight tokenizer (optional)
- **FPDF** – PDF generation

---

## 📃 Sample CSV Input

```csv
date,description,amount
2024-06-01,Swiggy Order,450
2024-06-02,Netflix Subscription,500
2024-06-03,Zomato Gold,299
```

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/expense-explainer-bot.git
cd expense-explainer-bot

# 2. Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run main.py
```

---

## 📤 Optional .env Support

You can optionally include a `.env` file for future enhancements (e.g., API keys, DB configs):

```ini
API_KEY=your_optional_key
DB_URI=sqlite:///expenses.db
```

---

## 📝 License

**MIT** – Free to use for personal or educational projects.

---

## 👤 Made by Ayman

📧 [YourEmail@example.com]  
🌐 [YourPortfolioLink]

---

> Want to deploy this to Hugging Face Spaces or Replit? Let me know — it's fully compatible!
>>>>>>> cc0242d (Initial commit)
