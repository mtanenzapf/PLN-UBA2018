Procesamiento de Lenguaje Natural - UBA 2018
============================================


Ejercicio 1
-----------

Ejercicio 2
-----------
En este ejercicio se pide implementar un modelo de ngramas modificando la clase NGram en ngram.py.
Esta clase se crea recibiendo el n y una lista de oraciones. Luego se costruye un diccionario count, donde se guarda la cantidad de apariciones de cada ngrama y n-1grama. Para esto, a cada oración se le agrega n-1 marcadores <s> al comienzo de la oración y uno </s> al final. Despúes se iteran los ngramas y n-1gramas de cada oración sumando las apariciones.

La clase cuenta con los siguientes métodos:

- count
Dado un ngrama o un n-1grama, devuelve la cantidad de veces que aparece. Esto se hace usando el diccionario count que fue creado al inicializar la clase.

- cond_prob
Calcula la probabilidad condicional de un token dados los n-1 tokens anteriores. Para esto se divide la cantidad de veces que aparece el token despúes de los prev_tokens por la cantidad de veces que aparecen los prev_tokens. Los valores necesarios se obtienen del diccionario count.

- sent_prob
Calcula la probabilidad de una oración. Para esto se multiplican las probabilidades de todos los ngramas de la oración, usando el método cond_prob.

- sent_prob_log
Calcula la probabilidad logarítmica de una oración. Dado que el método anterior puede tener problemas de underflow por multiplicar probabilidades que pueden ser muy chicas, implementamos el cálculo de la probabilidad logarítimca. Para esto se suman los logaritmos en base 2 de las probabilidades de todos los ngramas de la oración, usando el método cond_prob.

Ejercicio 3
-----------

Ejercicio 4
-----------

Ejercicio 5
-----------

Ejercicio 6
-----------
