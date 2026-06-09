//*****************************************************************
// File:   Attributes.java
// Author: Elias Zabaleta y Hugo López Navarro
// Date:   mayo 26
// Coms:   Clase para almacenar los atributos sintetizados durante 
//         el análisis sintáctico y la generación de código.
//*****************************************************************

package lib.attributes;

import lib.symbolTable.Symbol;
import lib.tools.codeGeneration.CodeBlock;

public class Attributes {
    // Bloque de código asociado a la expresión o instrucción
    public CodeBlock code;
    
    // Tipo de la expresión, para comprobaciones semánticas
    public Symbol.Types type; 
    
    // Constructor por defecto
    public Attributes() {
        this.code = new CodeBlock();
        this.type = Symbol.Types.UNDEFINED; 
    }
}
