import ollama


def ollama_response(person_ask: str):
    # If Ollama is a separate container named "ollama" in the same network:
    client = ollama.Client(host="http://0.0.0.0:11434")

    # OR if Ollama is running on your Mac/Windows host:
    # client = ollama.Client(host='http://host.docker.internal:11434')

    response = client.chat(
        model="tinyllama:1.1b",
        messages=[
            {
                "role": "system",
                "content": "You are a movie expert. Recommend 3 movies based on user favorites. Keep it short.",
            },
            {
                "role": "user",
                "content": f"I like these movies: {person_ask}. What should I watch next?",
            },
        ],
    )
    print(response)
    return response.message.content
