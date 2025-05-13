class Author:
    all = []
    def __init__(self,name):
        if isinstance(name,str):
           self.name = name
           Author.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.author== self]
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract(self,book,date,royalties):
            if not isinstance(book,Book):
                raise Exception("Must provide an instance otf a book")
            if not isinstance(date, str):
                raise Exception("Date must be a string")
            if not isinstance(royalties, int):
                raise Exception("Royalties must be an integer")
            return Contract(self,book,date,royalties)
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:

    all = []
    def __init__(self,title):
        if isinstance(title, str):
          self.title = title
          Book.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [contract.author for contract in self.contracts()]
 


class Contract:
    all = []

    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author 
    @author.setter
    def author(self,value):
        if not isinstance(value,Author):
            raise Exception("author must be an instance of Author")
        self._author = value
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self,value):
        if not isinstance(value,Book):
            raise Exception("book should be an instance of Book")
        self._book = value
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,value):
        if not isinstance(value, str):
            raise Exception("date should be a string")
        self._date = value
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self,value):
        if not isinstance(value,int):
            raise Exception("royalties should be integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls,date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        return [contract for contract in cls.all if contract.date == date]

                            

        