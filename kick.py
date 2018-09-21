from math import *

from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Material, LRotationf, NodePath
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import TextNode
from panda3d.core import LVector3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.interval.MetaInterval import Sequence, Parallel
from direct.interval.LerpInterval import LerpFunc
from direct.interval.FunctionInterval import Func, Wait
from direct.task import Task
from panda3d.core import lookAt
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomVertexWriter
from panda3d.core import Texture, GeomNode
from panda3d.core import PerspectiveLens
from direct.interval.LerpInterval import LerpHprInterval
from direct.interval.IntervalGlobal import *
#from tkinter import *
import ctypes
import os
import random
#import win32api, pyHook, pythoncom
import sys
from direct.interval.LerpInterval import LerpPosInterval
from panda3d.core import Point3, LVector3
from pandac.PandaModules import *

class PenaltyKick(ShowBase):
	#angleD
	global co
	co = 0
	def __init__(self):
		#try:
		#if(co == 0):
		ShowBase.__init__(self)
		#	co += 1
		self.disableMouse()
		base.setBackgroundColor(0, 0, 1)
		#camera.setPosHpr(45, -45, 45, 45, -45, 45)		
		self.accept("escape", sys.exit)  # Escape quits	

        # Disable default mouse-based camera control.  This is a method on the
        # ShowBase class from which we inherit.
		#self.disableMouse()
		camera.setPosHpr(-10, -50, 10, -10, -7, 0)
		#camera.setPosHpr(-50, 40, 0, 270, 0, 0)
		#base.setBackgroundColor(0,1,0)
		#base
		net = loader.loadModel("models/drawnNet")
		net.setColor(1, 1, 0)
		net.setScale(2.5, 2.5, 1.5)
		net.setPosHpr(0, 53, -2, 0, -10, 0)
		net.reparentTo(render)


		global targetY
		targetY = 40

		postR = loader.loadModel("models/box")
		postR.setColor(0.75, 0, 0.25)
		postR.setScale(0.03, 0.03, 1)
		LidR = postR.find('**/lid')
		PandaR = postR.find('**/turningthing')
		HingeNodeR = postR.find('**/box').attachNewNode('nHingeNode')
		HingeNodeR.setPos(.8659, 6.5, 5.4)
		LidR.wrtReparentTo(HingeNodeR)
		HingeNodeR.setHpr(0, 90, 0)
		lidCloseR = Parallel(
		    LerpHprInterval(HingeNodeR, 2.0, (0, 90, 0), blendType='easeInOut'))
		postR.setPosHpr(18, 55.5, -2, 0, 0, 0)
		postR.reparentTo(render)

		postGR = loader.loadModel("models/box")
		postGR.setColor(0.75, 0, 0.25)
		postGR.setScale(0.03, 0.03, 1)
		lidGR = postGR.find('**/lid')
		PandaGR = postGR.find('**/turningthing')
		HingeNodeGR = postGR.find('**/box').attachNewNode('nHingeNode')
		HingeNodeGR.setPos(.8659, 6.5, 5.4)
		#lidGR.wrtReparentTo(HingeNodeR)
		HingeNodeGR.setHpr(0, 90, 0)
		lidCloseGR = Parallel(
		    LerpHprInterval(HingeNodeGR, 2.0, (0, 90, 0), blendType='easeInOut'))
		postGR.setPosHpr(18, 58.5, -4, 90, 0, 90)
		postGR.reparentTo(render)
		

		postL = loader.loadModel("models/box")
		postL.setColor(0.75, 0, 0.25)
		postL.setScale(0.03, 0.03, 2)
		LidL = postL.find('**/lid')
		PandaL = postL.find('**/turningthing')
		HingeNodeL = postL.find('**/box').attachNewNode('nHingeNode')
		HingeNodeL.setPos(.8659, 6.5, 5.4)
		LidL.wrtReparentTo(HingeNodeL)
		HingeNodeL.setHpr(0, 90, 0)
		lidCloseL = Parallel(
		    LerpHprInterval(HingeNodeL, 2.0, (90, 0, 0), blendType='easeInOut'))
		postL.setPosHpr(-18, 55.5, -1, 0, 0, 0)
		postL.reparentTo(render)

		postGL = loader.loadModel("models/box")
		postGL.setColor(0.75, 0, 0.25)
		postGL.setScale(0.03, 0.03, 1)
		lidGL = postGL.find('**/lid')
		PandaGL = postGL.find('**/turningthing')
		HingeNodeGL = postGL.find('**/box').attachNewNode('nHingeNode')
		HingeNodeGL.setPos(.8659, 6.5, 5.4)
		#lidGR.wrtReparentTo(HingeNodeR)
		HingeNodeGL.setHpr(0, 90, 0)
		lidCloseGL = Parallel(
		    LerpHprInterval(HingeNodeGL, 2.0, (0, 90, 0), blendType='easeInOut'))
		postGL.setPosHpr(-18, 58.5, -4.5, 90, 0, 90)
		postGL.reparentTo(render)
		#camera.setPosHpr(20, 45, 0, 90, 0, 0)

		postT = loader.loadModel("models/box")
		postT.setColor(0.75, 0, 0.25)
		postT.setScale(1.70, 0.03, 0.03)
		LidT = postL.find('**/lid')
		PandaT = postT.find('**/turningthing')
		HingeNodeT = postT.find('**/box').attachNewNode('nHingeNode')
		HingeNodeT.setPos(.8659, 6.5, 5.4)
		LidT.wrtReparentTo(HingeNodeT)
		HingeNodeT.setHpr(0, 90, 0)
		lidCloseT = Parallel(
		    LerpHprInterval(HingeNodeT, 2.0, (0, 90, 0), blendType='easeInOut'))
		postT.setPosHpr(0, 55.5, 9.8, 0, 0, 0)
		postT.reparentTo(render)

		global ball
		ballRoot = render.attachNewNode("ballRoot")
		ball = loader.loadModel("models/ball")
		ball.reparentTo(ballRoot)
		#ball.setColor(0.5, 0, 1)
		ball.setScale(6, 6, 6)
		ball.setPosHpr(0, -12, -3, 0, -20, 0)
		#self.kick.setPos(0, 40, 0)
		ballTex = loader.loadTexture("pictures/ball.jpg")
		ball.setTexture(ballTex)
		ball.reparentTo(render)
		ballSphere = ball.find("**/ball")
		ballSphere.node().setFromCollideMask(BitMask32.bit(0))
		ballSphere.node().setIntoCollideMask(BitMask32.allOff())

		ambientLight = AmbientLight("ambientLight")
		ambientLight.setColor((.55, .55, .55, 1))
		directionalLight = DirectionalLight("directionalLight")
		directionalLight.setDirection(LVector3(0, 0, -1))
		directionalLight.setColor((0.375, 0.375, 0.375, 1))
		directionalLight.setSpecularColor((1, 1, 1, 1))

		ballRoot.setLight(render.attachNewNode(ambientLight))
		ballRoot.setLight(render.attachNewNode(directionalLight))
		m = Material()
		m.setSpecular((1, 1, 1, 1))
		m.setShininess(96)
		ball.setMaterial(m, 1)

		cs = CollisionSphere(0, 0, 0, 0.41)
		cNodePath = ball.attachNewNode(CollisionNode('cnode'))
		cNodePath.node().addSolid(cs)
		#cNodePath.show()
		#0, 53, -2
		cW = CollisionPolygon(Point3(-1,40,-4), Point3(-1,40,8), Point3(1,40,8), Point3(1,40,-4))
		cwNodePath = net.attachNewNode(CollisionNode('cwnode'))
		cwNodePath.node().addSolid(cW)
		#cwNodePath.show()

		#queue = CollisionHandlerQueue()
		#traverser.addCollider(cs, queue)
		#traverser.traverse(render)

		ground = loader.loadModel("models/square")
		ground.setPosHpr(0, 35, -5, 0, 0, 0)
		ground.setScale(120, 120, 120)
		#ground.setColor(0.2, 1, 0)
		grass = loader.loadTexture("pictures/grass_1.jpg")
		ground.setTexture(grass)
		ground.reparentTo(render)

		wall = loader.loadModel("models/square")
		wall.setPosHpr(5, 100, 18, 0, 90, 0)
		wall.setScale(90, 50, 75)
		#camera.setPos(0, -150, 0)
		#wall.setColor(0.5, 0.5, 0.5)
		crowd = loader.loadTexture("pictures/crowd.png")
		wall.setTexture(crowd)
		wall.reparentTo(render)


		rightWall = loader.loadModel("models/square")
		rightWall.setPosHpr(48, 45, 0, -90, 90, 0)
		rightWall.setScale(100, 100, 100)
		rightWall.setColor(0.75, 0.75, 0.75)
		rightWall.reparentTo(render)

		global angle
		angle = loader.loadModel("models/box")
		angle.setColor(0.25, 0.25, 0.25)
		angle.setScale(1.0, 0.25, 0.03)
		LidA = angle.find('**/lid')
		PandaA = angle.find('**/turningthing')
		HingeNodeA = angle.find('**/box').attachNewNode('nHingeNode')
		HingeNodeA.setPos(.8659, 6.5, 5.4)
		LidA.wrtReparentTo(HingeNodeA)
		HingeNodeA.setHpr(0, 90, 0)
		lidCloseA = Parallel(
		    LerpHprInterval(HingeNodeA, 2.0, (0, 90, 0), blendType='easeInOut'))
		angle.setPosHpr(0, 10.5, -3, 0, 90, 0)
		#bar = loader.loadTexture("pictures/bar.png")
		#angle.setTexture(bar)
		angle.reparentTo(render)

		global angleD
		angleD = loader.loadModel("models/box")
		angleD.setColor(0, 0, 1)
		angleD.setScale(0.1, 0.25, 0.03)
		LidD = angleD.find('**/lid')
		PandaD = angleD.find('**/turningthing')
		HingeNodeD = angleD.find('**/box').attachNewNode('nHingeNode')
		HingeNodeD.setPos(.8659, 6.5, 5.4)
		LidD.wrtReparentTo(HingeNodeD)
		HingeNodeD.setHpr(0, 90, 0)
		lidCloseD = Parallel(
		    LerpHprInterval(HingeNodeD, 2.0, (0, 90, 0), blendType='easeInOut'))
		angleD.setPosHpr(0, 10.4, -3, 0, 90, 0)
		angleD.reparentTo(render)

		global power
		power = loader.loadModel("models/box")
		power.setColor(0.25, 0.25, 0.25)
		power.setScale(0.12, 2.2, 0.03)
		LidP = power.find('**/lid')
		PandaP = power.find('**/turningthing')
		HingeNodeP = power.find('**/box').attachNewNode('nHingeNode')
		HingeNodeP.setPos(.8659, 6.5, 5.4)
		LidP.wrtReparentTo(HingeNodeP)
		HingeNodeP.setHpr(0, 90, 0)
		lidCloseP = Parallel(
		    LerpHprInterval(HingeNodeP, 2.0, (0, 90, 0), blendType='easeInOut'))
		power.setPosHpr(-18, 10.5, -3, 0, 90, 0)

		global powerD
		powerD = loader.loadModel("models/box")
		powerD.setColor(1, 0, 0)
		powerD.setScale(0.12, 0.05, 0.03)
		LidD = power.find('**/lid')
		PandaD = power.find('**/turningthing')
		HingeNodeD = power.find('**/box').attachNewNode('nHingeNode')
		HingeNodeD.setPos(.8659, 6.5, 5.4)
		LidD.wrtReparentTo(HingeNodeD)
		HingeNodeD.setHpr(0, 90, 0)
		lidCloseD = Parallel(
		    LerpHprInterval(HingeNodeD, 2.0, (0, 90, 0), blendType='easeInOut'))
		powerD.setPosHpr(-18, 10, -4.5, 0, 50, 0)

		global bishop
		bishop = loader.loadModel("models/bishop")
		bs = loader.loadTexture("pictures/bishop.png")
		bishop.setTexture(bs)
		bishop.setScale(10, 10, 10)
		#bishop.setColor(0, 0.4, 1)
		bishop.setPosHpr(0, 42, -5, 90, 0, 0)
		bishop.reparentTo(render)

		global bArmL
		bArmL = loader.loadModel("models/bishop")
		bArmL.setScale(2, 2, 4)
		bishop.setTexture(bs)
		#bArmL.setColor(0, 0.4, 1)
		bArmL.setPos(-1, 55, 6)
		#bArmL.reparentTo(render)

		global bArmR
		bArmR = loader.loadModel("models/bishop")
		bArmR.setScale(2, 2, 4)
		bishop.setTexture(bs)
		#bArmR.setColor(0, 0.4, 1)
		bArmR.setPos(1, 55, 6)
		#bArmR.reparentTo(render)

		global start
		start = loader.loadModel("models/square")
		start.setPosHpr(5, -25, 18, 0, 90, 0)
		start.setScale(90, 50, 75)
		#camera.setPos(0, -150, 0)
		start.setColor(0.5, 0.5, 0.5)
		#crowd = loader.loadTexture("pictures/crowd.png")
		#start.setTexture(crowd)
		start.reparentTo(render)

		title = TextNode('title')
		title.setText("Welcome to Penalty Kick!")
		global textNodePath
		textNodePath = aspect2d.attachNewNode(title)
		textNodePath.setScale(0.25)
		title.setWordwrap(8)
		title.setCardColor(0, 0, 0, 0)
		title.setCardAsMargin(0, 0, 0, 0)
		title.setCardDecal(True)
		textNodePath.setPos(-0.75, 0, 0.5)
		self.instructions = \
        	OnscreenText(text="Press any key to begin",
                     parent=base.a2dBottomRight, align=TextNode.ARight,
                     pos=(-1, +0.08), fg=(1, 1, 1, 1), scale=.06,
                     shadow=(0, 0, 0, 0.5))
        #self.accept('ball-into-net', ballCollideHandler)
		base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
		self.accept('keystroke', self.next)
		#textNodePath.reparentTo(render)
	def ballCollideHandler(self, entry):
		ballLerp = Sequence(Parallel(LerpPosInterval(ball, 0.75, Point3(ball.getX(), 0, ball.getZ()), Point3(ball.getX(),ball.getY(), ball.getZ()),	 None, 'noBlend', 0, 1, 'bLerp')))
		if (counter < 5):
			self.score = \
				score.clear()
    			OnscreenText(text=counter + "/5",
           			parent=base.a2dTopRight, align=TextNode.ARight,
            		fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.1, shadow=(0, 0, 0, 0.5))
    		counter += 1
			#camera.setPosHpr(-15, -85, 0, -20, -10, 0)
	def nothing(self, x):
		pass
		counter = 0
	def blank_(self):
		pass
	def next(self, x):
		base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
		self.accept('keystroke', self.nothing)
		self.accept('enter', self.blank_)
		start.setPos(0, -100, 0)
		#self.instructions.clearText()
		textNodePath.setPos(-100,-100, 0)
		self.instructions.clearText()
		self.title = \
    		OnscreenText(text="Penalty Kick",
                     parent=base.a2dBottomRight, align=TextNode.ARight,
                     fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=0.15,
                    shadow=(0, 0, 0, 0.5))
		self.instructions = \
			OnscreenText(text="Choose your angle with the space bar",
                     parent=base.a2dTopLeft, align=TextNode.ALeft,
                     pos=(0.05, -0.08), fg=(1, 1, 1, 1), scale=.1,
                     shadow=(0, 0, 0, 0.5))

		self.angleText = \
        	OnscreenText(text="Angle",
                     parent=base.a2dBottomRight, align=TextNode.ARight,
                     pos=(-1.3, +.82), fg=(1, 1, 1, 1), scale=0.15,
                     shadow=(0, 0, 0, 0.5))
		#self.score = \
		#	OnscreenText(text="0/5",
        #   			parent=base.a2dTopRight, align=TextNode.ARight,
        #    		fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.08, shadow=(0, 0, 0, 0.5))
		global bLerp
		bLerp = Sequence(Parallel(LerpPosInterval(bishop, 0.6, Point3(-15, 57, -5), Point3(15, 57, -5), None, 'easeInOut', 0, 1, 'bLerp')), 
			LerpPosInterval(bishop, 0.5, Point3(15, 57, -5), Point3(-15, 57, -5), None, 'easeInOut', 0, 1, 'bLerp'))
		#bishopInterval = bishop.posInterval
		bLerp.loop() 

		#ball sims until location reached, then sims a drop down. no collision check needed



		global angleDLerp
		angleDLerp = Sequence(Parallel(LerpPosInterval(angleD, 0.6, Point3(-9.5, 10.4, -3), Point3(9.5, 10.4, -3), None, 'easeInOut', 0, 1, 'bLerp')), 
			LerpPosInterval(angleD, 0.8, Point3(10, 10.4, -3), Point3(-10, 10.4, -3), None, 'easeInOut', 0, 1, 'bLerp'))
		angleDLerp.loop()

		global powerDLerp
		powerDLerp = Sequence(Parallel(LerpPosInterval(powerD, 0.3, Point3(-18, 10, -4.5), Point3(-18, 10, 11), None, 'easeInOut', 0, 1, 'bLerp')), 
			LerpPosInterval(powerD, 0.5, Point3(-18, 10, 11), Point3(-18, 10, -4.5), None, 'easeInOut', 0, 1, 'bLerp'))
		x = 1
		self.accept('space', self.angleDis)
		
        #place
		#print("hi")
		#inp = input("")       # Get the input
		#while inp != "":        # Loop until it is a blank line
		#	print("??")
		#	inp = input() 
		#	angleD.setFluidPos(-10, 10.4, -3)
		#	angleD.setFuildPos(10, 10.4, -3)
		#pause = input('')

		#click event, fire ball
	global oneToFive
	oneToFive = 0
	global oneOrTwo
	oneOrTwo = 0
	def angleDis(self):
		self.angleText.clearText()
		ballPos = ball.getPos(render)
		angleDPos = angleD.getPos(render)
		direction = ballPos - angleDPos
		#fn = ForceNode('push')
		#p = LinearVectorForce((direction + ballPos)  * 2)
		#fn.addForce(p)
		#ball.addLinearForce(pull)
		#self.setVelocity(ball, LVector3(ballPos-angleDPos))
		#print(ballPos, angleDPos)
		ballX = ball.getX(render)
		#print(ballPos, ballX)
		#ball.setFluidPos(ballPos + direction * 1)
		ballX = ball.getX(render)
		ballY = ball.getY(render)
		ballZ = ball.getZ(render)
		angleDX = angleD.getX(render)
		angleDY = angleD.getY(render)
		angleDZ = angleD.getZ(render)
		angleDD = (angleDX + 9.5)/(19)
		#print(angleDX)
		if(angleDD <= 0.2):
			oneToFive = 1
		elif(angleDD <= 0.4):
			oneToFive = 2
		elif(angleDD <= 0.6):
			oneToFive =3
		elif(angleDD <= 0.8):
			oneToFive = 4
		else:	
			oneToFive = 5
		#print(oneToFive)
		#global ballLerp
		#ballLerp = Sequence(Parallel(LerpPosInterval(ball, 1, Point3(ball.getX(), 70, ball.getZ() + 10), ball.getPos(), None, 'easeInOut', 0, 1, 'bLerp')))
		#ballLerp.start()
		#ballLerp.finish()
		#print(angleDPos, angleDX, angleDY, angleDZ)
		#print(angleD.getPos(render), direction, ballPos, ballX, ballY, ballZ)
		#print
		self.instructions.clearText()
		self.instructions = \
        	OnscreenText(text="Choose the power with the space bar",
                     parent=base.a2dTopLeft, align=TextNode.ALeft,
                     pos=(0.05, -0.08), fg=(1, 1, 1, 1), scale=.06,
                     shadow=(0, 0, 0, 0.5))
		self.powerText = \
        	OnscreenText(text="Power",
                     parent=base.a2dBottomRight, align=TextNode.ARight,
                     pos=(-2.2, 1.6), fg=(1, 1, 1, 1), scale=.15,
                     shadow=(0, 0, 0, 0.5))
		power.reparentTo(render)


		#angle.setPos(0,0, -100)
		angleDLerp.finish()
		angleD.setPos(angleDX, angleDY, angleDZ)
		powerD.reparentTo(render)
		powerDLerp.loop()
		self.accept('space', self.powerDis,[oneToFive])

	def powerDis(self, oTF):
		self.powerText.clearText()
		powerDX = powerD.getX(render)
		powerDY = powerD.getY(render)
		powerDZ = powerD.getZ(render)
		powerDLerp.finish()
		powerD.setPos(powerDX, powerDY, powerDZ)
		#print(11-(15.5/2), powerDZ)
		if(powerDZ > 11-(15.5/2)):
			oneOrTwo = 2
		else:
			oneOrTwo = 1


		#go in direction that angle bar says, in relative speed
		ballKZ = 2
		#print(oTF)
		ballKX = oTF * (0.2*19)
		if(oneOrTwo == 2):
			#print("hi")
			ballKZ += 8
		fifth = (1/3) * 19
