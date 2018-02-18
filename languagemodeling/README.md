Procesamiento de Lenguaje Natural - UBA 2018
============================================

Ejercicio 1: Corpus
-------------------
Como corpus se usaron los primeros tres libros de la saga A Song of Ice and Fire de George R. R. Martin en español. En total ocupa 6,4 MB.
Para cargar el corpus se uso el corpus reader de NLTK *PlaintextCorpusReader*.

Ejercicio 2: Modelo de n-gramas
-------------------------------
En este ejercicio se pide implementar un modelo de ngramas modificando la clase NGram en *ngram.py*.
Esta clase se crea recibiendo el n y una lista de oraciones. Luego se construye un diccionario *count*, donde se guarda la cantidad de apariciones de cada ngrama y n-1grama. Para esto, a cada oración se le agrega n-1 marcadores \<s\> al comienzo de la oración y uno \</s\> al final. Después se iteran los ngramas y n-1gramas de cada oración sumando las apariciones.

La clase cuenta con los siguientes métodos:

- *count*
Dado un ngrama o un n-1grama, devuelve la cantidad de veces que aparece. Esto se hace usando el diccionario *count* que fue creado al inicializar la clase.

- *cond_prob*
Calcula la probabilidad condicional de un token dados los n-1 tokens anteriores. Para esto se divide la cantidad de veces que aparece el token después de los *prev_tokens* por la cantidad de veces que aparecen los *prev_tokens*. Los valores necesarios se obtienen del diccionario *count*.

- *sent_prob*
Calcula la probabilidad de una oración. Para esto se multiplican las probabilidades de todos los ngramas de la oración, usando el método *cond_prob*.

- *sent_prob_log*
Calcula la probabilidad logarítmica de una oración. Dado que el método anterior puede tener problemas de underflow por multiplicar probabilidades muy chicas, implementamos el cálculo de la probabilidad logarítimca. Para esto se suman los logaritmos en base 2 de las probabilidades de todos los ngramas de la oración, usando el método *cond_prob*.

Ejercicio 3: Generación de Texto
--------------------------------
En este ejercicio se pide implementar un generarador de oraciones de lenguaje natural implementando la clase NGramGeneratoren ngram_generator.py.
Al incializar la clase, se crea un diccionario *sorted_probs* donde para cada n-1grama se guardan los posibles tokens siguientes junto con sus probabilidades ordenados de mayor a menor.

- *generate_token*
Dada una lista de tokens, genera el siguiente token de manera aleatoria. Para esto, se busca la lista de posibles tokens siguientes del ngrama formado por los *prev_tokens* en el diccionario *sorted_probs*. Luego se elige alguno de forma random teniendo en cuenta las probabilidades de cada uno. 

- *generate_sent*
Genera una oración de manera aleatoria. Se comienza generando n-1 \<s\> como tokens previos y se llama a la función *generate_token* para conseguir el siguiente. Esto se repite llamando a *generate_token* con los tokens previos correspondientes hasta que el token conseguido sea \</s\>. Todos los tokens obtenidos forman la nueva oración.

Se generaron las siguientes oraciones:

| n | oraciones |
|---|---|
| 1 | La del volver al brazo al allí tan vez. <br><br> Magnar espada sintió hacer Walder demás. <br><br> Pelaje es tras sopló días casa hay no la iras su lugar las en el que. <br><br>
De el hombre estaban lanzas a vamos tenido en por visto envejecido el rechazada en.
| 2 | El rostro que dice Hullen no le trenzó el vestido. <br><br> No debimos apartarnos del corazón mismo la Casa Lannister asesinaron los estuviera presente cuando Ned con ellos. <br><br> Madre y empezó a lo vimos fueron arrollados por la mirada. <br><br> De verdad antes de roble caído.|
| 3 | En la cima , hasta que la princesa Elia tendría que ser Ilyn , traedme su cabeza fue un sonido grave y sonoro , y de esas historias que la oportunidad de matarme , pero sólo porque pone veneno en la Balerion. <br><br> 
Me has traído algún regalo por mi cara lo de Jon Nieve , tenían edad suficiente para el viaje ya se habían quedado con el frío que antes dormía empezaba a sentirse como una sombra blanca en los ojos. <br><br> Se había reunido en torno al otro lado del patio de armas ? <br><br> En aquella isla pedregosa en medio de las almenas , y aquí el chico gordo igual que no fuera hijo de mi autocontrol — advirtió Dany —.|
| 4 |  Decidió que se mataría antes de seguir así. <br><br> Una fila de carromatos tirados por bueyes entraba en aquel momento las hojas caídas hacían más difícil seguir las huellas , pero era un precio muy alto — replicó Ned —. <br><br> Los cascos de sus corceles al cruzar el puente cuando lord Renly salió del Torreón de Craster en medio de la lluvia a un rostro humano , el enano , hincando una rodilla en el suelo. <br><br> 
Las mujeres recogían frutas en los jardines de la ribera antes de encontrar por fin un sitio donde haga calor .|

