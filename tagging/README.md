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

|tag	 |freq	|%     |top|
|---|---|---|---|
|sp000	 |79884	|15.45 |(de, en, a, del, con)|
|nc0s000 |63452	|12.27 |(presidente, equipo, partido, país, año)|
|da0000	 |54549	|10.55 |(la, el, los, las, El)|
|aq0000	 |33906	|6.56  |(pasado, gran, mayor, nuevo, próximo)|
|fc	 |30147	|5.83  |(,)|
|np00000 |29111	|5.63  |(Gobierno, España, PP, Barcelona, Madrid)||
|nc0p000 |27736	|5.36  |(años, millones, personas, países, días)
|fp	 |17512	|3.39  |(.)|
|rg	 |15336	|2.97  |(más, hoy, también, ayer, ya)|
|cc	 |15023	|2.90  |(y, pero, o, Pero, e)|

sp000	Preposition	en, de, entre<br>
nc0s000	Common noun (singular)	lista, hotel, partido<br>
da0000	Article (definite)	el, la, los, las<br>
aq0000	Adjective (descriptive)	populares, elegido, emocionada, andaluz<br>
fc      Comma	,<br>
np00000	Proper noun	Málaga, Parlamento, UFINSA<br>
nc0p000	Common noun (plural)	años, elecciones<br>
fp	Period / full-stop	.<br>
rg	Adverb (general)	siempre, más, personalmente<br>
cc	Conjunction (coordinating)	y, o, pero<br>

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

Se entrenó el modelo con el script *train.py* y se evaluó con *eval.py* y se obtuvieron los siguientes resultados:

100.0% (87.58% / 95.26% / 18.01%)<br>
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

Se calcularon los tiempos de entrenamiento y evaluación y el accuracy para el modelo MEMM, para los 3 clasificadores pedidos, para n = 1,2,3,4. A continuación se detallan los resultados:

Tiempos de entrenamiento:

|n \ model	|maxent	|svm|mnb	|
|---	|---	|---	|---	|
|1	|10:03 min	|4:56 min	|46 seg	|
|2|12:48 min	|5:52 min	|53 seg	|
|3	|16:27 min	|7:16 min	|57 seg	|
|4	|19:58 min	|9:06 min	|1:04 min	|


Tiempos y resultados de evaluación:

|n\clf	|maxent	|svm|mnb	|
|---	|---	|---	|---	|
|1	|27 seg <br><br>100.0% (91.69% / 0.00% / 91.69%)<br>Accuracy: 91.69% / 0.00% / 91.69%	|28 seg <br><br>100.0% (94.11% / 0.00% / 94.11%)<br>Accuracy: 94.11% / 0.00% / 94.11%|1:05 horas <br><br>100.0% (74.85% / 0.00% / 74.85%)<br>Accuracy: 74.85% / 0.00% / 74.85%|
|2|30 seg <br><br>100.0% (90.20% / 0.00% / 90.20%)<br>Accuracy: 90.20% / 0.00% / 90.20%	|27 seg	<br><br>100.0% (92.43% / 0.00% / 92.43%)<br>Accuracy: 92.43% / 0.00% / 92.43%|1:06 horas <br><br>100.0% (76.73% / 0.00% / 76.73%)<br>Accuracy: 76.73% / 0.00% / 76.73%|
|3	|30 seg <br><br>100.0% (89.58% / 0.00% / 89.58%)<br>Accuracy: 89.58% / 0.00% / 89.58%	|28 seg <br><br>100.0% (92.27% / 0.00% / 92.27%)<br>Accuracy: 92.27% / 0.00% / 92.27%|1:06 horas <br><br>100.0% (78.79% / 0.00% / 78.79%)<br>Accuracy: 78.79% / 0.00% / 78.79%|
|4	|33 seg <br><br>100.0% (89.48% / 0.00% / 89.48%)<br>Accuracy: 89.48% / 0.00% / 89.48%	|29 seg <br><br>100.0% (92.13% / 0.00% / 92.13%)<br>Accuracy: 92.13% / 0.00% / 92.13%	|1:07 horas<br><br>100.0% (80.50% / 0.00% / 80.50%)<br>Accuracy: 80.50% / 0.00% / 80.50%|
