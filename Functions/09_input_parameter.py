#chai = "Ginger chai"

#def prepare_Chai(order):
    #print("Preparing ", order)


#prepare_Chai(chai)
#print(chai)

chai = [1,2,3]

def edit_Chai(cup): # here cup is parameter
    cup[1] = 42

edit_Chai(chai) # here cup is argument ( args)
print(chai)

def make_Chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_Chai("Darjeeling", "Yes", "Low") #Proportional
make_Chai(tea="Green", sugar="Medium", milk="No") # Keywords

def special_chai(*ingrediants, **extraas):
    print("Ingrediants", ingrediants)
    print("Extraas", extraas)

special_chai("Cinnamon", "Cardmom", sweetners="Honey", foam= "yes")

# def chai_order(order=[]):
    # order.append("Masala")
    # print(order)

def chai_order(order=None):
     if order is None:
         order = []
     print(order)

chai_order()
chai_order()