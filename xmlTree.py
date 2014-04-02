#!/usr/bin/env python2
# -*- coding: utf8 -*-
"""
    Library for XML processing
    ->    class XML Tree Builders
"""

__author__ = "Habiboulaye AMADOU BOUBACAR (habiboulaye@gmail.com)"
__version__ = "$Revision: 1.12 $"
__date__ = "$Date: 2013/01/17 15:18:15 $"
__copyright__ = "Copyright (c) Free 2013"
__license__ = "Python"

import sys
from lxml import etree as eTree
from pyLxml import _Trace, _Debug, _ERROR_PROG


##################################################################################
class cXmlTree:
    """
        class XML Tree Builder
    """
    def __init__(self, inFileName):
        if bool(_Debug):
            print 'xmlDocTree: Init constructor'
        try:
            pT=eTree.XMLParser(remove_blank_text=False)
            _docTree=eTree.parse(inFileName, parser=pT)
        except Exception, Err:  #ERREUR !
            sys.stderr.write("\nEERREUR LORS DU CHARGEMENT/PARSING DU FICHIER : EXISTENCE OU FORMAT-XML ??: MSG <%s>\n" %Err)
            sys.exit(_ERROR_PROG) 
            
        self.docTree = _docTree
        self.root = _docTree.getroot()
        
    """ Parser events """ 
    def eventDoc(self, parser, elt):
        if bool(_Debug):
            print 'cXmlTree: eventDoc'
        pass
    
    def eventElement(self, parser, elt):
        if bool(_Debug):
            print ('cXmlTree: eventElement')
        pass
               
    def eventPI(self, parser, elt):
        if bool(_Debug):
            print ('cXmlTree: eventPI')
        pass
    
    def eventComment(self, parser, elt):
        if bool(_Debug):
            print ('cXmlTree: eventComment')
        pass
   
    def insertXmlElement(self, newChild, refChild, ipos=-1):
        if bool(_Debug):
            print ('cXmlTree: insertXmlElement')
        if (newChild==None) or (refChild==None):
            sys.stderr.write("ERROR-imput insertXmlElement: Element newChild or refChild is inconsistent \n\tMSGinfo: newChild=%s refChild=%s" %(newChild,refChild))
            sys.exit(_ERROR_PROG)
        try:
            parent=refChild.getparent()
            #print 'refChild.getparent()', refChild, refChild.getparent()
            refIndex=parent.index(refChild)
            if (ipos == -1):    # insertion de newChild Before<-1> refChild
                parent.insert(refIndex,newChild)
                return True
            elif (ipos == +1):  # insertion de newChild After<+1> refChild
                parent.insert(refIndex+1,newChild)
                return True
            elif (ipos == 0):   # Remplacement<0> de newChild par refChild
                parent.insert(refIndex,newChild)
                parent.remove(refChild)
                return True
        except Exception, Err:
            sys.stderr.write("ERROR insertXmlElement: %s" %(Err))
            sys.exit(_ERROR_PROG)
    
    def removeXmlElement(self, Child):
        if bool(_Debug):
            print ('cXmlTree: removeXmlElement')
        if (Child==None):
            if bool(_Trace):
                sys.stderr.write("WARRING-imput removeXmlElement: Element is incorrect \n\tMSGinfo: ELT=%s" %(Child))
            #sys.exit(_ERROR_PROG)
            return 0
        try:
            parent=Child.getparent()
            parent.remove(Child)
            return True
        except Exception, Err:
            sys.stderr.write("ERROR removeXmlElement: %s" %(Err))
            sys.exit(_ERROR_PROG)

    """ DTD validation """
    def DTDvalid(self, dtdFile):
        if bool(_Debug):
            print ('cXmlTree: DTDvalid')
        DTD = eTree.DTD(dtdFile)
        if DTD.validate(self.root): return True
        else:   return False
        
    def printXmlDoc(self, outFile):
        if bool(_Debug):
            print 'cXmlTree: printXmlDoc'
        self.docTree.write(outFile,method="xml",xml_declaration=True,encoding="UTF-8",pretty_print=False)

