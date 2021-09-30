class India:
    def lang(self):
        print("Hindi")

class UK:
    def lang(self):
        print("English")

ind=India()
uk=UK()

for country in(ind,uk):
    country.lang()



