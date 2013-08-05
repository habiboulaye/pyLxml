pyLxml
======

Python XML library with some basic classes and functions to easly process XML data.

1. pyLxml module:
    
    cXmlTree: generic class for building Tree structure for XML data
      - eventElement, eventPI, eventComment ...: event functions
      - functions to insert and remove elements: insertXmlElement, removeXmlElement
      - DTDvalid: function to verify the XML conformity file with regard a DTD
      - printXmlDoc: function to print/white the (modified) XML output
    
    cXmlParser: class for parsing xml Tree, intanciated object from cXmlTree
      - xmlWalker: parsing function using preorder transversal of XML nodes, throwing events
    
2. Usage-DEV:

    ClassTemplet: model/example to use to create new classes based on the pyLxml module.
      - ClassTemplet(cXmlTree) : Your class inherits from the generic class
      - You then only have to re-write the event functions that are useful for your needs


3. Install-Require:

      - python 2.7
      - lxml 2.2.8
      - pyLxml ()

4. Usage-CMD
      
    Console mode: Turn LConsole=True (main function) 
      > python CreateSoft.py sample.in.xml sample.out.xml
      
    Local model: overwise
      Ø Run
    
