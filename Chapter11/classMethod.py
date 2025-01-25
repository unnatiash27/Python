class emp:
    a=1
    @classmethod
    def show(cls):
        print(f"Value is {cls.a}")

obj=emp()
obj.a=7
obj.show()