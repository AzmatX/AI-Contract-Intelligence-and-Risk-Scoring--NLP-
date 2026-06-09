from transformers import AutoTokenizer
import json

# Load JSON file
with open("data/contract_1.json", "r", encoding="utf-8") as f:
    contract = json.load(f)

text = contract["text"]

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("roberta-base")

tokens = tokenizer(
    text,
    truncation=True,
    padding="max_length",
    max_length=128
)

print("Input IDs:")
print(tokens["input_ids"][:20])

print("\nNumber of tokens:")
print(len(tokens["input_ids"]))