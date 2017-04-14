#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:46:58 2017

@author: booleanbite
"""
from calculadora import Calculadora

def test_suma():
    calc= Calculadora(2,2)
    assert calc.suma() == 4
                    
def test_resta():
    calc= Calculadora(2,2)
    assert calc.resta() == 0
                    
def test_mult():
    calc= Calculadora(2,2)
    assert calc.mult() == 4

def test_div():
    calc= Calculadora(2,2)
    assert calc.div() == 1