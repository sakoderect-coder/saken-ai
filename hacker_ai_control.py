import ollama

def ask_hacker_ai(prompt):
    # Используем созданную нами модель
    response = ollama.chat(model='hacker_ai', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return response['message']['content']

print("--- HACKER AI INTERFACE LOADED ---")
print("Пример: 'Проанализируй этот IP 192.168.1.1' или 'Напиши скрипт для брутфорса'")

while True:
    user_input = input("\n[Target/Task]> ")
    if user_input.lower() in ['exit', 'quit']:
        break
        
    print("\n[Анализ ИИ]:")
    result = ask_hacker_ai(user_input)
    print(result)
