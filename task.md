# SPECTRA'26 Collaborative Rich Text Editor

## Planning
- [x] Read problem statement PDF
- [x] Design architecture (C backend + web frontend)

## Implementation - Backend (C)
- [x] Download mongoose.c/h and cJSON.c/h libraries
- [x] Implement HTTP API (auth, document CRUD, versions, chat)
- [x] Implement WebSocket collaboration (deltas, cursors, presence)
- [x] Implement conflict handling (document locking)
- [x] Implement version history (save/restore)
- [x] Implement AI chat responses
- [x] Implement code execution handler

## Implementation - Frontend
- [x] Build HTML with auth, sidebar, editor, panels, status bar
- [x] Build premium dark theme CSS with glassmorphism
- [x] Build client-side JS (auth, editor, collab, chat, versions, offline)

## Build & Verify
- [x] Create build script
- [x] Compile with GCC
- [x] Test in browser (browser subagent testing successful)
- [x] Create walkthrough

## AI API Extension
- [x] Create python helper script [ai_helper.py](file:///c:/Users/307520%20B7IIN/OneDrive/Desktop/prompton/ai_helper.py) to route context to Groq API
- [x] Create python script [generate_prompt_pdf.py](file:///c:/Users/307520%20B7IIN/OneDrive/Desktop/prompton/generate_prompt_pdf.py) for Prompt Documentation PDF
- [x] Connect C backend [main.c](file:///c:/Users/307520%20B7IIN/OneDrive/Desktop/prompton/src/main.c) to [ai_helper.py](file:///c:/Users/307520%20B7IIN/OneDrive/Desktop/prompton/ai_helper.py) via `popen()`
- [x] Compile and test AI integration
- [x] Generate Prompt Engineering PDF

## Bug Fixes
- [x] Clean C compiler warnings (`time_t`, [strdup](file:///c:/Users/307520%20B7IIN/OneDrive/Desktop/prompton/lib/mongoose.h#761-762), etc.)
- [x] Clean CSS lint warnings (`backdrop-filter`)
