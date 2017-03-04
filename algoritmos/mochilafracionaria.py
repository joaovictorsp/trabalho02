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
from operator import attrgetter
import time

itens = []
peso = []
valor = []
capacidade = 0
qtd = 0
tam = 0

class Item:
	def __init__(self,valor,peso,valioso):
		self.valor = valor
		self.peso = peso
		self.valioso = valioso

it = Item(0,0,0)

def mochilaFracionaria(peso,valor,qtd,capacidade):
	global itens

	indice = 0
	j = qtd

	while j >= 1:
		if peso[j] <= capacidade:	
			vet[j] = 1
			capacidade = capacidade - peso[j]
		else:
			vet[j] = capacidade/peso[j]
			capacidade = 0
		j -= 1

	return vet

class FirstScreen(Screen):
	def setaCap(self,*args):
		global capacidade
		capacidade = int(self.ids.my_cap.text)

class SecondScreen(Screen):
	def Insere(self,*args):
		peso = 0
		valor = 0
		global capacidade
		global itens
		global qtd
		global it
		i = 1

		valor = int(self.ids.my_val.text)
		peso = int(self.ids.my_peso.text)
		valioso = float(valor/peso)
		qtd += 1

		it[i] = Item(valor,peso,valioso)
		i += 1

		#it.valor.append(valor)
		#it.peso.append(peso)
		#it.valioso.append(float(valor/peso))
		
		self.ids.my_val.text = '0'
		self.ids.my_peso.text = '0'
	
	def Resolve(self,*args):
		global it
		global itens
		global capacidade
		global qtd

		it.sort(key=attrgetter("valioso"))	
		itens = mochilaFracionaria(it.peso,it.valor,qtd,capacidade)

class ThirdScreen(Screen):
	def Imprime(self,*args):
		global capacidade
		global it
		global capacidade
		global qtd
		global itens

		label = self.ids.my_imprime
		i = 0 

		i = qtd
		while i >= 1:
			label.text += ''+itens[j]
			i -= 1

		 

class MyScreenManager(ScreenManager):
	pass

class MochilaFracionariaApp(App):
	def build(self):
		return MyScreenManager()

if __name__ == '__main__':
	MochilaFracionariaApp().run()