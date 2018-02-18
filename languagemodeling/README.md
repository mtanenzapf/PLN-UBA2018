Procesamiento de Lenguaje Natural - UBA 2018
============================================


Ejercicio 1
-----------
Como corpus se usaron los primeros tres libros de la saga A Song of Ice and Fire de George R. R. Martin en español. En total ocupa 6,4 MB.
Para cargar el corpus se uso el corpus reader de NLTK PlaintextCorpusReader.

Ejercicio 2
-----------
En este ejercicio se pide implementar un modelo de ngramas modificando la clase NGram en ngram.py.
Esta clase se crea recibiendo el n y una lista de oraciones. Luego se costruye un diccionario count, donde se guarda la cantidad de apariciones de cada ngrama y n-1grama. Para esto, a cada oración se le agrega n-1 marcadores <s> al comienzo de la oración y uno </s> al final. Despúes se iteran los ngramas y n-1gramas de cada oración sumando las apariciones.

La clase cuenta con los siguientes métodos:

- count
Dado un ngrama o un n-1grama, devuelve la cantidad de veces que aparece. Esto se hace usando el diccionario count que fue creado al inicializar la clase.

- cond_prob
Calcula la probabilidad condicional de un token dados los n-1 tokens anteriores. Para esto se divide la cantidad de veces que aparece el token después de los prev_tokens por la cantidad de veces que aparecen los prev_tokens. Los valores necesarios se obtienen del diccionario count.

- sent_prob
Calcula la probabilidad de una oración. Para esto se multiplican las probabilidades de todos los ngramas de la oración, usando el método cond_prob.

- sent_prob_log
Calcula la probabilidad logarítmica de una oración. Dado que el método anterior puede tener problemas de underflow por multiplicar probabilidades que pueden ser muy chicas, implementamos el cálculo de la probabilidad logarítimca. Para esto se suman los logaritmos en base 2 de las probabilidades de todos los ngramas de la oración, usando el método cond_prob.

Ejercicio 3
-----------
En este ejercicio se pide implementar un generar oraciones de lenguaje natural implementando la clase NGramGeneratoren ngram_generator.py.
Al incializar la clase, se crea un diccionario sorted_probs donde para cada n-1grama se guardan los posibles tokens siguientes junto con sus probabilidades ordenados de mayor a menor.

- generate_token
Dada una lista de tokens, genera el siguiente token de manera aleatoria. Para esto, se busca la lista de posibles tokens siguientes del ngrama formado por los prev_tokens en el diccionario sorted_probs. Luego se elige alguno de forma random teniendo en cuenta las probabilidades de cada uno. 

- generate_sent
Genera una oración de manera aleatoria. Se comienza generando n-1 <s> como tokens previos y se llama a la función generate_token para conseguir el siguiente. Esto se repite llamande a generate_token con los tokens previos correspondientes hasta que el token conseguido sea </s>. Todos los tokens obtenidos forman la nueva oración.

Ejercicio 4
-----------
En este ejericio se pide implementar el suavizado add-one modificando la clase AddOneNGram en ngram.py.
Al inicializar la clase se calcula el diccionario count como en NGram y además se calcula el tamaño del vocabulario que se guarda en la variable V.

Se implementaron los siguientes métodos:

- V
Devuelve el tamaño del vocabulario.

- cond_prob
Calcula la probabilidad condicional de un token dados los n-1 tokens anteriores usando el suavizado add-one. Para esto se divide la cantidad de veces que aparece el token después de los prev_tokens + 1 por la cantidad de veces que aparecen los prev_tokens + V. Los valores necesarios se obtienen del diccionario count y de la variable V.

Ejercicio 5
-----------

Ejercicio 6
-----------
