📝 AI Blog Paragraph Generator

A simple Python project that uses the OpenAI API to generate a short blog-style paragraph on any topic.

This project demonstrates how to integrate the OpenAI Completion API (instruct model) into Python, send prompts, and retrieve AI-generated text. It’s ideal for beginners exploring API usage and text generation models.

🚀 Features

Generate a blog-style paragraph for any topic

Uses OpenAI GPT-3.5-Turbo-Instruct model

Simple function-based implementation

Easy to customize for larger applications

📂 Project Structure
blog-generator/
│
├── main.py        # Contains the API call and paragraph generator function
└── README.md      # Project documentation

🧠 How It Works

The project sends a prompt to the OpenAI API with the topic provided by the user.

def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text
  return retrieve_blog


The model returns a text response, which is printed as the generated blog paragraph.

🛠️ Setup Instructions
1. Install dependencies
pip install openai

2. Add your API key

Replace the value of openai.api_key in the script:

openai.api_key = "your_api_key_here"


⚠️ Never commit your real API key to GitHub
Use environment variables instead.

▶️ Run the Project
python main.py


Example Output:

Why NYC is better than your city.
<AI-generated paragraph here>

📌 Future Improvements

Add GUI or web interface

Convert into a Flask or FastAPI API

Add dropdown for writing tone (funny, formal, academic)

Allow long-form blog generation (multiple paragraphs)

📜 License

This project is for learning purposes and free to use.
