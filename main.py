class Wallet:
    def __init__(self, money = 0):
        self.money = money

    def credit(self, amount):
        self.money += amount

    def debit(self, amount):
        self.money -= amount
    
    def __str__(self) :
        return f"Your wallet balance is {self.money} KD"
 
print("\n \n######### Wallet Class #########\n")

wallet = Wallet(6) #The balance of wallet is 6 KD
wallet.credit(5) #The amount in the wallet is increased by 5 KD, so the balance is 11 KD.
wallet = Wallet(5).debit(3) #The balance should be 2 KD
wallet = Wallet()  # This should default money inside the wallet to 0 KD
print(wallet) #This should print "Your wallet balance is 0 KD"

print("\n \n######### Person Class #########\n")

class Person:
    def __init__(self, name, location, wallet):
        self.name = name
        self.location = location
        self.wallet = Wallet(wallet)

    def moveTo(self, point):
        self.location = point
        print(f"You've moved to the location: {self.location}")
    


person = Person("Moh", 5, 50)
print(f"You have in your wallet amount of {person.wallet} ") #This should print "Your wallet balance is 50 KD"

person.moveTo(10)


print("\n \n######### Vendor Class #########\n")

class Vendor(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
        self.range = 5
        self.price = 1

    def sellTo(self, customer, number_of_icecreams):
        
        #Moves to the customer's location
        self.location = customer.location

        #Transfers money from the customer's wallet to the vendor's wallet
        self.wallet.credit(self.price * number_of_icecreams) #Vendor wallet
        customer.wallet.debit(self.price * number_of_icecreams) #Customer wallet

        #Prints a nice message saying how many icecreams were sold
        print(f"The vendor {self.name} has sold {number_of_icecreams} number of ice-creams.")


print("\n \n######### Customer Class #########\n")


class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)


    def _is_in_range(self, vendor):
        # Checks if the customer is in range of vendor
        distance = abs(vendor.location - self.location)
        

        if distance < vendor.range :
            
            return True
        else:
            print(f"Sorry, the vendor is too far!")
            return False

    def _have_enough_money(self, vendor, number_of_icecreams):
        # Check if the customer has enough money
        if self.wallet.money >= vendor.price * number_of_icecreams :
            
            return True
        else:
            print(f"Sorry, you don't have enough money!")
            return False

    def request_icecream(self, vendor, number_of_icecreams):
        if self._have_enough_money(vendor, number_of_icecreams) and self._is_in_range(vendor):
            vendor.sellTo(self, number_of_icecreams)
        
aziz_vendor = Vendor("Aziz", 9, 10)

nearby_customer = Customer("Abdallah", 11, 10)
broke_customer = Customer("Ali", 10, 0)
far_customer = Customer("Hamad", 1000, 5)

# Sales transaction between customer "Abdullah" and vendor "Aziz" of 1 ice-cream for 1 KD.
nearby_customer.request_icecream(aziz_vendor, 1)
print(f"\nThe customer {nearby_customer.name} has remaining amouunt of {nearby_customer.wallet.money} in his wallet.")
print(f"The vendor {aziz_vendor.name} has amouunt of {aziz_vendor.wallet.money} in his wallet.\n")

broke_customer.request_icecream(aziz_vendor, 1)

far_customer.request_icecream(aziz_vendor, 1)