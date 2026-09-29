# Gemini API App

A simple Python application that integrates the **Google Gemini API** to generate AI-powered responses.

## 🚀 Features

* Integrates Google Gemini API with Python
* Generates AI responses from user prompts
* Uses `.env` for secure API key management
* Simple and beginner-friendly project structure

## 🛠️ Technologies Used

* Python
* Google Gemini API
* python-dotenv

## 📁 Project Structure

```text
gemini-api-app/
│
├── app.py
├── .env
├── .gitignore
└── venv/
```

> `.env` and `venv/` are excluded from GitHub using `.gitignore`.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/vikashkumar12a/gemini-api-app.git
cd gemini-api-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create `.env`

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

### 6. Run the application

```bash
python app.py
```

## 🔐 Security

Never upload your API key to GitHub.

The `.env` file is included in `.gitignore` so that sensitive credentials are not committed to the repository.

## 📌 Purpose

This project was created to learn and practice:

* API integration
* Environment variables
* Python virtual environments
* Git and GitHub
* Generative AI application development

## 👨‍💻 Author

**Vikash Kumar**

GitHub: [@vikashkumar12a](https://github.com/vikashkumar12a)

---

⭐ If you find this project useful, feel free to explore the repository.
