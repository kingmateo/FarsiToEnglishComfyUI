import requests

class Farsi_To_En_DeepSeek:
    def __init__(self):
        self.DEEPSEEK_API_KEY = "کلید شما"
    
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
            
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        
        prompt = f"""Translate the following Persian text to English. 
Return only the English translation without any additional text, explanations, or notes:

{text_fa}"""

        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            translated_text = result["choices"][0]["message"]["content"].strip()
            
            return (translated_text,)
            
        except requests.exceptions.RequestException as e:
            return (f"Request error: {str(e)}",)
        except KeyError as e:
            return (f"Unexpected API response format: {str(e)}",)
        except Exception as e:
            return (f"Unexpected error: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "Farsi_To_En_DeepSeek": Farsi_To_En_DeepSeek
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Farsi_To_En_DeepSeek": "🇮🇷 Farsi to English (DeepSeek API) - By AHYVFX"
}