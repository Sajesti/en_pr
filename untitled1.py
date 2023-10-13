class User:
    def __init__(self, username, password):
        self.user = username
        self.pas = password
        
class Buyer(User):
    def __init__(self, username, password, Address, nationalID ):
        super().__init__(username, password)
        self.adrs = Address
        self.Cnmber = nationalID
        
    def info(self):
        print(self.user, self.pas, self.adrs ,self.Cnmber )
        
pr = Buyer("saj","S@J127","saveh",6186978814)        
pr.info()


    