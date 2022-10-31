class Star_Cinema:
    hall_list = []

    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_hall(self):
        hall = [self.hall_no, self.rows, self.cols]
        Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        super().__init__(rows, cols, hall_no)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        lst = []
        self.show_list.append(show)
        for i in range(self.rows):
            r = [f'{chr(i + 65)}{j + 1}' for j in range(self.cols)]
            lst.append(r)
        self.seats[id] = lst

    def book_seats(self, name, phone_number, id, book_seats):
        correct_id = False
        booked = False
        for key, value in self.seats.items():
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
        for show in self.show_list:
            if show[0] == id:
                movie_name = show[1]
                time = show[2]

        for s in book_seats:
            b_seats += f'{chr(s[0]-1+65)}{s[1]} '

        if not booked and correct_id:
            print("--------------------------------------------------------")
            print("######### Booking ticket successful! #########")
            print("--------------------------------------------------------")
            print(f'Name: {name}')
            print(f'Phone Number: {phone_number}\n\n')
            print(f'Movie Name: {movie_name}\t\t\tMovie Time: {time}')
            print(f'Tickets: {b_seats}\t\t\tHall: {self.hall_no}')
            print("--------------------------------------------------------")

    def view_show_list(self):
        for show in self.show_list:
            print(f'Movie Name: {show[1]}\t\t\tShow ID: {show[0]}\t\t\tTime: {show[2]}')

    def view_available_seats(self, id):

        for key, value in self.seats.items():
            if key == id:
                for i in range(self.rows):
                    for j in range(self.cols):
                        if value[i][j] != 'X':
                            print(value[i][j], end=" ")
                    print()

    def menu(self):
        print("------------------------------------------------")
        print("1. View all running shows.")
        print("2. View available seats.")
        print("3. Book tickets.")


h = Hall(5, 7, "a22")
h2 = Hall(5, 7, "a33")
h.entry_show("www", "Bostir Rani Suriya", "2.06pm")
h.entry_show("xxx", "No 1 Shakib Khan", "7.30pm")
h.entry_show("zzz", "Gorib The Chotolok", "9.30pm")
h.entry_show("aaa", "Sokal The Morning", "1.30pm")
h.entry_hall()
h2.entry_hall()
h.book_seats("Shakil", "01*******", "www", [(1, 3), (1, 1)])
h.book_seats("Soha", "01*******", "aaa", [(1, 3), (2, 4)])
# h.view_show_list()
h.view_available_seats("www")
h.view_show_list()
