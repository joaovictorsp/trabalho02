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

itens2 = [] #vetor com as partes usadas dos itens
peso = [] #vetor de pesos dos itens
valor = [] #vetor de valores dos itens
capacidade = 0 #capacidade da mochila
qtd = 0 # Quantidade de elementos
tam = 0 #tamanho do vetor
#itCont = 0 #contador de itens para armazenar a posição

class Item:
	def __init__(self,valor,peso,valorAbsoluto,itCont):
		self.valor = valor
		self.peso = peso
		self.valorAbsoluto = valorAbsoluto
		self.itCont = itCont

itens = []

def ordenaItens(valor,peso,valorAbsoluto):
	for j in range(o,len(valorAbsoluto)):
		for i in range(0,len(valorAbsoluto) - 1):
			if valorAbsoluto[i] > valorAbsoluto[i+1]:
				aux = valorAbsoluto[i+1]
				valorAbsoluto[i+1] = valorAbsoluto[i]
				valorAbsoluto[i] = aux #valorAbsoluto = valor/peso
				#Ordenar os vetores de acordo com o maior valor absoluto valor/peso

	return valorAbsoluto
			

def mochilaFracionaria(peso,valor,qtd,capacidade):
	global itens
	aux = 0.0
	#vet = [0 for x in range(100)]
	vet = []
	indice = 0
	j = qtd-1

	while j >= 0:
		if peso[j] <= capacidade:	
			vet.append(1)
			capacidade = capacidade - peso[j]
		else:
			aux = float(capacidade)/float(peso[j])
			aux = format(aux,'.2f')
			vet.append(float(aux))
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

		valor = int(self.ids.my_val.text)
		peso = int(self.ids.my_peso.text)
		valorAbsoluto = float(valor/peso)
		qtd += 1
		
		itens.append(Item(valor,peso,valorAbsoluto,qtd))

		#it.valor.append(valor)
		#it.peso.append(peso)
		#it.valorAbsoluto.append(float(valor/peso))
		
		self.ids.my_val.text = '0'
		self.ids.my_peso.text = '0'
	
	def Resolve(self,*args):
		global it
		global itens
		global itens2
		global capacidade
		global qtd

		itens.sort(key=attrgetter("valorAbsoluto"))	
		peso = []
		valor = []
		#for i in range(len(itens)):
		#	peso.append(itens[i].peso)
		#	valor.append(itens[i].valor)

		for elem in itens:
			peso.append(elem.peso)
			valor.append(elem.valor)

		itens2 = mochilaFracionaria(peso,valor,qtd,capacidade)

class ThirdScreen(Screen):
	def Imprime(self,*args):
		global capacidade
		global it
		global capacidaded
		global qtd
		global itens
		global itens2

		label = self.ids.my_imprime
		i = 0 

		#i = qtd
		#while i >= 1:
		#	label.text += ' '+str(itens2[i])+' '
		#	i -= 1
		#for i in range(len(itens2)):
		#	label.text += ' '+str(itens2[i])+' '
		label.text = ''
		i = qtd - 1
		for elem in itens2:
			label.text += ' '+str(elem)+' do item %d'%(itens[i].itCont)+'\n'
		 	i -= 1

class MyScreenManager(ScreenManager):
	pass

class MochilaFracionariaApp(App):
	def build(self):
		return MyScreenManager()

if __name__ == '__main__':
	MochilaFracionariaApp().run()
