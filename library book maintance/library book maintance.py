library={}
def add_book(title,author,year):
    book={'Title':title,'author':author,'Year':year}
    library[title]=book
    print(f'{title}added to library.')
def remove_book(title):
        if title in library:
            del library[title]
            print(f'{title}removed from library.')
        else:
            print(f'{title}not found in library.')
def print_library():
        for title,book in library.items():
            print(f'Title:{book["Title"]},author:{book["Author"]},Year:{book["year"]}')
def main():
        while True:
           print("1.Add book")
           print("2.remove book")
           print("3.print library")
           print("4.Exit")
           choice=input("Enter your choice:")
           if choice=='1':
                title=input("Enter the title:")
                author=input("Enter the author:")
                year=input("enter the year:")
                add_book(title,author,year)
           elif choice=='2':
                titile=input("Enter the title of the book to remove:")
                remove_book(title)
           elif choice=='3':
                print("library Contents:")
                print_library()
           elif choice=='4':
                print("Exiting the Library program.")
                break
           else:
                print("invalid choice.please select a valid option.")
if __name__=="__main__":
    main()
                    
            
    
