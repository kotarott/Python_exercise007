from googletrans import Translator

class My_Translator():
    def __init__(self):
        self.to_lang = "ja"
        self.translator = Translator()
    
    def trans_to_jp(self, words):
        # translated = self.translator.translate(words, dest="ja")
        translated = Translator().translate(words, dest="ja")
        return translated.text

def test():
    translator = Translator()
    translated = translator.translate("Hello Everyone", dest="ja")
    print(translated.text)

if __name__ == "__main__":
    translator = My_Translator()
    words = input("翻訳したい文章を入力してください\n>>> ")
    result = translator.trans_to_jp(words)
    print(">>> ", result)