Ejercicio 4: Suavizado add-one
------------------------------
En este ejericio se pide implementar el suavizado add-one modificando la clase AddOneNGram en *ngram.py*.
Al inicializar la clase se calcula el diccionario *count* como en NGram y además se calcula el tamaño del vocabulario que se guarda en la variable *V*.

Se implementaron los siguientes métodos:

- *V*
Devuelve el tamaño del vocabulario.

- *cond_prob*
Calcula la probabilidad condicional de un token dados los n-1 tokens anteriores usando el suavizado add-one. Para esto se divide la cantidad de veces que aparece el token después de los *prev_tokens* + 1, por la cantidad de veces que aparecen los *prev_tokens* + V. Los valores necesarios se obtienen del diccionario *count* y de la variable *V*.

Ejercicio 5: Evaluación de Modelos de Lenguaje
----------------------------------------------
Para este ejercicio se dividieron las oraciones del corpus en 2, 90% para entrenamiento y 10% para test. Se uso el script *train.py* para entrenar el modelo de suavizado add-one con el conjunto de oraciones de entrenamiento. Luego, se uso el script *eval.py* para calcular la log probability, la cross entropy y la perplexity usando las oraciones de test. Esto se hizo para n = 1,2,3 y 4.

| n | Log probability | Cross entropy| Perplexity |
|---|---|---|---|
| 1 | -1277333.3393448822 | 9.510053600852347 | 729.1407896141487 |
| 2 | -1364592.7015803868 | 10.159720517447077 | 1143.880412497499 |
| 3 | -1686417.8203116502 | 12.555785847429531 | 6020.993511748579 |
| 4 | -1773033.340590898 | 13.200659205971812 | 9414.4376500024 |


Ejercicio 6: Suavizado por Interpolación
----------------------------------------
En este ejercicio se pide implementar el suavizado por interpolación en la clase InterpolatedNGramen en *ngram.py*.
Para poder hacer la interpolación se computan todos los kgramas con k<=n. Los lambdas de la interpolación se calculan en base a un único parámetro gamma, que puede ser dado o calculado en el momento. Si no se pasa ningún gamma, se separan un 10% de las oraciones para held out. Luego se prueban distintos gamma y se usa el que da la menor perplexity para el conjunto de held out.

Se implementó el siguiente método:

- *cond_prob*
Devuelve la probabilidad condicional de un token usando suavizado por interpolación. Para esto se hacen n iteraciones, en cada una se calcula el lambda usando el gamma y se lo multiplica por la probabilidad condicional usando el método en la clase NGram. En la última iteración la probabilidad condicional se calcula usando la de add-one, a menos que la clase se inicialice indicando lo contrario, donde se usa la de NGram.

Finalmente se intentaron buscar a mano los gammas que minimizan la perplexity para n = 1,2,3 y 4. Los gammas se probaron con hasta 1 decimal.

| n | gamma | Perplexity |
|---|---|---|
| 1 | todos los gammas dan la misma perplexity | 762.5292125370454 |
| 2 | 107.2 | 192.83350392552626 |
| 3 | 138.6 | 170.1299139687285 |
| 4 | 162.3 | 169.2744951965361 |