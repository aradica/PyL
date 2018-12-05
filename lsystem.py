"""
Author: Andrija Radica

Računalno crtanje fraktala
Večer Matematike 6. prosinca, 2018.


Symbol interpretations:

F, G	Go forward by some number of units
f       Go forward by some number of units but don't draw
B	    Go backward by some number of units
-	    Turn left by some degrees
+	    Turn right by some degrees

"""

import turtle


def applyRules(string, rules):
    newstr = ""
    for char in string:
        if char in rules:
            newstr += rules[char]
        else:
            newstr += char
    return newstr


def drawSystem(turtle, instructions, angle, d):
    for cmd in instructions:
        if cmd == "F" or cmd == "G":
            turtle.forward(d)
        elif cmd == "f":
            turtle.penup()
            turtle.forward(d)
            turtle.pendown()
        elif cmd == "B":
            turtle.backward(d)
        elif cmd == "+":
            turtle.right(angle)
        elif cmd == "-":
            turtle.left(angle)
        


#axiom
string = "FX"
#rule dictionary
rules = {
    "X": "X+YF+",
    "Y": "-FX-Y"
}

angle = 90
iterations = 14


#number of iterations
for i in range(iterations):
    string = applyRules(string, rules)
    #print(string)

T = turtle.Turtle()
T.speed("fastest")
T._tracer(2, 0)

wn = turtle.Screen()
drawSystem(T, string, angle, 4)
T._update()
wn.exitonclick()