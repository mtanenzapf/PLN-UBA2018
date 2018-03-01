Procesamiento de Lenguaje Natural - UBA 2018
============================================

Ejercicio 1: Corpus AnCora: Estadísticas de etiquetas POS
---------------------------------------------------------
En este ejercicio se calculan estadísticas del corpus AnCora. Se obtuvieron los siguientes resultados:

**Basic Statistics**
- sents: 17378
- tokens: 517194
- words: 46501
- tags: 85 

**Most Frequent POS Tags**

|tag	 |freq	|%     |top| meaning|
|---|---|---|---|---|
|sp000	 |79884	|15.45 |(de, en, a, del, con)|Preposition: en, de, entre|
|nc0s000 |63452	|12.27 |(presidente, equipo, partido, país, año)| Common noun (singular): lista, hotel, partido|
|da0000	 |54549	|10.55 |(la, el, los, las, El)|Article (definite): el, la, los, las|
|aq0000	 |33906	|6.56  |(pasado, gran, mayor, nuevo, próximo)|Adjective (descriptive): populares, elegido, emocionada, andaluz|
|fc	 |30147	|5.83  |(,)|Comma|
|np00000 |29111	|5.63  |(Gobierno, España, PP, Barcelona, Madrid)|Proper noun: Málaga, Parlamento, UFINSA|
|nc0p000 |27736	|5.36  |(años, millones, personas, países, días)|Common noun (plural): años, elecciones|
|fp	 |17512	|3.39  |(.)|Period / full-stop|
|rg	 |15336	|2.97  |(más, hoy, también, ayer, ya)|Adverb (general): siempre, más, personalmente|
|cc	 |15023	|2.90  |(y, pero, o, Pero, e)|Conjunction (coordinating): y, o, pero|

**Word Ambiguity Levels**

|n	|words	|%	|top|
|---|---|---|---|
|1	|43972	|94.56	|(,, con, por, su, El)|
|2	|2318	|4.98	|(el, en, y, ", los)|
|3	|180	|0.39	|(de, la, ., un, no)|
|4	|23	|0.05	|(que, a, dos, este, fue)|
|5	|5	|0.01	|(mismo, cinco, medio, ocho, vista)|
|6	|3	|0.01	|(una, como, uno)|
|7	|0	|0.00	|()|
|8	|0	|0.00	|()|
|9	|0	|0.00	|()|


Ejercicio 2: Baseline Tagger
----------------------------
Se implementó un baseline tagger que dada una palabra, le asigna la etiqueta más frecuente. La clase recibe un conjunto de oraciones etiquetadas de entrenamiento, y para cada palabra guarda la etiqueta más frecuente. Esto se usa para después etiquetar nuevas palabras. Para las palabras desconocidas se devuelve la etiqueta 'nc0s000'.

Se entrenó el modelo con el script *train.py* y se evaluó con *eval.py* y se obtuvieron los siguientes resu|ltados:

100.0% (87.58% / 95.26% / 18.01%)
Accuracy: 87.58% / 95.26% / 18.01%

|g \ m	|sp000	|nc0s000|da0000	|aq0000	|fc	|nc0p000|rg	|np00000|fp	|cc	|
|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|
|sp000	|14.28	|0.05	|-	|-	|-	|-	|0.01	|-	|-	|-	|	
|nc0s000|0.00	12.20	|-	|0.27	|-	|0.00	|0.03	|0.00	|-	|0.00	|	
|da0000	|-	|0.15	|9.54	|-	|-	|-	|-	|-	|-	|-	|
|aq0000	|0.01	|2.04	|-	|4.84	|-	|0.14	|0.00	|-	|-	|-	|
|fc	|-	|-	|-	|-	|5.85	|-	|-	|-	|-	|-	|
|nc0p000|-	|1.24	|-	|0.18	|-	|4.10	|-	|-	|-	|-	|
|rg	|0.02	|0.31	|-	|0.04	|-	|-	|3.27	|-	|-	|0.02	|
|np00000|0.00	|2.04	|-	|0.00	|-	|0.00	|-	|1.52	|-	|0.00	|
|fp	|-	|-	|-	|-	|-	|-	|-	|-	|3.55	|-	|
|cc	|0.00	|0.01	|-	|-	|-	|-	|0.05	|0.00	|-	|3.34	|


Ejercicio 3: Features para Etiquetado de Secuencias
---------------------------------------------------

Ejercicio 4: Maximum Entropy Markov Models
------------------------------------------
