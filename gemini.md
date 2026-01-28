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
1.  **3-Layer A.N.T. Architecture**:
    - **Layer 1: Architecture (`architecture/`)**: Technical SOPs and Prompt Templates.
    - **Layer 2: Navigation (Decision Making)**: `app.py` logic and route handlers.
    - **Layer 3: Tools (`tools/`)**: Atomic, deterministic Python scripts (e.g., `ollama_tool.py`).
2.  **UI/UX**: "Wow" factor design, Glassmorphism, and interactive tables.
3.  **Data-First**: Define schema in `gemini.md` before coding.
4.  **Local Isolation**: Use `.tmp/` for intermediate data and never leak prompts to the cloud.

## Maintenance Log
- **2026-01-27**: Initialized Project via BLAST Protocol.
- **2026-01-27**: Implemented 3-Layer Architecture.
- **2026-01-27**: Deployed Glassmorphism UI.
- **2026-01-28**: Pushed code to GitHub: [LocalLLM-TestCase-Generator](https://github.com/masettinaresh/LocalLLM-TestCase-Generator).
- **2026-01-27**: Final Deployment Checklist Complete.
    - App verified on `localhost:5000`.
    - `llama3.2` model confirmed.
    - `run.bat` auto-setup configured.
