############################
#Borrar pantalla


# GRUPO 18
import os
import string



def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
############################
#####################################################################################################
# Funciones punto 1




def calcular_indices(recuperados, relevantes_consulta,cant_reg_relevantes):
    recall = relevantes_consulta / cant_reg_relevantes # Total de documentos relevantes en la base de datos
    recall="{:.2f}%".format(recall)
    precision = relevantes_consulta / recuperados
    precision="{:.2f}%".format(precision)
    return recall, precision


# FIN Funciones punto 1
#####################################################################################################

#####################################################################################################
# Funciones punto 2
#####################################################################################################

"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compare_texts(text1, text2):
    # Vectorización de los textos utilizando TF-IDF sin eliminar stopwords
    vectorizer = TfidfVectorizer(stop_words=None)
    tfidf = vectorizer.fit_transform([text1, text2])

    # Cálculo de la similitud coseno entre los vectores TF-IDF de los textos
    sim_cos = cosine_similarity(tfidf[0], tfidf[1])

    return sim_cos[0][0]


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compare_lists(list1, list2):
    # Convertir las listas en cadenas de texto
    text1 = " ".join(list1)
    text2 = " ".join(list2)

    # Vectorización de los textos utilizando TF-IDF sin eliminar stopwords
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])

    # Cálculo de la similitud coseno entre los vectores TF-IDF de los textos
    sim_cos = cosine_similarity(tfidf[0], tfidf[1])

    return sim_cos[0][0]

"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

def compara_texto_original(text1, text2):
    # Obtener las stopwords para español y convertirlas a lista
    stop_words = list(set(stopwords.words('spanish')))
    
    # Vectorización de los textos utilizando TF-IDF sin eliminar stopwords
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf = vectorizer.fit_transform([text1, text2])

    # Cálculo de la similitud coseno entre los vectores TF-IDF de los textos
    sim_cos = cosine_similarity(tfidf[0], tfidf[1])

    return sim_cos[0][0]






################################################################
import fitz
def leer_pdf(nombre_archivo):
    texto_completo = ""
    
    with fitz.open(nombre_archivo) as doc:
        for pagina in doc:
            texto_completo += pagina.get_text()
    
    return texto_completo

################################################################

def leer_txt(nombre_archivo):
    texto_completo = ""

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto_completo = archivo.read()

    return texto_completo

################################################################
import string

def eliminar_puntuaciones(tokens):
    # Obtener los signos de puntuación
    signos_puntuacion = set(string.punctuation)
    # Crear una nueva lista sin signos de puntuación
    tokens_sin_puntuacion = [token for token in tokens if token not in signos_puntuacion]
    return tokens_sin_puntuacion

####################################################################

from nltk.corpus import stopwords


def eliminar_stopwords(lista_palabras):
    # Obtenemos las stopwords para español
    stop_words = set(stopwords.words('spanish'))
    
    # Eliminamos las stopwords de la lista de palabras
    lista_sin_stopwords = [palabra for palabra in lista_palabras if not palabra.lower() in stop_words]
    
    return lista_sin_stopwords
#####################################################################



# FIN Funciones punto 2
#####################################################################################################



#####################################################################################################

