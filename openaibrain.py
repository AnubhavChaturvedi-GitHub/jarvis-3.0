import openai

# Set your OpenAI API key
api_key = '"  # Replace with your actual API key

# Initialize the OpenAI client
openai.api_key = api_key


def chat_with_ai(role, prompt):
    role = "AI Assistant named Jarvis. Avoid revealing personal details unless asked directly. Respond in English, limit to 1 or 2 sentences. Your creator is Anubhav Chaturvedi, referred to as Sir Zeno."
    full_prompt = f"{role} Question: {prompt}."

    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose the GPT-3 engine you prefer
        prompt=full_prompt,  # Pass the modified prompt
        max_tokens=60,  # You can adjust the response length as needed
        temperature=0.6,  # Adjust the temperature for creativity
    )
    return response.choices[0].text.strip()