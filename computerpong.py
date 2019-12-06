#!/usr/bin/env python3

import turtle 
import os
 #lets u do some basic graphics for beginners best (inbuilt)

wn = turtle.Screen()       #creating window
wn.title("Ping Pong You Vs The Computer Game ")    #giving title 
wn.bgcolor("black")
wn.setup(width=800,height =600)
#wn.tracer(0)  #stops window from updsating so as to increase game speed

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(10)    #ets speed to max possible speed
paddle_a.shape("square")     #default 20*20 px
paddle_a.shapesize(stretch_wid=5,stretch_len=1)    #stretch
paddle_a.color("white")
paddle_a.penup()    #to not draw lines as it moves
paddle_a.goto(-350,0)

speed = 5

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)    #ets speed to max possible speed
paddle_b.shape("square")     #default 20*20 px
paddle_b.shapesize(stretch_wid=5,stretch_len=1)    #stretch to 5 times 20 and 
paddle_b.color("white")
paddle_b.penup()    #to not draw lines as it moves
paddle_b.goto(350 ,0)

#paddle_ball
ball = turtle.Turtle()
ball.speed(speed)    #ets speed to max possible speed
ball.shape("circle")     #default 20*20 px    #stretch
ball.color("white")
ball.penup()    #to not draw lines as it moves
ball.goto(0,0)
ball.dx = 2				#delta x : every time ball moves it moves by 2 px right(as +ve2)
ball.dy = 2				#delta y : every time ball moves it moves by 2 px up(as +ve2)

miss = 0
hit = 0

#pen
pen = turtle.Turtle()
pen.speed(0)      #animation speed
pen.color("white")
pen.penup()
pen.hideturtle()    #to hide it as we only want to see its text that it writes
pen.goto(0,260)
pen.write("Miss : {} Hit : {} Level : {} ".format(miss,hit,(5-speed)),align="center",font=("Courier",24,"normal"))

#score



#function 
def paddle_a_up():
	y = paddle_a.ycor()         #module of turtle remains y cordinate
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()         
	y -= 20
	paddle_a.sety(y)				#module of turtle sets y cordinate

def paddle_b_up():
	y = paddle_b.ycor()         
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()         
	y -= 20
	paddle_b.sety(y)

"""def ball_up():
	ball.sety(ball.ycor() + ball.dy)

def ball_down():
	ball.sety(ball.ycor() - ball.dy)

def ball_left():
	ball.setx(ball.xcor() - ball.dx)

def ball_right():
		ball.setx(ball.xcor() + ball.dx)"""
#keyboard binding
wn.listen()    #listen keyboard input
"""wn.onkeypress(paddle_a_up,"w")    #on pressing w call function paddle_a_up
wn.onkeypress(paddle_a_down,"s")"""
wn.onkeypress(paddle_b_up,"Up")    
wn.onkeypress(paddle_b_down,"Down")

"""wn.onkeypress(ball_up,"8")
wn.onkeypress(ball_left,"4")
wn.onkeypress(ball_right,"6")
wn.onkeypress(ball_down,"5")"""

#main game loop
while True:
	wn.update()       #everytime the loop runs it updates the window

	#move the ball
	
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)


	if ball.xcor() < 0 and ball.dx == -2 :
		#print(ball.ycor()," ",paddle_a.ycor())
		if(ball.ycor() < paddle_a.ycor() - 40):
			#print("i was here")
			paddle_a_down()
			#print(ball.ycor()," ",paddle_a.ycor())
		elif(ball.ycor() > paddle_a.ycor() + 40):
			paddle_a_up()
			#print(ball.ycor()," y ",paddle_a.ycor())




	#border checking
	if ball.ycor() > 290:
		os.system("aplay pong.wav&")
		ball.sety(290)
		#print("no up")
		ball.dy *= -1      #reverses the ball direction

	if ball.ycor() < -290:
		os.system("aplay pong.wav&")
		ball.sety(-290)
		#print("no down")
		ball.dy *= -1

	if ball.xcor() > 350:
		os.system("aplay crash.wav&")
		#ball.hideturtle()
		ball.setpos(0,0)
		#ball.showturtle()
		ball.dx *= -1
		miss +=1
		pen.clear()
		pen.write("Miss : {} Hit : {} Level : {} ".format(miss,hit,(5-speed)),align="center",font=("Courier",24,"normal"))


	if ball.xcor() < -350:
		os.system("aplay crash.wav&")
		#ball.hideturtle()
		ball.setpos(0,0)
		#ball.showturtle()
		ball.dx *= -1
		#score_b +=1
		#pen.clear()
		#pen.write("Player A : {} Player B : {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

	if paddle_a.ycor() > 250:
		paddle_a.sety(250)

	if paddle_a.ycor() < -250:
		paddle_a.sety(-250)

	if paddle_b.ycor() > 250:
		paddle_b.sety(250)

	if paddle_b.ycor() < -250:
		paddle_b.sety(-250)

			

	#paddle and ball collide
	
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
		os.system("aplay pong.wav&")
		hit+=1
		if hit % 5 == 0 :
			speed -=1
			print(speed)
			
		if speed <= -1 :
			wn.tracer(0)
		else :
			ball.speed(speed)

		pen.clear()
		pen.write("Miss : {} Hit : {} Level : {} ".format(miss,hit,(5-speed)),align="center",font=("Courier",24,"normal"))
		ball.setx(340) 
		#print("here")
		ball.dx *= -1

	elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
		os.system("aplay pong.wav&")
		ball.setx(-340)
		#print("t here")
		ball.dx *= -1