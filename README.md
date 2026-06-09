# Compilador CPT a P-Máquina 🚀

Este repositorio contiene un compilador completo para el lenguaje de programación **CPT**, desarrollado para la asignatura de Procesadores de Lenguajes (Universidad de Zaragoza). El compilador traduce código fuente CPT a código objeto (ensamblador) diseñado para ser ejecutado en una máquina de pila abstracta (**P-Máquina**).

Actualmente, el proyecto ha alcanzado un **Nivel 2 de implementación**, soportando características avanzadas de lenguajes estructurados.

## ✨ Características del Lenguaje soportadas

* **Tipos de datos:** Escalares (`int`, `char`, `bool`) y estructuras de datos estáticas (`array` unidimensionales).
* **Gestión de Memoria y Ámbitos:** * Soporte completo para variables globales y locales.
    * Anidamiento de subprogramas (funciones dentro de funciones).
    * Gestión dinámica del entorno de ejecución mediante **Static Link (Display)** para la resolución de variables en ámbitos superiores (*shadowing* y encadenamiento estático).
* **Subprogramas:**
    * Procedimientos (`proc`) y Funciones (`func`) con retorno de tipos.
    * Paso de parámetros por **Valor** (`in`) y por **Referencia** (`out`, `inout`).
    * Soporte para recursividad (ej. cálculo de la serie de Fibonacci).
* **Control de Flujo:**
    * Estructuras iterativas: `loop while ... do ... done`.
    * Estructuras condicionales múltiples: `when ... elsewhen ... else ... done`.
* **Expresiones:** * Operadores aritméticos (asociativos por la izquierda) y división (recursiva por la derecha).
    * Operadores lógicos y relacionales con validación estricta de tipos en tiempo de compilación.
 
## 📂 Estructura del Repositorio

* `traductor/`: Contiene el núcleo del compilador (`cpt.jj`), desarrollado con **JavaCC**. Define la gramática léxica, sintáctica y la traducción dirigida por sintaxis.
* `lib/`: Librerías de soporte escritas en Java.
    * `symbolTable/`: Gestión de la Tabla de Símbolos, bloques de ámbito y clases de parámetros.
    * `tools/codeGeneration/`: Utilidades para la inyección y formateo de instrucciones P-Code.
* `test/`,`test_actual/`, `mis_tests/`,`extras/` : Baterías de pruebas de estrés, incluyendo algoritmos complejos por ejemplo:
    * El Juego de la Vida de Conway.
    * El problema de las N-Reinas.
    * Conjetura de Goldbach.
* `test.py`: Script en Python automatizado para compilar y ejecutar bancos de pruebas completos.
* `build.xml`: Archivo de configuración de Apache Ant para la compilación del proyecto.

## 🛠️ Requisitos Previos

Para compilar y ejecutar este proyecto necesitas tener instalado en tu sistema:
* **Java Development Kit (JDK)** 8 o superior.
* **Apache Ant** (para la automatización de la compilación).
* **Python 3** (opcional, para ejecutar el script de pruebas masivas).
* **JavaCC** (gestionado automáticamente a través de la tarea de Ant).

## 🚀 Instalación y Uso

### 1. Compilar el proyecto
Sitúate en el directorio raíz del repositorio y ejecuta Ant para limpiar versiones anteriores y compilar el archivo `.jj` junto con las clases de Java:

```bash
ant clean && ant

*Si la compilación es exitosa, se generará el árbol de clases en la carpeta `build/` y los ejecutables en `dist/`.*

### 2. Ejecutar pruebas automatizadas
Para lanzar el compilador sobre un directorio completo de archivos `.cpt` y ensamblarlos en la P-Máquina, utiliza el script de Python proporcionado:

    python3 test.py test_actual

### 3. Ejecución manual
El compilador generará un archivo `.pcode`. Si hay errores semánticos, léxicos o sintácticos, la generación se detendrá y se mostrará un mensaje de error estandarizado indicando la línea y columna del fallo.

---
*Proyecto de la asignatura Procesadores de Lenguajes - Universidad de Zaragoza*
