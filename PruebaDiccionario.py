meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CRINGE": "Algo raro o embarazoso",
            "ROFL" : "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }
for i in range(4):          
    word = input("Escribe una palabra que no entiendas(¡con mayusculas!)")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Ups, no lo sabemos")
