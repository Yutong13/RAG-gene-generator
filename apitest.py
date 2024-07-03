from openai import OpenAI
with open("secretKey.txt","r") as f:
    client = OpenAI(api_key=f.read())


def generate_answer(question, model="gpt-4o-2024-05-13"):
    response = client.chat.completions.create(model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ],
    max_tokens=150,
    temperature=0.5,
    n=1)
    answer = response.choices[0].message.content.strip()
    return answer

if __name__ == "__main__":
    question = "what is RAG in computer science"
    answer = generate_answer(question)
    print(f"Question: {question}")
    print(f"Answer: {answer}")
