#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:55:16 2017

@author: victor
"""

class Calculadora:
    
    a=0
    b=0
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def suma(self):
        return self.a+self.b
    
    def resta(self):
        return self.a-self.b
    
    def mult(self):
        return self.a*self.b
    
    def div(self):
        return self.a/self.b
pass
