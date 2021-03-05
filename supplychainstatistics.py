import matplotlib.pyplot as plt

class SupplyChainStatistics:
    
    def __init__(self):
        
        #Cost statistics
        self.retailerallcosts = []
        self.wholesalerallcosts = []
        self.distributorallcosts = []
        self.factoryallcosts = []
        
        #Order statistics
        self.retailerallorders = []
        self.wholesalerallorders= []
        self.distributorallorders= []
        self.factoryallorders = []
        
        #Inventory statistics
        self.retailerallinventory= []
        self.wholesalerallinventory = []
        self.distributorallinventory = []
        self.factoryallinventory = []
        
        return
    
    def retailerorderRecord(self, retailerordersthisweek):
        self.retailerallorders.append(retailerordersthisweek)
        return
    
    def wholesalerorderRecord(self, wholesalerorderthisweek):
        self.wholesalerallorders.append(wholesalerorderthisweek)
        return
    
    def distributororderRecord(self, distributorordersthisweek):
        self.distributorallorders.append(distributorordersthisweek)
        return
    
    def factoryorderRecord(self, factoryordersthisweek):
        self.factoryallorders.append(factoryordersthisweek)
        return
    
    
    
    
    def retailercostRecord(self, retailercoststhisweek):
        self.retailerallcosts.append(retailercoststhisweek)
        return
    
    def wholesalercostRecord(self, wholesalercoststhisweek):
        self.wholesalerallcosts.append(wholesalercoststhisweek)
        return
    
    def distributorcostRecord(self, distributorcoststhisweek):
        self.distributorallcosts.append(distributorcoststhisweek)
        return
    
    def factorycostRecord(self, factorycoststhisweek):
        self.factoryallcosts.append(factorycoststhisweek)
        return
    
    
    
    def retailerinventoryRecord(self, retailerinventorythisweek):
        self.retailerallinventory.append(retailerinventorythisweek)
        return
    
    def wholesalerinventoryRecord(self, wholesalerinventorythisweek):
        self.wholesalerallinventory.append(wholesalerinventorythisweek)
        return
    
    def distributorinventoryRecord(self, distributorinventorythisweek):
        self.distributorallinventory.append(distributorinventorythisweek)
        return
    
    def factoryinventoryRecord(self, factoryinventorythisweek):
        self.factoryallinventory.append(factoryinventorythisweek)
        return
    
    def PlotCosts(self):
        plt.title("Cost Incurred Over Time")
        plt.plot(self.retailerallcosts, "r", label = "Retailer")
        plt.plot(self.wholesalerallcosts, "w", label = "Wholesaler")
        plt.plot(self.distributorallcosts, "d", label = "Distributor")
        plt.plot(self.factoryallcosts, "f", label="Factory")
        legend = plt.legend(loc='upper left', shadow=True)
        print (legend)
        plt.ylabel('Cost ($)')
        plt.xlabel("Weeks")
        plt.show()
        
        return
    
    def PlotOrders(self):
        plt.title("Orders Placed Over Time")
        plt.plot(self.retailerallorders, "r", label = "Retailer")
        plt.plot(self.wholesalerallorders, "w", label = "Wholesaler")
        plt.plot(self.distributorallorders, "d", label = "Distributor")
        plt.plot(self.factoryallorders, "f", label="Factory")
        legend = plt.legend(loc='upper left', shadow=True)
        print(legend)
        plt.ylabel('Orders')
        plt.xlabel("Weeks")
        plt.show()
        
        return
    
    def PlotInventory(self):
        plt.title("Inventory Over Time")
        plt.plot(self.retailerallinventory, "r", label = "Retailer")
        plt.plot(self.wholesalerallinventory, "w", label = "Wholesaler")
        plt.plot(self.distributorallinventory, "d", label = "Distributor")
        plt.plot(self.factoryallinventory, "f", label="Factory")
        legend = plt.legend(loc='upper left', shadow=True)
        print(legend)
        plt.ylabel('Inventory')
        plt.xlabel("Weeks")
        plt.show()
        
        return