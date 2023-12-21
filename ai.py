import openai

openai.api_key = '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'

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="What dinosaurs lived in the cretaceous period?",
  max_tokens=60
)

print(response['choices'][0]['text'].strip())