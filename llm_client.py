# !ollama pull llama3.2
from openai import OpenAI
from config import OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_API_KEY
from config import OUTPUT_MARKDOWN

from pathlib import Path

LLM_BASE_URL = OLLAMA_BASE_URL
LLM_API_KEY = OLLAMA_API_KEY
LLM_MODEL = OLLAMA_MODEL

class LLMClient:
    def __init__(
        self,
        base_url: str = LLM_BASE_URL,
        api_key: str = LLM_API_KEY,
        model: str = LLM_MODEL
    ):
        self.model = model
        self.client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
    def load_markdown_file(self, file_path: str) -> str:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Markdown file not found: {file_path}")
        return path.read_text(encoding="utf-8")
    def healthcheck(self) -> str:
        """
        Minimal test to confirem the model endpoint is working.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role":"user","content":"Reply with exactly: OK"}
            ]
        )
        return response.choices[0].message.content.strip()

    def ask(self, prompt:str, system_prompt: str = "") -> str:
        """
        Standard text generation helper.
        """
        messages = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role":"user", "content":prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()

    def summarize_newsletters(self, file_path: str = OUTPUT_MARKDOWN) -> str:
        system_prompt = """
        You are a sharp tech and finance writer creating a comprehensive daily blog post from newsletter content.

        Your job is not to summarize each email one by one.
        Your job is to read all of the provided markdown context, synthesize the important ideas across it, and write one cohesive blog post.

        Rules:
        - Use only the information in the provided newsletters
        - Do not invent facts
        - Synthesize across all emails rather than treating them separately
        - Connect related stories, companies, and themes where appropriate
        - Add thoughtful analysis and light opinion, but keep it grounded in the provided content
        - Focus on what matters most, not every single item
        - Write like a real human analyst or blogger: clear, insightful, and engaging
        - Avoid generic filler, repetition, and robotic phrasing
        """

        markdown_text = self.load_markdown_file(file_path)

        prompt = f"""
        Below is newsletter content collected over the last day in markdown format.

        Your task is to read ALL of it carefully, piece together the major developments, and write one comprehensive blog post that feels unified and intentional.

        Markdown context:
        {markdown_text}

        Instructions:
        - Look across the full context before writing
        - Identify the most important headlines across all newsletters
        - Connect overlapping themes across AI, finance, infrastructure, developer tools, markets, and business strategy
        - Highlight the companies that appear most important or signal larger shifts
        - Include thoughtful interpretation of why these developments matter
        - Where appropriate, explain how separate stories fit into a broader trend
        - Prioritize synthesis over simple recap

        Output format:

        1. A strong blog title
        2. A compelling introduction that frames the day’s biggest developments
        3. 3 to 5 body sections with clear subheadings
        4. A section on companies or organizations worth watching
        5. A forward-looking conclusion on what these stories may mean going forward

        Writing style:
        - Write in full paragraphs, not just bullets
        - It should feel like a polished blog article someone would actually read
        - Be detailed enough to be useful, but not bloated
        - Include some opinion and analysis, but make sure it is clearly tied to the newsletter content
        """

        return self.ask(prompt=prompt, system_prompt=system_prompt)

if __name__ == "__main__":
    llm = LLMClient()
    try:
        print("Healthcheck: ", llm.healthcheck())
        print()

        blog = llm.summarize_newsletters()

        print(blog)
    except Exception as e:
        print("LMM client failed")
        print(e)