class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        self.user = user
        
    def set_password(self, password):
        self.password = password
    
    def info(self, nolimit=True):
        if nolimit:
            print(f"Host: {self.host}\nUser: {self.user}\nPassword: {self.password}")
        else:
            print(f"Host: {self.host}")
        print('')
        
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.set_user(user)
        connection.set_password(password)
        
        return connection

    @staticmethod
    def soma(x, y):
        return x + y
    
c1 = Connection()
c1.info()

c1.set_user("Jorge")
c1.set_password('123')
c1.info()

c2 = Connection.create_with_auth('Maria', '745')
c2.info()
soma = c2.soma(2,3)

print(type(soma), soma)