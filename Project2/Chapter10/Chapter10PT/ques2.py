class calci:
    def __init__(self,n):
        self.n=n
    def sq(self):
        print(f"Square is- {self.n * self.n}")
    def cub(self):
        print(f"Square is- {self.n * self.n * self.n}")
    def root(self):
        print(f"Square is- {self.n ** 1/2}")

a=calci(4)
a.sq()
a.cub()
a.root()