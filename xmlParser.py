#!/usr/bin/env python2
# -*- coding: utf8 -*-
"""
    Library for XML processing
    ->    class XML Parsers
"""

__author__ = "Habib"
__version__ = "$Revision: 1.12 $"
__date__ = "$Date: 2013/01/17 15:18:15 $"
__copyright__ = "Copyright (c) Free 2013"
__license__ = "Python"

from lxml import etree as eTree
from pyLxml import _Trace, _Debug

##################################################################################
class cXmlParser:
    """
        Class XML Parser
    """
    def __init__(self, docTree):
        if bool(_Trace):
            print ('cXmlParser: Init constructor')
        self.xmldocTree = docTree
   
    def xmlWalker(self, parent, level=0):
        if bool(_Trace):
            print ('xmlwalker: Init constructor')
        if parent is None:
            return False
        elif len(parent.getchildren())==0:
            return False
        if parent == self.xmldocTree.root:
            self.xmldocTree.eventDoc(self, parent)
          
        listElts=parent.getchildren()
        elt=listElts[0]
        while elt in listElts:
            if elt.tag is eTree.PI: #---> ProcessingInstruction
                if bool(_Debug):
                    print ('\nProcessingInstruction -> {0} {1}'.format(elt.target, elt.text))
                self.xmldocTree.eventPI(self, elt)
            elif elt.tag is eTree.Comment: #---> Comment
                if bool(_Debug):
                    print ('\nComment -> {0} {1}'.format(elt.tag, elt.text))
                self.xmldocTree.eventComment(self,elt)    
            else:   #---> XML Elements
                if bool(_Debug):
                    print ('\nElement -> {0} {1} {2}'.format(elt.tag, elt.attrib, elt.text))                
                self.xmldocTree.eventElement(self,elt)
            self.xmlWalker(elt, level+1)
            elt=elt.getnext()
    
                 
