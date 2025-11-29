
# **AI Blog Paragraph Generator**

A simple Python project that uses the **OpenAI API** to generate a blog-style paragraph from any topic input.
This project demonstrates how to connect to the OpenAI Completion API, send prompts, and process AI-generated responses.

---

## **📌 Features**

* Generate a paragraph on any topic
* Uses **GPT-3.5-Turbo-Instruct** model
* Easy-to-understand Python code
* Beginner-friendly OpenAI API integration

---

## **📁 Project Structure**

```
/blog-generator
│── main.py        # Core Python script with API call
│── README.md      # Documentation
```

---

## **🛠️ Installation & Setup**

### **1. Install OpenAI library**

```bash
pip install openai
```

### **2. Add your OpenAI API key**

In `main.py`:

```python
openai.api_key = "your_api_key_here"
```

⚠️ **Important:**
Do NOT upload your actual API key to GitHub.
Use environment variables in real projects.

---

## **🚀 Usage**

Run the script:

```bash
python main.py
```

Example call inside code:

```python
print(generate_blog("Why NYC is better than your city."))
```

Output will be an AI-generated paragraph based on the topic you provide.

---

## **🧠 Code Overview**

```python
def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt='Write a paragraph about the following topic. ' + paragraph_topic,
        max_tokens=400,
        temperature=0.3
    )

    retrieve_blog = response.choices[0].text
    return retrieve_blog
```

---

## **🌱 Future Enhancements**

* Add UI using Flask/Streamlit
* Add multiple paragraph output
* Add tone selector (formal, funny, professional)
* Export output as PDF or text file

---

## **📜 License**

This project is open-source and free for learning purposes.

---
