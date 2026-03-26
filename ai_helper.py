import sys
import os
import json
import urllib.request
import urllib.error

def main():
    if len(sys.argv) != 3:
        print("Error: Required arguments <prompt_file> <content_file>")
        sys.exit(1)

    prompt_file = sys.argv[1]
    content_file = sys.argv[2]

    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read().strip()
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
    except Exception as e:
        print(f"Error reading input files: {e}")
        sys.exit(1)

    # Using Groq API instead of OpenAI
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        # Fallback to provided key if environment variable is not set
        api_key = "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"

    # Clean up the command prefix if it exists
    if prompt.lower().startswith("@ai"):
        prompt = prompt[3:].strip()

    # System prompt explaining the role
    system_prompt = (
        "You are an intelligent AI assistant embedded directly within a collaborative rich text editor. "
        "Your role is to help the user by analyzing, summarizing, formatting, or improving the document they are currently working on. "
        "The current full text of their document is provided below, formatted as a JSON Delta or raw text. "
        "Use this context to answer their query accurately and concisely. Do not use Markdown formatting in your response unless specifically asked, as the chat panel is plain text. "
        "Be extremely helpful, polite, and direct.\n\n"
        f"--- CURRENT DOCUMENT CONTENT ---\n{content}\n--- END DOCUMENT CONTENT ---"
    )

    req_body = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 512
    }

    req_data = json.dumps(req_body).encode('utf-8')
    req = urllib.request.Request("https://api.groq.com/openai/v1/chat/completions", data=req_data)
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read()
            res_json = json.loads(res_body)
            answer = res_json.get("choices", [{}])[0].get("message", {}).get("content", "No response generated.")
            print(answer)
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode('utf-8')
        print(f"API Error Occurred: {e.code} - {error_msg}")
    except Exception as e:
        print(f"Internal Error Occurred: {e}")

if __name__ == "__main__":
    main()
