# codex_lite.py

from transformers import pipeline

class CodexLite:
    def __init__(self):
        print("[🔮] Codex-Lite: Summoning local model...")
        self.generator = pipeline(
            "text-generation",
            model="Salesforce/codegen-350M-mono",  # Small 350M code model
            device=-1  # CPU only
        )
        print("[✅] Codex-Lite: Ready.")

    def ask(self, prompt: str, max_tokens: int = 128) -> str:
        print(f"[⚡] Codex-Lite: Generating code for prompt: {prompt}")
        output = self.generator(prompt, max_length=max_tokens, do_sample=True)
        return output[0]['generated_text']

# Example direct usage:
if __name__ == "__main__":
    codex = CodexLite()
    result = codex.ask("def greet():")
    print(result)
