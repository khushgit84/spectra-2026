import sys
import os

try:
    from fpdf import FPDF
except ImportError:
    print("Error: The 'fpdf' module is missing.")
    print("Please run: pip install fpdf")
    sys.exit(1)

class SpectraPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, "SPECTRA'26 - Technical Documentation & AI Prompting", 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_full_doc(filename):
    pdf = SpectraPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- TITLE PAGE ---
    pdf.add_page()
    pdf.set_font("Arial", 'B', 28)
    pdf.ln(40)
    pdf.cell(0, 20, "SPECTRA'26", 0, 1, 'C')
    pdf.set_font("Arial", 'B', 18)
    pdf.cell(0, 10, "Technical Implementation & AI Prompt Engineering", 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, "Algorithm Overview | Backend Prompts | System Architecture", 0, 1, 'C')
    pdf.ln(20)

    # --- SECTION 1: CORE ALGORITHMS ---
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(108, 92, 231) # Purple
    pdf.cell(0, 10, "1. Core System Algorithms", 0, 1)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "1.1 WebSocket Event Synchronization", 0, 1)
    pdf.set_font("Arial", '', 11)
    sync_algo = (
        "The editor uses a centralized event relay model based on Mongoose for high-speed synchronization. "
        "When a user makes a change: \n"
        "1. Client generates a Quill Delta (JSON-based operational transform).\n"
        "2. Delta is wrapped in a WebSocket packet and sent to the C backend.\n"
        "3. Backend validates the user's document lock status (see 1.3).\n"
        "4. Valid changes are broadcast to all other active connections in the same document room.\n"
        "5. The server periodically triggers version snapshots for non-volatile persistence."
    )
    pdf.multi_cell(0, 7, sync_algo)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "1.2 Document Locking (Optimistic Concurrency)", 0, 1)
    pdf.set_font("Arial", '', 11)
    lock_algo = (
        "To prevent race conditions during heavy collaboration, a 'Strict Lock' mechanism is used: \n"
        "- Initial State: Document is 'Unlocked'.\n"
        "- Lock Acquisition: A user sends a 'lock' request. Server checks if 'locked_by == -1'.\n"
        "- Enforcement: If locked, the server rejects all 'delta' packets from users other than the lock holder.\n"
        "- Auto-Release: When a user disconnects or closes the session, the C cleanup handler (MG_EV_CLOSE) "
        "automatically resets 'locked_by = -1' to ensure the document doesn't remain orphaned."
    )
    pdf.multi_cell(0, 7, lock_algo)

    # --- SECTION 2: AI BACKEND PROMPTS ---
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(108, 92, 231)
    pdf.cell(0, 10, "2. AI Prompt Engineering for Backends", 0, 1)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)

    backends = [
        ("Google Gemini (Pro/Flash)", 
         "Context: 'You are a technical document architect. Analyze the provided file content and generate a concise summary.'\n"
         "Prompt: 'Generate a structured summary of the following document. Ignore formatting JSON garbage. Focusing on core concepts: [DOC_CONTENT]'"),
        
        ("Anthropic Claude 3 Opus",
         "Context: 'You are an elite coding assistant. Your output must be direct and technical.'\n"
         "Prompt: 'Looking at the SPECTRA'26 source code and this active document, suggest three critical grammatical or structural improvements. Document: [DOC_CONTENT]'"),
        
        ("Deepseek Coder V2",
         "Context: 'Expert software engineer specializing in C/WebSocket systems.'\n"
         "Prompt: 'Identify potential memory leaks or logic errors in the delta synchronization handler based on the document state: [DOC_CONTENT]'"),
        
        ("Kimi AI (Moonshot)",
         "Context: 'Multilingual document assistant.'\n"
         "Prompt: 'Translate or explain the technical jargon in this document to a layman's audience. Document: [DOC_CONTENT]'")
    ]

    for title, prompt in backends:
        pdf.set_font("Arial", 'B', 13)
        pdf.cell(0, 10, title, 0, 1)
        pdf.set_font("Courier", '', 10)
        pdf.set_fill_color(245, 245, 245)
        pdf.multi_cell(0, 6, prompt, fill=True, border=1)
        pdf.ln(5)

    # --- SECTION 3: SYSTEM PROMPT ---
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(108, 92, 231)
    pdf.cell(0, 10, "3. Global System Prompt Injection", 0, 1)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    
    system_p = (
        "System Instruction: \n"
        "'You are SPECTRA-AI, an agent embedded in a real-time collaborative platform. "
        "You have direct visibility into the editor's live state. \n"
        "User Query: {USER_QUERY}\n"
        "Document Context: {FULL_DOCUMENT_BUFFER}\n"
        "Command: Provide a high-density response. No preamble. No markdown outside code blocks. "
        "Limit to 256 tokens for real-time performance.'"
    )
    pdf.set_font("Courier", 'B', 10)
    pdf.multi_cell(0, 6, system_p, border=1)

    pdf.output(filename)
    print(f"Documentation generated: {filename}")

if __name__ == "__main__":
    generate_full_doc("SPECTRA26_Implementation_Plan.pdf")
