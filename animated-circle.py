# animated-circle.py
# Program to animate a circle
# Author: Austin Clayton
# Date Created: 5/8/2018

from graphics import *

def main():
    # create a graphics window
    win = GraphWin("Circle Animation", 450, 300)
    win.setBackground("black")
    
    # White circle
    shape = Circle(Point(250,45), 10)
    shape.setOutline("black")
    shape.setFill("cyan")
    shape.draw(win)

    # White circle
    shape2 = Circle(Point(100,150), 10)
    shape2.setOutline("black")
    shape2.setFill("pink")
    shape2.draw(win)

    # White circle
    shape3 = Circle(Point(250,250), 10)
    shape3.setOutline("black")
    shape3.setFill("orange")
    shape3.draw(win)

    # Create movement variables
    dx = 1
    dy = 1

    # Create movement variables
    dx2 = 1
    dy2 = 1

    # Create movement variables
    dx3 = 1
    dy3 = 1

    # animate circle
    for i in range(10000):
        shape.move(dx,dy)
        center = shape.getCenter()

        x = center.getX()
        y = center.getY()
        if((x > 440) or (x < 10)):
            dx = -dx
        if((y > 290) or (y < 10)):
            dy = -dy

        shape2.move(dx2,dy2)
        center2 = shape2.getCenter()

        x2 = center2.getX()
        y2 = center2.getY()
        if((x2 > 440) or (x2 < 10)):
            dx2 = -dx2
        if((y2 > 290) or (y2 < 10)):
            dy2 = -dy2

        shape3.move(dx3,dy3)
        center3 = shape3.getCenter()

        x3 = center3.getX()
        y3 = center3.getY()
        if((x3 > 440) or (x3 < 10)):
            dx3 = -dx3
        if((y3 > 290) or (y3 < 10)):
            dy3 = -dy3
        update(30) # pause so rate is not more than 30 times a second

    win.getmouse()
    win.close()

main()
