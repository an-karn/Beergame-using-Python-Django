name= input ("Name:")
print(f"Hello,{name}")

u=str(input("User role:"))

class Player:
  def __init__(self, Role=0):
      self.Role =Role
      

@property
def Aboutrole(self):
      return self.Role

@Aboutrole.setter
def Aboutrole(self, c):
      self.Role = c

Role_obj = Player()
print(Role_obj.Role)

Role_obj.Role = (input("Choose Role: "))
print(Role_obj.Role)

class Player:
   def __init__(self, demand=0):
      self.demand =demand
      
print("Current demand is 0")

@property
def Aboutdemand(self):
      return self.demand

@Aboutdemand.setter
def Aboutdemand(self, a):
      self.demand = a

demand_obj = Player()
print(demand_obj.demand)

demand_obj.demand = (input("Set demand: "))
print(demand_obj.demand)

class Player:
  def __init__(self, cost=0):
      self.cost =cost
      

@property
def Aboutcost(self):
      return self.cost

@Aboutcost.setter
def Aboutcost(self, b):
      self.cost = b

cost_obj = Player()
print(cost_obj.cost)

cost_obj.cost = (input("Set cost: "))
print(cost_obj.cost)



class Player:
  def __init__(self, inventory=0):
      self.inventory =inventory
      

@property
def Aboutinventory(self):
      return self.inventory

@Aboutinventory.setter
def Aboutinventory(self, d):
      self.inventory = d

inventory_obj = Player()
print(inventory_obj.inventory)

inventory_obj.inventory = (input("Set inventory: "))
print(inventory_obj.inventory)

def increaseinventory():
  return inventory= inventory+numberofbeers
  

  increaseinventory()

def decreaseinventory():
  return inventory= inventory-numberofbeers

   decreaseinventory()
