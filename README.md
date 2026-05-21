# YouTube Video Analyzer

A simple AI-powered Streamlit application that analyzes YouTube videos using Agno Agents and the Groq LLM. The app accepts a YouTube video URL and generates a structured analysis including summaries, timestamps, themes, and key discussion points.

---

## Developer

**Saurav Kumar**

---

## Features

- YouTube video content analysis
- AI-generated summaries
- Timestamp-based topic breakdown
- Theme and discussion detection
- Streamlit web interface
- Powered by Groq + Agno Agents

---

## Project Structure

```bash
.
├── UI.py
├── youtube_analyzer.py
├── .env
└── README.md
```

### Files

- `UI.py` → Streamlit frontend interface
- `youtube_analyzer.py` → AI Agent configuration and logic
- `.env` → Stores Groq API key securely

---

## Requirements

- Python 3.10+
- streamlit
- python-dotenv
- agno

---

## Install Dependencies

```powershell
pip install streamlit python-dotenv agno
```

---

## Setup Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## Run the Application

```powershell
python -m streamlit run UI.py
```

After running the command, Streamlit will provide a local URL in the terminal.

Example:

```bash
http://localhost:8501
```

Open it in your browser.

---

## How It Works

1. User enters a YouTube video URL
2. Streamlit sends the URL to the Agno AI Agent
3. The Groq model processes the video information
4. The app returns:
   - Summary
   - Key topics
   - Important timestamps
   - Video insights

---

## Technologies Used

- Python
- Streamlit
- Agno SDK
- Groq API
- Llama 3.3 70B Versatile Model

---

## Notes

- Keep your API keys private
- Do not upload `.env` files to GitHub
- Internet connection is required for AI processing

---

## License

This project is created for learning and educational purposes.
