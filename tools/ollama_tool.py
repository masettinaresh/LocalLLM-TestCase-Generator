import requests
import json
import os

class OllamaTool:
    def __init__(self, model="llama3.2", api_url="http://localhost:11434/api/generate"):
        self.model = model
        self.api_url = api_url

    def generate(self, prompt):
        """
        Generates text using Ollama.
        Returns: (response_text, error_message)
        """
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(self.api_url, json=payload)
            if response.status_code == 404:
                return None, f"Model '{self.model}' not found. Please run: ollama pull {self.model}"
            response.raise_for_status()
            result = response.json()
            return result.get("response", ""), None
            
        except requests.exceptions.ConnectionError:
            return None, "Could not connect to Ollama. Is it running at localhost:11434?"
        except Exception as e:
            return None, str(e)

# Self-test block
if __name__ == "__main__":
    tool = OllamaTool()
    print("Testing Ollama connection...")
    resp, err = tool.generate("Say hello")
    if err:
        print(f"Error: {err}")
    else:
        print(f"Success: {resp}")
