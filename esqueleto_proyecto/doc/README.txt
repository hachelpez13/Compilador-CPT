Compilador cpt.jar (V1.0)
------------------------------
Análisis léxico y sintáctico

Invocar como:

-------------------------------------------------------------
java -jar cpt.jar <fichero_fuente_cpt>
-------------------------------------------------------------

Alternativamente

-------------------------------------------------------------
java -jar cpt.jar <fichero_fuente_cpt.cpt>
-------------------------------------------------------------

Para las pruebas hemos utilizado el archivo test.py, asi como la carpeta proporcionada de test y una nuestra llamada mis_tests.

Se ejecuta de la forma:

   python3 test.py mis_tests

Primero es necesario ejecutar ant clean && ant para compilar el proyecto (o recompilarlo si ya estaba creado).

Práctica 3 hecha hasta el nivel 2, permite variables locales y parámetros en funciones y procediminetos.


Copia analisis sintactico basico para probar el analisis léxico exclusivamente.

//------------ Símbolo inicial de la gramática. Para análisis léxico no hace falta más
void Programa() : 
{

}
{
   ( 
	   < tBOOL > | < tCHAR >
   )+
   < EOF >
}

