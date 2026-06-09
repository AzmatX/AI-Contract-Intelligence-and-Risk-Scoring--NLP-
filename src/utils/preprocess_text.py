from datasets import load_dataset
import re

def clean_text(text):
    text = text.lower()                     # lowercase
    text = re.sub(r'\s+', ' ', text)        # remove extra spaces/newlines
    text = text.strip()
    return text

dataset = load_dataset(
    "theatticusproject/cuad",
    streaming=True
)

sample = next(iter(dataset["train"]))

pdf = sample["pdf"]

text = ""

for page in pdf.pages[:3]:
    page_text = page.extract_text()
    if page_text:
        text += page_text

cleaned_text = clean_text(text)

print(cleaned_text[:2000])