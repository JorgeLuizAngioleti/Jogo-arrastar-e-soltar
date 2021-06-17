import turtle
import math
#config. janela
larg= 1400
alt = 800
janela = turtle.Screen()
janela.title('Arrastar e soltar')
janela.bgcolor('white')
janela.setup(larg,alt,50,50)
janela.tracer(0)
#registro de imagens/tem que ser gif
imagens = ['lar.gif','gato.gif','pato.gif','limao.gif',
           'base.gif','certo.gif','co.gif','ba.gif']
for i in imagens:
	janela.register_shape(i)

'''Class arrastar'''
class Arrastar(turtle.Turtle):
	def __init__(self, imagem):
		turtle.Turtle.__init__(self)
		#self.personagem = turtle.Turtle()
		self.up()
		self.shape(imagem)
		self.color('green')
		self.home()
		self.speed(0)
		self.ondrag(self.mover)

	def mover(self, x, y):
		self.ondrag(None)
		self.goto(x, y)
		self.ondrag(self.mover)

'''Class quadrado '''
class Quadrado(turtle.Turtle):
	def __init__(self, x, y, tam_al, tam_lar):
		turtle.Turtle.__init__(self)
		self.up()
		#self.pensize(20)
		self.shape('square')
		self.color('black','springgreen')
		self.goto(x, y)
		self.speed(0)
		self.turtlesize(tam_al, tam_lar,5)

def colisao(t1, t2):
    distancia = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distancia < 200:#raio de 200 meu quadrado tem 200
        return True
    else:
        return False
#texto
class Escreve(turtle.Turtle):
	def __init__(self, texto, x, y):
		turtle.Turtle.__init__(self)
		self.speed(0)
		self.up()
		self.hideturtle()
		self.color('green')
		self.setposition(x, y)
		self.write(texto, move=True, align="center", font=("Arial", 20, "normal"))
		
		
#barras
descricao = Quadrado(0,320, 4,larg)
descricao.color('black','limegreen')
descricao2 = Quadrado(0,-320, 4,larg)
descricao2.color('black','limegreen')
#objetos
q1 = Quadrado(-480,0, 20, 20)#20 equivale a 200
q1.shape('base.gif')
q2 = Quadrado(480,0, 20, 20)
q2.shape('base.gif')
p1 = Arrastar('lar.gif')
p2 = Arrastar('gato.gif')
p3 = Arrastar('pato.gif')
p4 = Arrastar('limao.gif')
p5 = Arrastar('co.gif')
p6 = Arrastar('ba.gif')
#venceu
c= Quadrado(550,-230, 2,2)
c.hideturtle()
c.shape('certo.gif')
#textos do jogo
escrever1 = Escreve("Animais", -480,200)
escrever2 = Escreve("Frutas", 480,200)
escrever3 = Escreve("Arraste para o quadrado corretamente as imagens:", 0,230)
escrever4 = Escreve("Informática Pedagógica", 0,-270)
while 1:
	janela.update()
	if colisao(q1,p2)and colisao(q2,p6)and colisao(q1,p5) and colisao(q1,p3) and colisao(q2,p1) and colisao(q2,p4):
		print('colisão')
		c.showturtle()
	else:
		print('afastou')	

janela.mainloop()
