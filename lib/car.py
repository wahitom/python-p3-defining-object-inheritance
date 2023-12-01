from vehicle import Vehicle

# Defining the superclass
# Defining the subclass
# overwriting inherited Methods 

class Car(Vehicle):
   def go(self):
      return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

# Asking the Car attrribute what its parent ie superclass is 
print(Car.__bases__)

# The __bases__ attribute is availabe for all python classes
# even built ones like int 
# ie 

print(int.__bases__)

# this is because pythn classes share the same metaclass ie type class

print(int.__class__)
