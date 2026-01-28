# Project Constitution

## Data Schemas
### TestCaseRequest
- **Source**: User Input (UI)
- **Structure**:
  ```json
  {
    "user_input": "string",
    "model": "llama3.2"
  }
  ```

### TestCaseResponse
- **Source**: Ollama (LLM)
- **Structure**:
  ```json
  {
    "generated_testcases": "string (markdown)",
    "status": "success|error"
  }
  ```

## Behavioral Rules
1.  **Model**: Strictly use `llama3.2` via Ollama.
2.  **Interface**: Web-based Chat UI (HTML/CSS/JS).
3.  **Tone**: Professional, precise QA/Test Engineering tone.
4.  **Template**: Use a predefined "Test Case Generation" system prompt (to be defined).

## Architectural Invariants
1.  **3-Layer Architecture**:
    - **Layer 1: Architecture (SOPs)**: `prompts/` (The "Template"), `sops/` (Logic definitions).
    - **Layer 2: Navigation (Backend)**: Python Server (e.g., Flask/FastAPI) to bridge UI and Tools.
    - **Layer 3: Tools**: `tools/ollama_client.py` (Atomic Ollama interaction).
2.  **UI/UX**: "Wow" factor, modern aesthetics, responsive chat interface.
3.  **Data-First**: Validate input before sending to LLM.

## Maintenance Log
- **2026-01-27**: Initialized Project via BLAST Protocol.
- **2026-01-27**: Implemented 3-Layer Architecture.
- **2026-01-27**: Deployed Glassmorphism UI.
- **2026-01-27**: Final Deployment Checklist Complete.
    - App verified on `localhost:5000`.
    - `llama3.2` model confirmed.
    - `run.bat` auto-setup configured.
