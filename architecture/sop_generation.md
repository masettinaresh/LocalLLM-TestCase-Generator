# SOP: Test Case Generation

## Goal
Generate comprehensive QA test cases (Positive, Negative, Edge, Security) from natural language requirements using a local LLM.

## Inputs
- `user_input` (string): The feature description or requirement.
- `model` (string): The Ollama model to use (default: `llama3.2`).
- `template_path` (string): Path to the system prompt template.

## Logic (The "Algorithm")
1.  **Validate Input**: Ensure `user_input` is not empty.
2.  **Load Template**: Read the markdown template from `prompts/testcase_template.md`.
3.  **Construct Prompt**: Replace `{{user_input}}` in the template with the actual user input.
4.  **Call LLM**: Send the prompt to Ollama API (`/api/generate`).
5.  **Format Output**: Return the raw markdown response.

## Edge Cases
- **Ollama Offline**: If connection fails, return a 503 error with a helpful message.
- **Model Missing**: If `llama3.2` is not pulled, return a 500 error instructing to pull it.
- **Empty Output**: If LLM returns empty string, retry once or return error.
