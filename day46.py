class Library:
        def __init__(self,book,shelf):
                self.book = book
                self.shelf = shelf

class Science_Section(Library):
        def __init__(self, book, shelf,name):
                super().__init__(book,shelf)
                self.name = 'Physics book'

 sciene = Science_Section(20,4)
 print(sciene.book, sciene.shelf, sciene.name)

 #F= science_section(20,4, "Phisics book")
 #F.printinf()
 
                
                
