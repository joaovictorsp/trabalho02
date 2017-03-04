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

itens = 0
its = 0
capacidade = 0
c = []
p = []
v = []
resultado = []
item = []

class FirstScreen(Screen):
	text = StringProperty('')
	def setaCap(self,*args):
		global capacidade
		global c
		capacidade = int(self.ids.my_cap.text)
		cap = capacidade
		i = 0
		while i <= cap:
			c.append(i);
			i += 1 

		self.ids.my_cap.text = '0'


class SecondScreen(Screen):
	def insere(self,*args):
		global itens
		global v
		global p
		v.append(int(self.ids.my_val.text))
		p.append(int(self.ids.my_peso.text))
		itens += 1
		self.ids.my_val.text = '0'
		self.ids.my_peso.text = '0'


	def resolveMochila(self,*args):
		global c
		global capacidade
		global itens
		global item
		cap = capacidade
		its = 0
		i = 0
		j = 0
		elems = itens
		print str(elems) + '\n'

		#Monta uma matriz com 0 em todas posições
		for i in range(elems+1):
			linha = []
			for j in range(cap+1):
				linha.append(0)
			resultado.append(linha)
		
		#Setando primeiro elemento dos vetores valor e peso como 0
		v.append(0)
		p.append(0)
		
		#Resolve o problema preenchendo a matriz com os valores dos itens na mochila
		i = 0
		j = 0
		while j <= elems:
			while i <= cap:
				if j > 0:
					if p[j] == c[i] and v[j] >= resultado[j-1][i]:
						resultado[j][i] = v[j];
					elif p[j] < c[i] and (v[j] + resultado[j-1][c[i]-p[j]]) > resultado[j-1][i]:
						resultado[j][i] = v[j] + resultado[j-1][c[i] - p[j]]
					else:
						resultado[j][i] = resultado[j-1][i] 

				i += 1
			j += 1
			i = 1

		#Verifica quais os elementos contidos na mochila e adiciona no vetor item
		i = cap
		j = elems
		global its
		while(j != 0):
			if resultado[j][i] != resultado[j-1][i]:
				item.append(j)
				its += 1
			j = j-1
			i = i - j

class ThirdScreen(Screen):
	def Imprime(self,*args):
		global capacidade
		global itens
		global item

		label = self.ids.my_imprime1
		i = 0
		label.text += '\n'
		while i < capacidade:
			label.text += str(resultado[itens][i])+','
			i += 1

	def ImprimeElementos(self,*args):
		global its
		global item
		i = 0
		label = self.ids.my_imprime2
		label.text += '\n'
		while i < its:
			label.text +=str(item[i]+1)+',' #+1 pois o vetor inicia em 0
			i += 1



class MyScreenManager(ScreenManager):
	pass

class MochilaBoolApp(App):
	def build(self):
		return MyScreenManager()

if __name__ == '__main__':
	MochilaBoolApp().run()


