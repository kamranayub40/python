class car:
    def __init__(self,model,colour,name,owner,year_purshased):
        self.model=model
        self.colour=colour
        self.name=name
        self.owner=owner
        self.year_purshased=year_purshased
    
my=car('2018','Black','Landcrouser','Kamran Ayoub','2019')
print(my.model)
print(my.colour)
print(my.name)
print(my.owner)
print(my.year_purshased)
