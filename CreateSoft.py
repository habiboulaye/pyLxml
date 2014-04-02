#!/usr/bin/env python2
# -*- coding: utf8 -*-
""" 
ClassTemplet: model to create soft based-on pyLxml 

Usage : 
    - Replace ClassTemplet by your Class name 

CMD: python CreateSoft.py in.xml out.xml

"""

__author__ = "Habiboulaye AMADOU BOUBACAR (habiboulaye@gmail.com)"
__version__ = "$Revision: 1.1 $"
__date__ = "$Date: 2009/11/18 17:58:11 $"
__copyright__ = "Copyright (c) free 2013"
__license__ = "Python"

#-------------Importation des modules -----------------------------------------------
import time, sys

#sys.path.append("Path/to/pyLxml/..")
#import pyLxml
#sys.path.remove("Path/to/pyLxml/..")

from pyLxml.xmlParser import cXmlParser
from pyLxml.xmlTree import cXmlTree
from pyLxml import _Trace, _Debug, _ERROR_CMD, _ERROR_INPUT

print "\t\t", time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime())

#------------ Main class -----------------------------------------------------------
class ClassTemplet(cXmlTree):
    """
         ClassTemplet: inheritance from cXmlTree
    """
    def __init__(self,inXML):
        self._Trace, self._Debug=_Trace, _Debug
        if bool(self._Debug):
            print 'ClassTemplet: Init constructor'
        cXmlTree.__init__(self, inXML)

    def xmlProcessing(self, outFile, level):
        """
           Call cXmlParser:xmlWalker to parse the file 
        """
        if bool(self._Debug):
            print 'ClassTemplet: xmlProcessing'
        xmlParser = cXmlParser(self)
        xmlParser.xmlWalker(self.root, level)


    # Events: rewrite event-functions that are needs
    def eventElement(self, parser, elt):
        """
            Event -> Elements
        """
        if bool(self._Trace):
            print 'ClassTemplet: eventElement[%s : %s]' %(elt.tag, elt.attrib)
    # Process XML Elements
    # Write your codes ...

    def eventPI(self, parser, elt):
        """
            Event -> Processing Instructions
        """
        if bool(self._Trace):
            print 'ClassTemplet: eventPI[%s : %s]' %(elt.target, elt.text)
    # Process XML Processing Instructions
    # Write your codes ...
    
    def eventComment(self, parser, elt):
        """
            Event -> Comments
        """
        if bool(self._Trace):
            print 'ClassTemplet: eventComment[%s : %s]' %(elt.tag, elt.text)
        # Process XML Comments
        # Write your codes ...
        


#--------------------------------------------------------------------------------------
def usage():
    """usage: print documentation"""
    print( __doc__)
    
#--------------------------------------------------------------------------------------



#------------ Main function-----------------------------------------------------------
def main(argv):
    print "\n\t *_*_*_*_* Start Execution *_*_*_*_*\n"
    
    LConsole = True
    #---------------------------------------------------------------------------
    if LConsole: # Linux Console
        print ">>> Get commande line arguments"
        if len(sys.argv) == 3:
            inFile=sys.argv[1]
            outFile = sys.argv[2]        
        else:   #ERROR !
            sys.stderr.write("\nERROR COMMANDE :\n")
            usage()
            sys.exit(_ERROR_CMD)
    else:   # Local Execution
        inFile = 'sample.in.xml'
        outFile = 'sample.out.xml'
       
    #---------------------------------------------------------------------------
    try:
        infile=open(inFile, 'r')
        infile.close()
        print "inFile = [%s]" %(inFile.encode('UTF-8'))
    except Exception, Err: #ERREUR !
        sys.stderr.write("\nERROR: MSG <%s>\n" %Err)
        sys.exit(_ERROR_INPUT)
 
    #---------------------------------------------------------------------------
    print ("\n>>> Instanciate ClassTemplet child of class cXmlTree") 
    objTree = ClassTemplet(inFile)

    #---------------------------------------------------------------------------
    print ("\n>>> Process cXmlParser:xmlWalker on the instantied tree")
    objTree.xmlProcessing(outFile, level=0)
   
    #---------------------------------------------------------------------------
    print ("\n>>> Call cXmlTree:printxmlDoc to produce the (modified) XML output")
    objTree.printXmlDoc(outFile)

    #---------------------------------------------------------------------------
    print ("\n\t *_*_*_*_* Successful Execution *_*_*_*_*\n\n")

if __name__ == '__main__':
    main(sys.argv[1:])
    print "\t\t", time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.localtime())
      
