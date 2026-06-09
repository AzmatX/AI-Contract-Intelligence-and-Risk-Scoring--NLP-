from datasets import load_dataset
import json
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

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

contract_data = {
    "contract_id": 1,
    "text": clean_text(text)
}

with open("data/contract_1.json", "w", encoding="utf-8") as f:
    json.dump(contract_data, f, indent=4)

print("JSON file created successfully!")