while True:
    clear_screen()
    print("Trabajo Practico N°5 Clasificación Automática de Textos"+"\n\n")
    print("1. Calculo de la medición de índices de recuperación y precisión en diferentes búsquedas")
    print("2. Comparación de representaciones TF-IDF en la búsqueda de documentos similares en distintos casos de procesamiento")
    print("3. Salir\n")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        clear_screen()
        """Supongamos que partimos de una base de datos con 100 registros, 
        de los cuales 40 son relevantes para nuestra consulta y los otros 60 no lo son. 
        A partir de diferentes resultados de nuestras búsquedas, medir los índices de recuperación y de precisión:"""


        cant_reg_base_dato=int(input("Ingrese la cantidad de registros de la base de datos: "))
        cant_reg_relevantes=int(input("Ingrese cantidad de ducumentos relevantes para la consulta: "))
        cant_no_relevantes=cant_reg_base_dato-cant_reg_relevantes
        print("Cantidad de documentos no relevantes para la consulta:",cant_no_relevantes)

    
        recuperados = int(input("Ingrese el número de documentos recuperados: "))
        relevantes_consulta = int(input("Ingrese el número de documentos relevantes para la consulta: "))

        recall, precision = calcular_indices(recuperados, relevantes_consulta,cant_reg_relevantes)

        print("Índice de Recuperación: ", recall)
        print("Índice de Precisión: ", precision)

        input("Presione enter para continuar...")

           
    
    elif opcion == "2":


        #Consigue la ruta donde se encuentran almacenados los documentos PDFs y TXTs

        ruta_directorio = r"..\TPN5" # Reemplaza con la ruta de tu directorio de documentos
        lista_archivos = os.listdir(ruta_directorio)

        lista_archivos_pdf = [archivo for archivo in lista_archivos if archivo.endswith('.pdf')]
        lista_archivos_txt = [archivo for archivo in lista_archivos if archivo.endswith('.txt')]
        

        documentos_pdf = []
        for archivo in lista_archivos_pdf:
            # Leer el archivo PDF de la lista de PDFs
            texto_documentos = leer_pdf(archivo)
            documentos_pdf.append(texto_documentos)


        documentos_txt = []
                
        for archivo in lista_archivos_txt:
            # Leer el archivo PDF de la lista de TXTs
            texto_documentos = leer_txt(archivo)
            documentos_txt.append(texto_documentos)  
        

             
        ##########################################################################################


        while True:
            clear_screen()
            print("¡Has ingresado la opcion 2 del menú!"+"\n\n")
            print("¡Selecciona un opcion para lo cual trabajar!"+"\n\n")
            print("1. Con el texto original")
            print("2. Eliminando stop-words")
            print("3. Realizando stemming")
            print("4. Con bi-gramas")
            print("5. Volver al menú principal\n")

            subopcion = input("Ingrese una opción: ")
            if subopcion == "1":
                clear_screen()



                """
                docupdflist=[]

                for docupdf in documentos_pdf:
                    cadena = docupdf
                    lista = cadena.split()
                    docupdflist.append(lista)
                """
                

                print("Texto original de los documentos PDFs\n")

                
                """
                max_similitud = 0.0
                doc1_max = ""
                doc2_max = ""

                for i in range(len(documentos_pdf)):
                    for j in range(i+1, len(documentos_pdf)):
                        similitud = compara_texto_original(documentos_pdf[i], documentos_pdf[j])
                        if similitud > max_similitud:
                            max_similitud = similitud
                            doc1_max = "Texto {}".format(i+1)
                            doc2_max = "Texto {}".format(j+1)
                        print("Similitud coseno: {:.2f} entre la texto {} con en el texto {} asi tambien entre la texto {} con el texto {}".format(similitud, i+1, j+1, j+1, i+1))

                print("\nLa máxima similitud de {:.2f} se encuentra entre {} y {} o entre el {} y el {}\n".format(max_similitud, doc1_max, doc2_max,doc2_max,doc1_max))
                """
                while True:
                    try:
                        numero = int(input("\nIngresa un numero del documento de prueba del 1 al 5: "))
                        if 1 <= numero <= 5:
                            break
                        else:
                            print("El número debe estar en el rango del 1 al 5.")
                    except ValueError:
                        print("Error: Debes ingresar un número entero.")
                

                # Obtener un índice dentro del rango de la lista
                indice_docu = numero-1

                # Obtener el elemento correspondiente al índice aleatorio
                elemento = lista_archivos_pdf[indice_docu]
    
                # Imprimir el índice y el elemento elegido
                print("\nDocumento para elegido para la prueba es el : {}\n".format(elemento))


                copialistapdfs=list(lista_archivos_pdf)
                # Eliminar el elemento en el índice de la lista necesario para evitar valores repetidos
                del copialistapdfs[indice_docu]

                #Copia de la lista de documentos original para trabajar
                aux_documentos_pdf=list(documentos_pdf)
                del aux_documentos_pdf[indice_docu]

                #Se establece los elementos del documento de prueba
                docprueba=documentos_pdf[indice_docu]

                #Se comienza hacer la comparacion

                max_similitud = 0.0
                doc1_max = ""

                for i in range(len(aux_documentos_pdf)):
                    similitud = compara_texto_original(docprueba, aux_documentos_pdf[i])
                    if similitud > max_similitud:
                        max_similitud = similitud
                        doc1_max = copialistapdfs[i]
                    print("Similitud coseno: {:.2f} entre el {} con en el  {}".format(similitud,elemento,copialistapdfs[i]))
                
                print("\nLa máxima similitud de {:.2f} se encuentra entre {} y {}\n".format(max_similitud,elemento,doc1_max))

                #Se restaura los valores originales para no alterar en una segunda iteracion
                copialistapdfs=list(lista_archivos_pdf)
                aux_documentos_pdf=list(documentos_pdf)



                input("Presione enter para continuar...")
            elif subopcion == "2":
                clear_screen()
                input("Presione enter para continuar...")
            elif subopcion == "3":
                clear_screen()
                input("Presione enter para continuar...")   
            elif subopcion == "4":
                clear_screen()
                input("Presione enter para continuar...") 
            elif subopcion == "5":
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
                input("Presione enter para continuar...")
    
    
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida, por favor intente de nuevo.")
        input("Presione enter para continuar...")
