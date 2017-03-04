#!/usr/bin/python
#coding: utf-8
import kivy
kivy.require('1.9.1')
from kivy.uix.boxlayout import BoxLayout
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
import random

resp = ''

def lcs(a, b):
       tam = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
       for i, x in enumerate(a):
           for j, y in enumerate(b):
               if x == y:
                   tam[i+1][j+1] = tam[i][j] + 1
               else:
                   tam[i+1][j+1] = max(tam[i+1][j], tam[i][j+1])
       subsequencia = ""
       x, y = len(a), len(b)
       while x != 0 and y != 0:
           if tam[x][y] == tam[x-1][y]:
               x -= 1
           elif tam[x][y] == tam[x][y-1]:
               y -= 1
           else:
               assert a[x-1] == b[y-1]
               subsequencia = a[x-1] + subsequencia
               x -= 1
               y -= 1
       return subsequencia

class FirstScreen(Screen):
    def calculaSubsequencia(self,*args):
        global resp
        str1 = self.ids.my_txt1.text 
        str2 = self.ids.my_txt2.text 
        resp = lcs(str1,str2)

class SecondScreen(Screen):
    def imprime(self,*args):
        global resp
        label = self.ids.my_subsequencia
        label.text = resp

class MyScreenManager(ScreenManager):
    pass

class LcsApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    LcsApp().run()

