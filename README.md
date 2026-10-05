# AI Company Brochure Generator

A GenAI application that takes a company name and landing-page URL, extracts the website content, and uses an LLM to generate a company brochure — in either a **formal** or **humorous** style.

Built with Python, Gradio, and the NVIDIA NIM API (Nemotron model) as a learning/portfolio project during an LLM engineering course.

---

## Features

- **Website content extraction** – `scraper.py` fetches and cleans the target company's landing page using `requests` and `BeautifulSoup`
- **Two brochure styles** – choose between a formal, professional tone or a humorous, entertaining tone
- **LLM-powered generation** – uses NVIDIA's Nemotron model via the OpenAI-compatible NVIDIA NIM API
- **Streaming responses** – the brochure is streamed token-by-token and displayed live in the UI
- **Gradio interface** – simple browser-based UI with example inputs to get started quickly

---

## Architecture

```
Company Name + Website URL
            |
       scraper.py
    (requests + BeautifulSoup)
            |
    Website Content (text)
            |
    Prompt Construction
            |
 Formal / Humorous Mode
            |
      NVIDIA NIM API
            |
   Nemotron LLM Response
            |
      Streaming Output
            |
        Gradio UI
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| UI | [Gradio](https://gradio.app/) |
| LLM API | [NVIDIA NIM (OpenAI-compatible)](https://integrate.api.nvidia.com) |
| Model | `nvidia/nemotron-super-49b-v1` |
| API Client | `openai` Python package |
| Web scraping | `requests` + `beautifulsoup4` |
| Secrets | `python-dotenv` |

---

## Project Structure

```
AI-Company-Brochure-Generator/
├── app.py            # Main Gradio application
├── scraper.py        # Website content fetching and extraction
├── requirements.txt  # Python dependencies
├── .env.example      # Template for environment variables
├── .gitignore        # Excludes secrets, caches, and virtual environments
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Company-Brochure-Generator.git
cd AI-Company-Brochure-Generator
```

### 2. Create and activate a virtual environment

```bash
# Create
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS / Linux)
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Copy the example environment file and add your NVIDIA API key:

```bash
cp .env.example .env
```

Then open `.env` and replace the placeholder:

```
NVIDIA_API_KEY=your_nvidia_api_key_here
```

You can get a free NVIDIA NIM API key at [https://build.nvidia.com](https://build.nvidia.com).

---

## Running the Application

```bash
python app.py
```

Gradio will start a local server. Open the URL shown in your terminal (usually `http://127.0.0.1:7860`) in your browser.

---

## Usage

1. Enter the **company name** in the first text box
2. Enter the company's **landing page URL** (must start with `http://` or `https://`)
3. Select a **brochure style** — `humoured` or `formal`
4. Click **Submit**
5. Watch the brochure stream into the output panel in real time

You can also click one of the built-in **Examples** to try it immediately.

---

## Project Purpose

This project was built as a hands-on learning exercise during an LLM engineering course. The goals were to practice:

- **LLM API integration** – connecting to an external model API using the OpenAI client
- **Prompt and system-message design** – crafting prompts that produce different tones and styles
- **Streaming responses** – handling generator-based streaming from an LLM API
- **Gradio interfaces** – building a simple but functional browser UI around a Python function
- **Website content extraction** – fetching and cleaning real web content to use as LLM context
- **Connecting components end-to-end** – combining scraping, prompting, and streaming into a complete GenAI application

---

## Limitations

- **Website accessibility** – some sites block automated requests or serve JavaScript-rendered content that `requests` cannot retrieve. Static HTML sites work best.
- **Content truncation** – `scraper.py` truncates extracted text to 2,000 characters to keep prompts within reasonable limits. Very large sites will be partially summarised.
- **NVIDIA API key required** – you need a free NVIDIA NIM API key to run this application.
- **Output accuracy** – the brochure is LLM-generated from scraped text. Results should be reviewed for accuracy before any real use.
- **Single-page scraping** – only the provided landing page URL is scraped; the tool does not crawl additional pages.

---

## License

This project is for educational and portfolio purposes.
