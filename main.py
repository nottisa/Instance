class Instance:
    '''
    instanceMODULE made by: Trey Fleishman
    copyright: Trey Fleishman 2021
    This code is reserved under the non-comercial no derivs creative commons liscence and may not be used commerically under any circumstances except with written permission fronm the developer
    Since this code is reserved under the non-comercial no derivs creative commons liscence, you may also not distribute any re-builds or build upons at any time except with written permision from the devloper
    Legal code( https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode ), Human Readable Code( https://creativecommons.org/licenses/by-nc-nd/4.0/ )
    A KEY IS REQUIRED FOR INSTANCEMODULE TO WORK THIS KEY IS PRE-PROGRAMMED
    build: 2.14
    '''
    
    
    def __init__(self, key = 0):
        import sys
        self.key = key
        if(self.key == 127387892721):
            import turtle
            self.turtle1 = turtle.Turtle()
            self.whatIsInstance = "Instance is a tool that I have created for drawing certain objects such as a superhero or box."
            self.help = "Here are some commands: help, whatIsInstance, makeBox, makeTriangle, changeVar. You can get help for a specific command by using help + (space) + (your command)"
            self.helpHelp = "Use the help command to figure out what commands do by using help+(space)+(your command)"
            self.helpMakeTriangle = "makeTriangle is a command used for making a triangle in python"
            self.helpMakeBox = "makeBox is command used for making a box in python. The variable boxSide1 is for the horizontal side and boxSide2 is for the vertical side. This uses the variable turtleColor and turtleSpeed as well. Change the length by using command changeVar."
            self.variablenotfoundforchangevar = "That variable is not available at this time please try one of the following variables: boxSide1, boxSide2, turtleColor, turtleSpeed, triangleSide1, triangleSide2, triangleSide3, triangleAngle1, triangleAngle2, or triangleAngle3."
            self.helpchangevar = "Change a parameter by calling this function. The current variables are; boxSide1, boxSide2, turtleColor, turtleSpeed, triangleSide1, triangleSide2, triangleSide3, triangleAngle1, triangleAngle2, and triangleAngle3. Depending on the variable it should be a string or an interger."
            self.commandNotValid = "That command is not valid. Try using help."
            self.boxSide1 = 100
            self.boxSide2 = 100
            self.turtleColor = "black"
            self.turtleVisible = True
            self.turtleSpeed = 10
            self.angle1 = 60
            self.angle2 = 60
            self.angle3 = 60
            self.triangle1 = 100
            self.triangle2 = 175
            self.triangle3 = 100
            self.angleI1 = 150 #makes sure angles ar in degrees (I hope)
            self.angleI2 = 150
            self.angleI3 = 150
        else:
            print("Key Invalid Please get a key")
            sys.exit()

    def changeturtleval(self, input, value):
      if input == "visible":
        if value == True:
          self.turtle1.showturtle()
        elif value == False:
          self.turtle1.hideturtle()
        else:
          raise ValueError("Value incorrect")
      else:
        raise ValueError("Input Invalid")
    def makeBox(self): #make sure functions are not inside def __init__(self):
        if(self.key == 127387892721):
            if(self.boxSide1 == 100 and self.boxSide2 == 100):
               print("Default values are being used for the box. Change these values to get a diffrent sized box.")
            self.turtle1.color(str(self.turtleColor))


            self.turtle1.speed(float(self.turtleSpeed))
            self.turtle1.forward(float(self.boxSide1))
            self.turtle1.right(90)
            self.turtle1.forward(float(self.boxSide2))
            self.turtle1.right(90)
            self.turtle1.forward(float(self.boxSide1))
            self.turtle1.right(90)
            self.turtle1.forward(float(self.boxSide2))
            self.turtle1.right(90)
        else:
            print("Key Invalid Please get a key")
    def makeTriangle(self):
        if(self.key == 127387892721):
          if(self.angle1 == 60 and self.angle2 == 60 and self.angle3 == 60 and self.triangle1 == 100 and self.triangle2 == 100 and self.triangle3 == 100):
            print("Default values will be used when creating the triangle as they have not been changed.")
          if((float(self.angle1) + float(self.angle2) + float(self.angle3)) == 180): #makes sure angles add up to 180 
            self.turtle1.color(str(self.turtleColor))
            self.turtle1.speed(float(self.turtleSpeed))
            self.turtle1.forward(float(self.triangle1)) #umm we need some more calculations + I kind of want to make a completly custom triangle
            self.turtle1.right(float(self.angleI1))
            self.turtle1.forward(float(self.triangle2))
            self.turtle1.right(float(self.angleI2))
            self.turtle1.forward(float(self.triangle3))
            self.turtle1.right(float(self.angleI3))
          else:
            print("Error cannot make triangle. Angles do not add up to 180. You need the angles to add to 180. Please try again.")
        else:
            print("Key Invalid Please get a key")
