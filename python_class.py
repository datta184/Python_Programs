class car:  # class
    def __init__(self,cr_name,cr_variant,cr_price,cr_IngineTpye): # init method
        self.crname = cr_name
        self.crtype = cr_variant
        self.crmodel = cr_price
        self.crIngineTpye = cr_IngineTpye
        
        
    def tata(self): 
        print("Car name is -------------->",self.crname)
        print("Car variant are ---------->",self.crtype)
        print("Car model name is -------->",self.crmodel)
        print("Car Engine type is ------->",self.crIngineTpye)
        
        
    def mahindra(self):
        print("Car name is -------------->",self.crname)
        print("Car car type is ---------->",self.crtype)
        print("Car model name is -------->",self.crmodel)
        print("Car Engine type is ------->",self.crIngineTpye)
        
# creating the object and passing values to class        
tata_car=car( 'TataNexon',  ['XE','XM','XM S'] , {'XE':'7.39L','XM':'8.39L','XM S':'8.99L'} , 'Disel')
tata_car.tata()

print('\n')

mahi=car('Scorpio',['s3','s3 plus 9','s11'],{'s3':'13L','s3 plus 9':'15L','s11':'18.84L'},'disel')
mahi.mahindra()