#		print(-9.5 + (oTF * fifth))
		tmp1 = -9.5 - fifth
		tmp2 = 9.5 + fifth
		#print(-9.5 + (oTF * (0.2*(tmp2-tmp1))), tmp2-tmp1, 0.2*(tmp2-tmp1), oTF*(0.2*(tmp2-tmp1)))
		#print(1/3)
		#ball.setX(ball.getX() + 5)
		goalieX = bishop.getX()
		goalieY = bishop.getY()
		goalieZ = bishop.getZ()
		if(abs(goalieX - ballKX) < 0.5):
			self.ballDown()
		bLerp.finish()
		bishop.setPos(goalieX, goalieY, goalieZ)
		#pt = #Point3(2*(-9.5 + (oTF * (0.2*(tmp2-tmp1)))
		#	pt.setY(-1)
		tmp = 1.7*(-9.5 + (oTF * (0.2*(tmp2-tmp1))))
		num = 63
		num2 = 65
		if(oneOrTwo == 2):
			num = 55
		rand = random.randrange(1,2,1)
		
		#print(rand)
		global blocked
		blocked = False
		if(abs(goalieX - tmp) < 5):
			if((rand == oneOrTwo) or abs(goalieX-tmp)-3):
				if(oneOrTwo == 2):
					yyy = tmp-1.5*0.6
					#print(yyy, tmp)
					bArmL.setX(yyy)
					if(oneToFive == 1):
						bArmR.setX(yyy - 2)
					elif(oneToFive == 2):
						bArmR.setX(yyy - 1)
					elif(oneToFive == 3):
						bArmR.setX(yyy + 0)
					elif(oneToFive == 4):
						bArmR.setX(yyy + 1)
					else:
						bArmR.setX(yyy + 2)

					bArmL.reparentTo(render)
					bArmR.reparentTo(render)
				bishop.setX(tmp)	
				num = 55
				num2 = 55
				blocked = True
			elif(oneOrTwo == 1):
				blocked = True
		#else:
		#	print(goalieX, tmp)
		#print(goalieX, tmp, abs(goalieX-tmp))
		ballLerp = Sequence(Parallel(LerpPosInterval(ball, 0.5, Point3(tmp, num, ballKZ), ball.getPos(), None, 'easeInOut', 0, 1, 'bLerp')),
			LerpPosInterval(ball, 0.75, Point3(tmp,num2, -3), Point3(tmp, num, ballKZ), None, 'easeInOut', 0, 1, 'bLerp'), Func(self.blockedC))
			


		angle.setPos(0, 0, -100)
		angleD.setPos(0, 0, -100)
		power.setPos(0, 0, -111)
		powerD.setPos(0, 0, -111)
		self.instructions.clearText()
		self.title.clearText()
		ballLerp.start()
		#self.__init__()
			#power is according to length of awwor
			#goalie moves in random direction, speed on click
			#if ball/goalie collide, no points for that round.
			#out of five points. Whoever has more at end wins.
	kicked = False;
	#def mousemove(event):
	#	print("1")
	#def mousedown(event):
	#	if not kicked:
	#		print("")
	def bC(self):
		#print("l")
		pass
	def blockedC(self):
		if(blocked):
			self.title.clearText()
			self.instructions.clearText()

			start.setPosHpr(5, -25, 18, 0, 90, 0)
			start.setColor(1, 0, 0)

			title1 = TextNode('game-over')
			title1.setText("You Failed. Try Again?")
			global tNP1
			tNP1 = aspect2d.attachNewNode(title1)
			tNP1.setScale(0.25)
			title1.setWordwrap(5)
			title1.setCardColor(0, 0, 0, 0)
			title1.setCardAsMargin(0, 0, 0, 0)
			title1.setCardDecal(True)
			tNP1.setPos(-0.65, 0, 0.5)

			self.instructions = \
        	OnscreenText(text="Press any key to restart",
                     parent=base.a2dBottomRight, align=TextNode.ARight,
                     pos=(-1, +0.08), fg=(1, 1, 1, 1), scale=.08,
                     shadow=(0, 0, 0, 0.5))
			#base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
			#self.accept('keystroke', self.myFunc)

			#yes = TextNode('yes')
			#yes.setText("Yes")
			#global tNPy
			#tNPy = aspect2d.attachNewNode(yes)
			#tNPy.setScale(0.25)
			#yes.setWordwrap(10)
			#yes.setCardColor(0, 0, 0, 0)
			#yes.setCardAsMargin(0, 0, 0, 0)
			#yes.setCardDecal(True)
			#yes.setCardBorder(2,2)
			#tPNy.setPos(-1.0, 1.0, 1)

			#self.yes_ = \
        	#OnscreenText(text="Yes",
            #         parent=base.a2dBottomLeft, align=TextNode.ALeft,
            #         pos=(0.05, 0.05), fg=(1, 1, 1, 1), scale=.35,
            #         shadow=(0, 0, 0, 0.5))
			#self.enableMouse()
			#camera.setPosHpr(-10, -50, 10, -10, -7, 0)
			#self.accept('mouse1', self.yesno_)
			base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
			self.accept('keystroke', self.myFunc)
		else:
			self.title.clearText()
			self.instructions.clearText()
			start.setPosHpr(5, -25, 18, 0, 90, 0)
			start.setColor(0, 1, 0)

			title2 = TextNode('congrats')
			title2.setText("Congratulations! Do it again?")
			global tNP2
			tNP2 = aspect2d.attachNewNode(title2)
			tNP2.setScale(0.25)
			title2.setWordwrap(8)
			title2.setCardColor(0, 0, 0, 0)
			title2.setCardAsMargin(0, 0, 0, 0)
			title2.setCardDecal(True)
			tNP2.setPos(-1, 0, 0.5)
			
			self.instructions = \
        	OnscreenText(text="Press any key to restart",
                     parent=base.a2dBottomRight, align=TextNode.ARight,
                     pos=(-1, +0.08), fg=(1, 1, 1, 1), scale=.08,
                     shadow=(0, 0, 0, 0.5))

			base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
			self.accept('keystroke', self.myFunc)	
			#self.no_ = \
        	#OnscreenText(text="No",
            #         parent=base.a2dBottomRight, align=TextNode.ALeft,
            #         pos=(0, 0.05), fg=(1, 1, 1, 1), scale=.35,
            #         shadow=(0, 0, 0, 0.5))
			#self.enableMouse()
			#camera.setPosHpr(-10, -50, 10, -10, -7, 0)
			#self.accept('mouse1', self.yesno_)
	def ballDown(self):
		pass
	def myFunc(self, x):
		os.execl(sys.executable, sys.executable, *sys.argv)
		#os.startfile(sys.argv[0])
		#os.execl(sys.executable,'"%s"'%sys.argv[0])
		#ShowBase.restart(False, None)
		#ShowBase.destroy()
		#ShowBase.__init__(self)
	def yesno_(self):
		pass
	def onclick(event):
		#ctypes.windll.user32.MessageBoxW(0, "hi", "title", 1)
		print("clicked", event.x, event.y)
	#def startKick(self):
	#	print("hi")
demo = PenaltyKick()
demo.run()