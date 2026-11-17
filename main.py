from openrouter import OpenRouter

API_KEY = ''



with OpenRouter(api_key=API_KEY) as client:
    response = client.responses.send(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        input="Explain quantum computing in one sentence.",
    )
    if response.status != "completed":
        message = response.error.message if response.error else f"Response ended as {response.status}"
        raise RuntimeError(message)

    message = next(item for item in reversed(response.output) if item.type == "message")
    print(next(part.text for part in message.content if part.type == "output_text"))