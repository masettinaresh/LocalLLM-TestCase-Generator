# Findings & Research

## 🎯 Discovery (Phase 1)
- **North Star**: A zero-data-leak, local LLM tool for QA engineers to turn requirements into structured test cases instantly.
- **Integrations**: 
    - **Ollama API**: Primary LLM engine (Llama 3.2).
    - **Flask**: Lightweight backend for routing.
- **Source of Truth**: The `prompts/testcase_template.md` serves as the logic blueprint.
- **Delivery Payload**: Markdown Tables displayed in a Glassmorphism UI and exported via `.md` files.

## 🛠️ Technical Research
- **Connection**: Direct HTTP REST calls to `http://localhost:11434/api/generate` are more stable and lighter than using the `ollama-python` library for this scope.
- **Prompting**: Llama 3.2 responds best to structured Markdown instructions. Using `<br>` tags in the prompt ensures multi-line steps are preserved in Markdown tables.

## ⚠️ Known Constraints & Discoveries
- **Console Encoding**: Windows PowerShell/CMD requires ASCII-based status indicators (`[OK]`) instead of Emojis to prevent `UnicodeEncodeError`.
- **Static Assets**: Flask requires absolute or relative paths starting with `/static/` when `send_static_file` is used to avoid 404s on CSS/JS.
- **Resource Usage**: Running `llama3.2` locally requires ~4GB of VRAM/RAM for smooth inference.

