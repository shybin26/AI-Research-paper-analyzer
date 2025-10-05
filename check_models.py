import google.generativeai as genai

# PASTE YOUR GOOGLE AI API KEY HERE
GOOGLE_API_KEY = 'AIzaSyB90kC8N03pwrQlUWmyWDoNZ8U8R6L0SiE'

genai.configure(api_key=GOOGLE_API_KEY)

print("Fetching available models...")

# This loop will go through all available models and print their names
for m in genai.list_models():
  # We check if 'generateContent' is a supported method for the model
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)