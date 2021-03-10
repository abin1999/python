class Parent:
   parentAttr = 100
   def __init__(self):
      print ('Calling parent constructor')

   def parentMethod(self):
      print ('Calling parent method')


class Child(Parent):
   def __init__(self):
      print ('Calling child constructor')

   def childMethod(self):
      print ('Calling child method')

c = Child()
c.childMethod()
c.parentMethod()
