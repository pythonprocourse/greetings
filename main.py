from greets import greetings
from translate import Translator

translator = Translator(to_lang='pt')

for g in greetings:
    print(translator.translate(g).title())