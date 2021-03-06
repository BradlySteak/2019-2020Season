import wpilib
from wpilib import controller as controller
import math
import rev
from enum import Enum
import logging
import sys
import time
import threading
from networktables import NetworkTables

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server='10.xx.xx.2')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
sd = NetworkTables.getTable('SmartDashboard')

class TurretAuto:
	def __init__(self):
		self.yaw = sd.getNumber('yaw',0)
	
		self.turretMotorID = 11
		self.spinMotorID = 12
		
		
		self.turretMotor = rev.CANSparkMax(self.turretMotorID,rev.MotorType.kBrushless)
		self.spinMotor = rev.CANSparkMax(self.spinMotorID,rev.MotorType.kBrushless)
		self.hoodServo = ??
		
		
		self.kP = 0.0
		self.kI = 0.0
		self.kD = 0.0
		
		self.turretTurnController = wpilib.controller.PIDController(self.kP,self.kI,self.kD)
		self.turretTurnController.setSetpoint(0)
		self.turretTurnController.setBounds(0,360)
		self.turretTurnController.setTolerance(0.1)
		
		self.sP = 0.0
		self.sI = 0.0
		self.sP = 0.0
		self.cruisingVelocity = 5500 #in rpm
		self.minVelocity = 1000
		
		self.spinController = rev._impl.CANPIDController(self.spinMotor)
		self.spinController.setP(self.sP,0)
		self.spinController.setI(self.sI,0)
		self.spinController.setD(self.sD,0)
		self.spinController.setSmartMotionMaxVelocity(self.cruisingVelocity,0)
		self.spinController.setSmartMotionMinOutputVelocity(self.minVelocity, 0)

	def velocityControl(self,desiredVelocity):
		
	def angularControl(self):
		
	def turretAlign(self):
		bop = self.yaw
		turretOutput = self.turretTurnController.calculate(bop)
		self.turretMotor.set(turretOutput)
	
	def turretShoot(self):
		#the turret must first align with the plane of the center of the target
		self.turretAlign()
		
		
		vDesired= #(insert Liam math here
		
		if (vDesired > self.maxVelocity) or (vDesired < self.minVelocity):
			#Angular control
			angularControl()
			
			
		else:
			#velocity control
			self.velocityControl(vDesired)
			