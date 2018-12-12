#coding: utf-8
#UFCG 2018.2 - FMCC2
#Aluno: Gabriel Carvalho de Lima
#matrícula: 118110237
#Atividade: Lista3

import cv2
import os

#pegando o nome das 2 imagens no diretorio input
caminho = os.listdir("../input/")

#usando o opencv para criar a representacao das imagens atravez de vetores salvos nas variaveis
img1 = cv2.imread("../input/" + caminho[0],-1)
img2 = cv2.imread("../input/" + caminho[1],-1)

#string para dar nome as novas imagens a serem geradas
a = "0"

#criando o alfa e o beta para realizar o fade atraves de uma combinacao convexa
#o alfa e um valor real entre 0 e 1, que comeca como 0
#o beta e 1 - alfa, pois alfa + beta = 1
beta = 0
alfa = 1-beta

#nesse laco o valor de beta e decrementado enquanto o de alfa e incrementado em uma taxa de 0,1 por imagem
for i in xrange(11):
	b = int(a) + 1
	cv2.imwrite("../output/imagem"+ a +".jpg",alfa*img1 + beta*img2) #aqui ocorre a expressao da combinacao em si onde cada imagem e gerada 
	print "%d vez: 1 imagem: %.1f   |   2 imagem: %.1f" % (i, alfa, beta) #aqui e mostrado o nivel de alfa e beta de cada imagem gerada 
	a = str(b)
	beta += 0.1
	alfa = 1-beta

