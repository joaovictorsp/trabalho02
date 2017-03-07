#!/usr/bin/python
#coding: utf-8
import kivy
kivy.require('1.9.1')
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition

qtd = 0 #quantida de matrizes
linhas = []  #vetor de linhas das matrizes
colunas = [] #vetor de colunas das matrizes
custo = 0 #custo da multiplicação das matrizes


def calculaMatriz(vet):
	#qtd = numero de matrizes
	qtd = len(vet) - 1
	custo = [[0 for i in range(qtd)] for j in range(qtd)]

	for tam in range(2, qtd + 1):
		for inicio in range(qtd - tam + 1):
			fim = inicio + tam -1
			custo[inicio][fim] = float('inf')

			for meio in range(inicio,fim):
				aux = custo[inicio][meio] + custo[meio+1][fim] + vet[inicio]*vet[meio+1]*vet[fim+1]
				custo[inicio][fim] = min(custo[inicio][fim],aux)
		return custo[0][qtd-1]

class FirstScreen(Screen):
	def setaMatriz(self,*args):
		global lcont
		global ccont
		global linhas
		global colunas
		global mcont
		global qtd

		#linhas[lcont] = int(self.ids.my_linhas.text)
		linhas.append(int(self.ids.my_linhas.text))
		colunas.append(int(self.ids.my_colunas.text))
		qtd += 1

	def calcula(self,*args):
		global qtd
		global linhas
		global colunas
		global custo
		m = []
		m2 = []
		i = 0
		j = 0
		b = []

		b.append(linhas[0])
		b.append(colunas[0])
		i = 1
		while i < qtd:
			b.append(colunas[i])
			i += 1

		custo = calculaMatriz(b)

class SecondScreen(Screen):
	def imprime(self,*args):
		global custo
		label = self.ids.my_imprime1

		label.text = 'Custo da multiplicação:\n'
		custo = format(custo,'.2f')
		label.text += '%s'%(custo)

class MyScreenManager(ScreenManager):
	pass

class MultiplicacaoMatrizApp(App):
	def build(self):
		return MyScreenManager()

if __name__ == '__main__':
	MultiplicacaoMatrizApp().run()


