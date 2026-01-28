# Project Plan: Local LLM TestCase Generator

## Phases
- [x] **Phase 1: Blueprint (Vision & Logic)**
    - [x] Discovery Questions
    - [x] Data Schema Definition (gemini.md)
    - [x] Obtain/Define "The Template" (System Prompt)
    - [x] Research: Flask/FastAPI vs others for local backend? (Decision: Flask for simplicity + file serving)
- [x] **Phase 2: Link (Connectivity)**
    - [x] `tools/check_ollama.py`: Verify Ollama is running and `llama3.2` is pulled.
    - [x] `tools/llm_handshake.py`: Verified via `tools/ollama_tool.py` self-test.
- [x] **Phase 3: Architect (The 3-Layer Build)**
    - [x] **Layer 1 (Architecture)**: Create `prompts/testcase_template.md` & `architecture/sop_generation.md`.
    - [x] **Layer 3 (Tools)**: Create `tools/ollama_tool.py` (atomic class).
    - [x] **Layer 2 (Navigation)**: Refactor `app.py` to use `OllamaTool`.
- [x] **Phase 4: Stylize (Refinement & UI)**
    - [x] **Assets**: UI icons/assets handled via CSS/Emoji.
    - [x] **Frontend**: Refined `index.html`, `style.css`, `script.js` with Glassmorphism & Table Styles.
    - [x] **Design**: "Download Report" feature added.
    - [x] **Payload Refinement**: Updated `prompts/testcase_template.md` for professional Table output.
- [x] **Phase 5: Trigger (Deployment)**
    - [x] Manual Verification (User checks UI).
    - [x] `run.bat` or `start.sh` for one-click launch.
    - [x] Final Documentation in `gemini.md`.

## Goals
- Create a local LLM TestCase generator with Ollama.
