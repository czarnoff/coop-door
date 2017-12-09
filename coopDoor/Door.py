class Door:
   switchTop=False
   switchBot=False
   def doorUp(self):
      return (self.switchTop and
            not self.switchBot)
   def doorDown(self):
      return (self.switchBot and
            not self.switchTop)

