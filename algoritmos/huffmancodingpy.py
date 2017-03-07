#!/usr/bin/python
#coding: utf-8
import kivy
kivy.require('1.9.1')
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
import time
from heapq import heappush, heappop, heapify
from collections import defaultdict

texto = defaultdict(int)
resultado = ''
freqLetra = defaultdict(int)

def encode(texto):
    global txt
    heap = [[peso, [caractere, ""]] for caractere, peso in texto.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for par in lo[1:]:
            par[1] = '0' + par[1]
        for par in hi[1:]:
            par[1] = '1' + par[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

class FirstScreen(Screen):
    def auxEncode(self,*args):
        global resultado
        global freqLetra
        freqLetra = defaultdict(int)
        entrada = self.ids.my_txt.text
          
        for caractere in entrada:
            freqLetra[caractere] += 1

        resultado = encode(freqLetra)

class SecondScreen(Screen):
    def imprime(self,*args):
        global resultado
        global freqLetra
        #label1 = self.ids.my_imprime1
        label2 = self.ids.my_imprime2
        #label3 = self.ids.my_imprime3
        #label4 = self.ids.my_imprime4
        #label1.text = "Caractere Frequencia Codigo"
        for elemento in resultado:
            label2.text += "%s     %s     %s"%(elemento[0],freqLetra[elemento[0]],elemento[1])+'\n'

class MyScreenManager(ScreenManager):
    pass

class HuffmanCodingPy(App):
    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    HuffmanCodingPy().run() 
    
