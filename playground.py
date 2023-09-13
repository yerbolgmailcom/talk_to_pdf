from pathlib import Path
import os
from load_dotenv import load_dotenv
from PyPDF2 import PdfReader


load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

reader = PdfReader("2023_GPT4All_Technical_Report.pdf")
sample_text = reader.pages[1].extract_text()[:1000]

Path("sample.txt").write_text(sample_text)
print(sample_text)

whole_text = "Page " + "\n\nPage ".join([f"{i}\n{page.extract_text()}" for i, page in enumerate(reader.pages, 1)])
Path("whole.txt").write_text(whole_text)
