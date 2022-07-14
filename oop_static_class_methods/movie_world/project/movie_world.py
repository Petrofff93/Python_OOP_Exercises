
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []
    
    @staticmethod
    def dvd_capacity():
        return 15
    
    @staticmethod
    def customer_capacity():
        return 10
    
    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)
            return
    
    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)   
            return
    
    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        
        for dvd in current_customer.rented_dvds:
            if dvd.id == dvd_id:    
                return f'{current_customer.name} has already rented {dvd.name}'
        
        if current_dvd.is_rented:
            return 'DVD is already rented'
        
        if current_customer.age < current_dvd.age_restriction:
            return f'{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie'
        
        current_customer.rented_dvds.append(current_dvd)
        current_dvd.is_rented = True
        return f'{current_customer.name} has successfully rented {current_dvd.name}'
    
    def return_dvd(self, customer_id, dvd_id):
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        
        for dvd in current_customer.rented_dvds:
            if dvd.id == dvd_id:
                current_dvd.is_rented = False
                current_customer.rented_dvds.remove(dvd)
                return f'{current_customer.name} has successfully returned {current_dvd.name}'
        return f'{current_customer.name} does not have that DVD'
    
    def __repr__(self):
        result = ''
        
        for customer in self.customers:
            result += repr(customer) + '\n'
            
        for dvd in self.dvds:
            result += repr(dvd) + '\n'
        
        return result
    