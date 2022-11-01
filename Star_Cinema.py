class _Star_Cinema:
    __hall_list = []

    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    def entry_hall(self):
        hall = [self._hall_no, self._rows, self._cols]
        _Star_Cinema.__hall_list.append(hall)


class _Hall(_Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        super().__init__(rows, cols, hall_no)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        lst = []
        self.__show_list.append(show)
        for i in range(self._rows):
            r = [f'{chr(i + 65)}{j + 1}' for j in range(self._cols)]
            lst.append(r)
        self.__seats[id] = lst

    def book_seats(self, name, phone_number, id, book_seats):
        correct_id = False
        booked = False
        for key, value in self.__seats.items():
            if key == id:
                correct_id = True
                for seat in book_seats:

                    if value[seat[0] - 1][seat[1] - 1] != 'X':
                        value[seat[0] - 1][seat[1] - 1] = 'X'
                    else:
                        booked = True
                        break

        if booked:
            print("This seats are already booked! Try another seats.")

        if not correct_id:
            print("This movie id is wrong or unavailable. Please try again!")

        movie_name = ""
        time = ""
        b_seats = ""
        for show in self.__show_list:
            if show[0] == id:
                movie_name = show[1]
                time = show[2]

        for s in book_seats:
            b_seats += f'{chr(s[0] - 1 + 65)}{s[1]} '

        if not booked and correct_id:
            print("-----------------------------------------------------------------------------------")
            print("######### Booking ticket successful! #########")
            print("-----------------------------------------------------------------------------------")
            print(f'Name: {name}')
            print(f'Phone Number: {phone_number}\n\n')
            print(f'Movie Name: {movie_name}\t\t\tMovie Time: {time}')
            print(f'Tickets: {b_seats}\nHall: {self._hall_no}')
            print("-----------------------------------------------------------------------------------")

    def view_show_list(self):
        for show in self.__show_list:
            print(f'Movie Name: {show[1]}\t\t\tShow ID: {show[0]}\t\t\tTime: {show[2]}')

    def view_available_seats(self, id):

        valid_id = False
        for key, value in self.__seats.items():
            if key == id:
                valid_id = True
                for i in range(self._rows):
                    for j in range(self._cols):
                        if value[i][j] != 'X':
                            print(value[i][j], end=" ")
                    print()
        if not valid_id:
            print("This movie id is wrong or unavailable. Please try again!")
            print("-----------------------------------------------------------------------------------")


def menu():
    print("-----------------------------------------------------------------------------------")
    print("1. View all running shows.")
    print("2. View available seats.")
    print("3. Book tickets.")
    print("4. Exit.")


h = _Hall(5, 22, "a22")

h2 = _Hall(5, 7, "a33")
h.entry_show("www", "Bostir Rani Suriya", "2.00pm")
h.entry_show("xxx", "No 1 Shakib Khan", "7.30pm")
h.entry_show("zzz", "Gorib The Chotolok", "9.30pm")
h.entry_show("aaa", "Sokal The Morning", "12.30pm")
h.entry_hall()
h2.entry_hall()
run = True
while run:
    menu()
    x = int(input("Enter your choice: "))
    if x == 1:
        print("-----------------------------------------------------------------------------------")
        h.view_show_list()
    elif x == 2:
        id = input("Enter movie ID: ")
        print("-----------------------------------------------------------------------------------")
        h.view_available_seats(id)
    elif x == 3:
        name = input("Enter your name: ")
        phone_number = input("Enter your mobile number: ")
        id = input("Enter movie ID: ")
        number_of_tickets = int(input("Enter number of tickets you want: "))
        seats = input("Enter seat number: ")
        lst = seats.split(" ")
        ticket = []
        is_ok = True
        for i in lst:
            t = (ord(i[0]) - 65 + 1, int(i[1:]))
            ticket.append(t)
            if t[0] < 1 or t[0] >= h._rows or t[1] < 1 or t[1] >= h._cols:
                is_ok = False
                break
        if is_ok:
            h.book_seats(name, phone_number, id, ticket)
        else:
            print("-----------------------------------------------------------------------------------")
            print("######### Sorry!!! Invalid seat number. #########")
            print("-----------------------------------------------------------------------------------")
    elif x == 4:
        run = False
    else:
        print("Wrong input. Try again")


