import eel
import desktop
import googletrans_api

app_name = "web"
end_point = "index.html"
size = (600,700)

@ eel.expose
def translate(words, from_lang, to_lang):
    translator = googletrans_api.My_Translator()
    translator.set_lang(from_lang, to_lang)
    translated = translator.trans_any(words)
    return translated

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)