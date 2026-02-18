"""
Sudarat Pitakwongroj
683040504-2
P1
"""



from datetime import datetime

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self._id = item_id
        self.__checked_out = False
    
    def get_status(self):
        return "Checked out" if self.__checked_out else "Available"
    
    def check_out(self):
        # if checked_out is False (item still in lib)
        if not self.__checked_out:
            self.__checked_out = True
            return True
        # can't check out if item not in lib
        return False
    
    def return_item(self):
        if self.__checked_out: 
            self.__checked_out = False
            return True       
        return False  
    
    def display_info(self):
        return f"Title: {self.title} \nID: {self._id} \nCheckout status: {self.get_status()}"

# implement 3 classes here
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        self.pages_count = 0

    def set_pages_count(self, pages):
        self.pages_count = pages

    def display_info (self):
        return f"Title: {self.title} \nAuthor: {self.author} \npages: {self.pages_count} \ncheckout status: {self.get_status()}" 
        

class Textbook(Book):
    def __init__(self, title, item_id, author, subject, grade_level):
        super().__init__(title, item_id, author,)
        self.subject = subject
        self.grade_level  = grade_level 

    def display_course_info(self):
        return f"Title: {self.title} \nAuthor: {self.author} \nPages: {self.pages_count} \nSubject: {self.subject} \nacademic_Level: {self.grade_level} \ncheckout status: {self.get_status()}" 


class Magazine(LibraryItem): 
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.month = datetime.now().month
        self.year = datetime.now().year
    
    def display_issue(self):
        return f"Title: {self.title} \nItem_ID: {self._id} \nIssue_number: {self.issue_number} \nMonth: {self.month} \nYear: {self.year} \ncheckout_status: {self.get_status()}"


# Test your code:
print("-------book------")
book0 = Book("The Silent Code", "B100", "Alan Turing")
book0.set_pages_count(350)
print(book0.display_info())

print("-------textbook------")
textbook1 = Textbook("Introduction to Physics", "T200", "David Hall", "Physics", "Grade 12")
print(textbook1.display_course_info())

print("-------magazine------")
magazine1 = Magazine("Tech Monthly", "M300", "07")
print(magazine1.display_issue())


book0.check_out()
textbook1.check_out()
magazine1.check_out()
print("-------CheckOut------")
print(book0.display_info())
print(textbook1.display_course_info())
print(magazine1.display_issue())


print("-------Return------")
book0.return_item()
print(book0.display_info())
print("---------------------")

# additional example
book = Book("Digital Future", "B400", "Sarah Johnson")
print(book.get_status())  # Available
book.check_out()
print(book.get_status())  # Checked out