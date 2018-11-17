import turtle
import math
wn=turtle.Screen()
wn.bgcolor('black') #背景设置为黑色

Sun=turtle.Turtle()
Sun.penup()
Sun.goto(-120,0)
Sun.dot(30,'orange')
Sun.hideturtle() #画出太阳

Mercury=turtle.Turtle() #水星
Venus=turtle.Turtle() #金星
Earth=turtle.Turtle() #地球
Mars=turtle.Turtle() #火星
Jupiter=turtle.Turtle() #木星
Satern=turtle.Turtle() #土星

def Planet_Setup(s,a,c,color):
    b=a*0.9
    m=(a*a-b*b)**0.5
    s.shape('circle')
    s.pensize(1.75)
    s.speed(0)
    s.pencolor(color)
    s.color(color)
    s.shapesize(c,c,1)
    s.penup()
    s.goto(m+a-120,0)
    s.pendown()
#设置基本参数与起始位置

def Draw_Planet(s,a,n,v):
    b=a*0.9
    m = (a*a-b*b) ** 0.5
    s.goto(m+a*math.cos(math.radians(n*v))-120,b*math.sin(math.radians(n*v)))
#行星运行

Planet_Setup(Mercury,35,0.6,'white')
Planet_Setup(Venus,55,0.8,'yellow')
Planet_Setup(Earth,85,0.9,'blue')
Planet_Setup(Mars,125,0.7,'red')
Planet_Setup(Jupiter,190,2,'sea green')
Planet_Setup(Satern,275,1.8,'grey')

for n in range(100000000000000000):
    Draw_Planet(Mercury,35,n,7)
    Draw_Planet(Venus,55,n,5)
    Draw_Planet(Earth,85,n,3)
    Draw_Planet(Mars,125,n,1.5)
    Draw_Planet(Jupiter,190,n,1)
    Draw_Planet(Satern,275,n,0.8)
