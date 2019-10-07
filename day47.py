class Library:
        def __init__(self, book, shelf):
            self.shelf = shelf
            self.book = book
               

                
Library1 = Library( 300, 45)

class Science_Section(Library):
        def __init__(self, name, book, shelf):
                super().__init__(book,shelf)
                self.name = name
                
        def printinfs(self):
            print(
                    "Number of book is :", self.book,
                      
                      "And we Have section for ",self.name)

s = Science_Section("Phisics book", 300,45)
s.printinfs()
s.book=20
s.self=4
s.printinfs()
