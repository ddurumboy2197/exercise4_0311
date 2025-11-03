class Xodim:
    def __init__(self, ism, lavozim):
        self.ism = ism
        self.__lavozim = lavozim

    def lavozim_kor(self):
        return self.__lavozim

    def lavozim_ozgartir(self, yangi_lavozim):
        self.__lavozim = yangi_lavozim
        print(f"{self.ism}ning lavozimi yangilandi: {self.__lavozim}")


x1 = Xodim("Ali", "Dasturchi")
print(x1.lavozim_kor())

x1.lavozim_ozgartir("Loyiha rahbari")
print(x1.lavozim_kor())
