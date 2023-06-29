# QuartzzDev <3

import turtle

print("Yazılacak İsim : ","\n Mümkünse Kısa Olsun")
write = input("")

pen = turtle.Turtle()


def curve():
  for i in range(200):

    pen.right(1)
    pen.forward(1)


def heart():
  pen.fillcolor('red')
  pen.begin_fill()
  pen.left(140)
  pen.forward(113)
  curve()
  pen.left(120)
  curve()
  pen.forward(112)
  pen.end_fill()


def writeName():
  pen.up()
  pen.setpos(-33, 95)
  pen.down()
  pen.color('black')
  pen.write(write, font=("Qairen", 12, "bold" , "italic"))

heart()
writeName()
pen.ht()

x = input("")    # Gelen Şeklin Ekrandan Gitmemesi İçin
