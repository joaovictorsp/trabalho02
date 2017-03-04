#!/usr/bin/python

import kivy
kivy.require('1.9.1')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
import sys

qtd = 0
linhas = []
colunas = []
b = []
lcont = 0
ccont = 0
mcont = 0

def MAXVAL(m):
	aux = []
	for i in m:
		for j in i:
			aux.append(i)
	return max(aux)

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
		m = []
		m2 = []
		i = 0
		j = 0

		#vetor com os valores de b
		b.append(linhas[0])
		b.append(colunas[0])
		i = 1
		while i < qtd:
			b.append(colunas[i])
			i += 1

		#fazendo uma matriz preenchida com 0
		i = 0
		for i in range(qtd):
			linha = []
			for j in range(qtd):
				linha.append(0)
			m.append(linha)

		#Calculando os valores
		d = qtd
		#distancia 1
		i = 0
		j = 0
		k = 1
		valor = 0

		n = len(b)
		tam = 1
		while tam < n:
			i = 0
			while i < n -tam:
				j = i + tam
				m[i][j] = sys.maxint
				k = 1
				while k < j:
					custo = m[i][k] + m[k+1][j] + b[i]*b[k+1]*b[j+1]
					if custo < m[i][j]:
						m[i][j] = custo
						s[i][j] = k
					k+=1
				i+=1
			tam+=1
		
			
class SecondScreen(Screen):
	def Imprimir(self,*args):
		pass

class MyScreenManager(ScreenManager):
	pass

class CalculaMatrizApp(App):
	def build(self):
		return MyScreenManager()

if __name__ == '__main__':
	CalculaMatrizApp().run()



