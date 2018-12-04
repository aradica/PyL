"""
Author: Andrija Radica

Računalno crtanje fraktala
Večer Matematike 6. prosinca, 2018.


Symbol interpretations:

F	Go forward by some number of units
B	Go backward by some number of units
-	Turn left by some degrees
+	Turn right by some degrees

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
        if cmd == "F":
            turtle.forward(d)
        elif cmd == "B":
            turtle.backward(d)
        elif cmd == "+":
            turtle.right(angle)
        elif cmd == "-":
            turtle.left(angle)
        


#axiom
string = "F-F-F-F"

#rule dictionary
rules = {
    "F": "F-F+F+FF-F-F+F"
}


#number of iterations
for i in range(3):
    string = applyRules(string, rules)
    #print(string)

T = turtle.Turtle()
#T.speed("fastest")
T._tracer(2, 0)

wn = turtle.Screen()
drawSystem(T, string, 90, 2)
T._update()
wn.exitonclick()