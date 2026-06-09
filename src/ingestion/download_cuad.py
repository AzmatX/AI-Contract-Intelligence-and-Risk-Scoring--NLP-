from datasets import load_dataset

dataset = load_dataset(
    "theatticusproject/cuad",
    streaming=True
)

train_data = dataset["train"]

sample = next(iter(train_data))

print(sample)