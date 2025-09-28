from gpt4all import GPT4All

model = GPT4All(
    model_name="Llama-3.2-3B-Instruct-Q4_0.gguf",
    model_path=rmodel_path = "C:/Users/HP/AppData/Local/nomic.ai/GPT4All/Llama-3.2-3B-Instruct-Q4_0.gguf"
,
    
  backend="gptj"
)

print("????? FADO EH Assistant is ready! (Type 'exit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("FADO: Goodbye! Stay healthy.")
        break

    response = model.generate(user_input)
    print("FADO:", response)
















from gpt4all import GPT4All


model = GPT4All("qwen2-1_5b-instruct-q4_0.gguf")

print("?? FADO AI is ready. Type your question (type 'exit' to quit).")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("?? Goodbye from FADO AI!")
        break

    response = model.generate(user_input)
    print("FADO AI:", response)













from gpt4all import GPT4All


model = GPT4All("qwen2-1_5b-instruct-q4_0.gguf")

print("💬 FADO AI is ready. Type your question (type 'exit' to quit).")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye from FADO AI!")
        break

    response = model.generate(user_input)
    print("FADO AI:", response)














fado ai advance terminal chat box code 


from gpt4all import GPT4All
import time

# Load model
model = GPT4All("qwen2-1_5b-instruct-q4_0.gguf")

# Intro
print("=" * 50)
print("🤖 FADO AI - Your Environmental Health Assistant")
print("💬 Ask me anything related to health, hygiene, safety.")
print("💡 Type 'exit' to quit.")
print("=" * 50)

while True:
    try:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye from FADO AI. Stay safe!")
            break

        print("FADO AI is thinking...\n")
        response = model.generate(user_input, max_tokens=500)

        # Simulate typing effect
        for char in response:
            print(char, end="", flush=True)
            time.sleep(0.01)

    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
        continue
