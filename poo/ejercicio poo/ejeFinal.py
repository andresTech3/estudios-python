#$ utilizando la api de chatgpt
import openai

openai.api_key = "sk-proj-mAyIP7XBRqttbgT4UGiHT3BlbkFJsFJoNesTo2kcG3hcQjy4"
system_rol = "Hace de cuenta que eres un analizador de sentimientos, yo te paso el sentimineto y tu vas analizar el sentimiento de los mensajes, y me das una respuesta con almenos 1 caracter y maximo 4 caracteres solo respuesta numericas. donde -1 es negatividad maxima , 0 es neutral y 1 es positividad maxima (puedes responder solo con ints y floats)"

mensajes = [{"rol": "system", "content": system_rol}]


class AnalizadorDeSentimientos:
    def analizador_sentimientos(self, polarity):
        if polarity >= -1 and polarity <= -0.3:
            return "\x1b[1;31m " + "Negativo" #$ para poder darle un color al texto
        elif polarity >= -0.3 and polarity < -0.1:
            return "\x1b[1;31m "+ "Algo Negativo"
        elif polarity >= -0.1 and polarity <= 0.1:  
            return "\x1b[1;33m " + "Neutral"
        elif polarity > 0.1 and polarity <= 0.4:
            return "\x1b[1;32m " + " Algo Positivo"
        elif polarity > 0.4 and polarity <= 1:
            return "\x1b[1;32m " + " Positivo"
        else :
            return "\x1b[1;33m No se puede determinar el sentimiento" + "\x1b[0;37m"
        
analizador = AnalizadorDeSentimientos()

while True:
    use_prompt = input("\x1b[1;33m" + "\nDecime Algo:  " + "\x1b[0;37m")
    mensajes.append({"role" : "user", "content": use_prompt})
    completion = openai.completions.create(
        model= "gpt-3.5-turbo",
        prompt= mensajes,
        max_tokens= 8
    )

    respuesta = completion.choices[0].prompt["content"]
    mensajes.append({"rol" : "assistant", "content": respuesta})

    sentimiento = analizador.analizador_sentimientos(respuesta)
    print(sentimiento)
    








# #chat bot analizador de sentimientos
# from textblob import TextBlob

# class AnalizadorDeSentimientos:
#     def analizarSentimientos(self,texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0 :
#             return "positivo"
#         elif analisis.sentiment.polarity == 0 :
#             return "neutral"
#         else :
#             return "negativo"

# analizador = AnalizadorDeSentimientos()
# resultado = analizador.analizarSentimientos("I'm so bad today I don't know what's wrong with me")
# print(resultado)