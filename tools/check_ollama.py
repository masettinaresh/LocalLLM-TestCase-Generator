import requests
import sys

def check_ollama(model="llama3.2"):
    try:
        # Check if Ollama is running
        print(f"Checking if Ollama is running at http://localhost:11434...")
        response = requests.get("http://localhost:11434/")
        if response.status_code == 200:
            print("[OK] Ollama is running.")
        else:
            print(f"[FAIL] Ollama returned status code: {response.status_code}")
            return False

        # Check if model exists
        print(f"Checking for model '{model}'...")
        tags_response = requests.get("http://localhost:11434/api/tags")
        tags = tags_response.json().get('models', [])
        model_found = any(m['name'].startswith(model) for m in tags)
        
        if model_found:
            print(f"[OK] Model '{model}' found.")
            return True
        else:
            print(f"[FAIL] Model '{model}' NOT found. Please run `ollama pull {model}`")
            return False

    except requests.exceptions.ConnectionError:
        print("[FAIL] Could not connect to Ollama. Is it running?")
        return False
    except Exception as e:
        print(f"[FAIL] Error: {e}")
        return False

if __name__ == "__main__":
    success = check_ollama()
    if not success:
        sys.exit(1)
