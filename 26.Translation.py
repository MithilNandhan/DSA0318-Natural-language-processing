from transformers import MarianMTModel, MarianTokenizer
def translate(text, model, tokenizer):
    tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**tokens)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text
if __name__ == "__main__":
    model_name = 'Helsinki-NLP/opus-mt-en-fr'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    english_text = "Hello, how are you?"
    french_translation = translate(english_text, model, tokenizer)
    print(f"English: {english_text}")
    print(f"French: {french_translation}")
