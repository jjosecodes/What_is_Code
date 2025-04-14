



class fraction:
    #methods 
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
# cant directly print fraction class 
# since it gives the reference to the object
    def show(self):
        print(f"{self.num}/{self.den}")



my_fraction = fraction(3, 5)
print(my_fraction)
my_fraction.show()