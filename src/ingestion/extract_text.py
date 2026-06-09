from datasets import load_dataset

print("Loading dataset...")

dataset = load_dataset(
    "theatticusproject/cuad",
    streaming=True
)

sample = next(iter(dataset["train"]))

pdf = sample["pdf"]

print("PDF loaded successfully!")

text = ""

for page in pdf.pages[:3]:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

print("\nExtracted Text:\n")
print(text[:3000])