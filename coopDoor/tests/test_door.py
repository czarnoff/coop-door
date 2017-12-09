import unittest

class MyTest(unittest.TestCase):
   def testDoor(self):
      import Door
      self.assertTrue(True)
   def testDoorUp(self):

      import Door
      mDoor = Door.Door()

#Door is only up if the top switch is high and bottom switch is low.
#Otherwise it is considered not up
      mDoor.switchTop=True

      mDoor.switchBot=False
      self.assertTrue(mDoor.doorUp())

      mDoor.switchBot=True
      self.assertFalse(mDoor.doorUp())

      mDoor.switchTop=False

      mDoor.switchBot=False
      self.assertFalse(mDoor.doorUp())

      mDoor.switchBot=True
      self.assertFalse(mDoor.doorUp())


   def testDoorDown(self):

      import Door
      mDoor = Door.Door()

#Door is only down if the bottom switch is high and top switch is low.
#Otherwise it is considered down
      mDoor.switchBot=True

      mDoor.switchTop=False
      self.assertTrue(mDoor.doorDown())

      mDoor.switchTop=True
      self.assertFalse(mDoor.doorDown())

      mDoor.switchBot=False

      mDoor.switchTop=False
      self.assertFalse(mDoor.doorDown())

      mDoor.switchTop=True
      self.assertFalse(mDoor.doorDown())


