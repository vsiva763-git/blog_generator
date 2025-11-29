import openai

openai.api_key = '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' # Fill in your own key

def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text

  return retrieve_blog

print(generate_blog('Why NYC is better than your city.'))
