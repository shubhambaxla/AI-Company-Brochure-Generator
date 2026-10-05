import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from scraper import fetch_website_contents

# Load environment variables from .env
load_dotenv()

# Set up the NVIDIA OpenAI-compatible client
nvidia = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

MODEL = "nvidia/nemotron-super-49b-v1"


def humoured(chat):
    """
    Generate a brochure in a humorous style using the NVIDIA Nemotron model.
    Streams the response token by token.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are a brochure generator that creates brochures based on "
                "user-provided content in a humorous and entertaining way."
            )
        },
        {"role": "user", "content": chat}
    ]

    stream = nvidia.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True
    )

    result = ""
    for chunk in stream:
        # Guard against empty chunks (no choices) to prevent IndexError
        if chunk.choices and chunk.choices[0].delta.content:
            result += chunk.choices[0].delta.content
        yield result


def formal(chat):
    """
    Generate a brochure in a formal, professional style using the NVIDIA Nemotron model.
    Streams the response token by token.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are a brochure generator that creates brochures based on "
                "user-provided content in a formal, professional manner."
            )
        },
        {"role": "user", "content": chat}
    ]

    stream = nvidia.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True
    )

    result = ""
    for chunk in stream:
        # Guard against empty chunks (no choices) to prevent IndexError
        if chunk.choices and chunk.choices[0].delta.content:
            result += chunk.choices[0].delta.content
        yield result


def stream_brochure(company_name, url, style):
    """
    Main orchestration function called by the Gradio interface.

    1. Builds a prompt from the company name and scraped website content.
    2. Routes to humoured() or formal() based on the selected style.
    3. Streams the LLM response back to Gradio.
    """
    yield ""

    prompt = f"Please generate a company brochure for {company_name}. Here is their landing page:\n"
    prompt += fetch_website_contents(url)

    if style == "humoured":
        result = humoured(prompt)
    elif style == "formal":
        result = formal(prompt)
    else:
        raise ValueError(f"Unknown style: {style}")

    yield from result


# --- Gradio UI components ---
name_input = gr.Textbox(label="Company Name")
url_input = gr.Textbox(label="Landing Page URL (include http:// or https://)")
style_selector = gr.Dropdown(
    ["humoured", "formal"],
    label="Brochure Style",
    value="humoured"
)
brochure_output = gr.Markdown(label="Generated Brochure")

# --- Build and launch the Gradio interface ---
view = gr.Interface(
    fn=stream_brochure,
    title="AI Company Brochure Generator",
    inputs=[name_input, url_input, style_selector],
    outputs=[brochure_output],
    examples=[
        ["Hugging Face", "https://huggingface.co", "humoured"],
        ["Edward Donner", "https://edwarddonner.com", "formal"],
    ],
    flagging_mode="never"
)

if __name__ == "__main__":
    view.launch()
