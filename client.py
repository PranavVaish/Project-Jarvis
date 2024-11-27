from openai import OpenAI
client = OpenAI(
  api_key="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"
)
completion = client.chat.completions.create(
  model="o1-preview-2024-09-12",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud."},
    {"role": "user", "content": "What is coding"}
  ]
)

print(completion.choices[0].message.content)

#print(completion.choices[0].message)