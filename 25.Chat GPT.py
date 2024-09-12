from transformers import GPT2LMHeadModel, AutoTokenizer
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
prompt_text = "Once upon a time,"
input_ids = tokenizer.encode(prompt_text, return_tensors='pt')
output = model.generate(input_ids, max_length=20, num_return_sequences=1,pad_token_id=tokenizer.eos_token_id)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Text:\n", generated_text)
