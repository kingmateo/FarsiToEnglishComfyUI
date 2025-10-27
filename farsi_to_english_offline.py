import torch
from transformers import MarianMTModel, MarianTokenizer

class Farsi_To_En_offline:
    def __init__(self):
        self.loaded = False
        self.model = None
        self.tokenizer = None
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_fa": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("english_text",)
    FUNCTION = "translate_text"
    CATEGORY = "text"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def translate_text(self, text_fa):
        if not text_fa.strip():
            return ("",)
            
        try:
            # لود مدل فقط در اولین استفاده
            if not self.loaded:
                print("🔄 Loading Farsi-English translation model...")
                model_name = "Helsinki-NLP/opus-mt-fa-en"
                self.tokenizer = MarianTokenizer.from_pretrained(model_name)
                self.model = MarianMTModel.from_pretrained(model_name)
                self.loaded = True
                print("✅ Translation model loaded successfully!")
            
            # ترجمه متن
            inputs = self.tokenizer(text_fa, return_tensors="pt", padding=True, truncation=True)
            translated = self.model.generate(**inputs)
            result = self.tokenizer.decode(translated[0], skip_special_tokens=True)
            
            return (result,)
            
        except Exception as e:
            return (f"Translation error: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "Farsi_To_En_offline": Farsi_To_En_offline
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Farsi_To_En_offline": "🇮🇷 Farsi to English (Offline) - By AHYVFX"
}