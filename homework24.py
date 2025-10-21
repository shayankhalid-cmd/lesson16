class dog:
    species = "canine"
    species = "golden retriever"
    def __init__ (self,name,age):
        self.name = name
        self.age = age
Leo = dog("leo",5)
snowy = dog("snowy",23)
print("leo is a {}".format(Leo.species))
print("snowy is also a {}".format(snowy.species))
print("{} is {} years old".format(Leo.name,Leo.age))
print("{} is {} years old".format(snowy.name,snowy.age))