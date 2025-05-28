class Cook:
    def prepare(self):
        print("Cook: Preparing a dish in a general way.")

class Chef(Cook):
    def prepare(self):
        Cook.prepare(self)
        print("Chef: Preparing a nice meal.")

class HomeCook(Cook):
    def prepare(self):
        print("HomeCook: Preparing a home-style dish.")

class PartTimeCook(Chef, HomeCook):
    def outputmethod(self):
        Chef.prepare(self)
        HomeCook.prepare(self)
    
    


parttime = PartTimeCook()
parttime.outputmethod()
