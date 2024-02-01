class 반():
    a = 1000
    def 이름정하기(self,name):
        self.name = name
    def 이름호출(self):
        print(self.name)
    def 이름특이하게호출(self):
        print(self.name+ "_____")

수민 = 반()
수민.a += 100
print(수민.a)


수만 = 반()
print(수만.a)