from dotenv import load_dotenv, find_dotenv
import os
import requests
_ = load_dotenv(find_dotenv())

together_api_key = os.getenv("TOGETHER_API_KEY")

url = "https://api.together.xyz/inference"

headers = {
    "Authorization": f"Bearer {together_api_key}",
    "Content-Type": "application/json"
}

model = "togethercomputer/llama-2-7b-chat"
prompt = """Please write me a birthday card for my dear friend, Suraj"""
prompt = f"[INST]{prompt}[/INST]"
temperature = 0.0
max_tokens = 1024

data = {
    "model": model,
    "prompt": prompt,
    "temperature": temperature,
    "max_tokens": max_tokens
}


def main():
    print("Hello from llama-project!")
    response = requests.post(url, headers=headers, json=data)
    # print(response.json()["output"]["choices"][0]["text"])
    print(response)


if __name__ == "__main__":
    main()
