from tabulate import tabulate

# Create class for hotel data.
class Hotel:
    sortParam = 'name'

    def __init__(self) -> None:
        self.name = ''
        self.roomAvl = 0
        self.location = ''
        self.rating = int
        self.pricePr = 0

    def __lt__(self, other):
        getattr(self, Hotel.sortParam) < getattr(other, Hotel.sortParam)

    @classmethod
    def sortByName(cls):
        cls.sortParam = 'name'

    @classmethod
    def sortByRate(cls):
        cls.sortParam = 'rating'

    @classmethod
    def sortByRoomAvailable(cls):
        cls.sortParam = 'roomAvl'

    def __repr__(self) -> str:
        return "HOTELS DATA:\nHotelName:{}\tRoom Available:{}\tLocation:{}\tRating:{}\tPricePer Room:{}".format(
            self.name, self.roomAvl, self.location, self.rating, self.pricePr)


# Create class for user data.
class User:
    def __init__(self) -> None:
        self.uname = ''
        self.uId = 0
        self.cost = 0

    def __repr__(self) -> str:
        return "UserName:{}\tUserId:{}\tBooking Cost:{}".format(self.uname, self.uId, self.cost)


def PrintHotelData(hotels):
    data = []
    for hotel in hotels:
        data.append([hotel.name, hotel.roomAvl, hotel.location, hotel.rating, hotel.pricePr])
    print(tabulate(data, headers=["Hotel Name", "Room Available", "Location", "Rating", "Price Per Room"],
                   tablefmt="pretty"))


def SortHotelByName(hotels):
    Hotel.sortByName()
    hotels.sort(key=lambda x: getattr(x, Hotel.sortParam))



def SortHotelByRating(hotels):
    Hotel.sortByRate()
    hotels.sort(key=lambda x: getattr(x, Hotel.sortParam))
  

def PrintHotelBycity(s, hotels):
    hotelsByLoc = [h for h in hotels if h.location == s]



def SortByRoomAvailable(hotels):
    Hotel.sortByRoomAvailable()
    hotels.sort(key=lambda x: getattr(x, Hotel.sortParam))




def PrintUserData(userName, userId, bookingCost, hotels):
    users = []
    for i in range(len(userName)):
        u = User()
        u.uname = userName[i]
        u.uId = userId[i]
        u.cost = bookingCost[i]
        users.append(u)

    data = []
    for user, hotel in zip(users, hotels):
        data.append([user.uname, user.uId, user.cost, hotel.name])

    print(tabulate(data, headers=["User Name", "User ID", "Booking Cost", "Hotel Name"], tablefmt="pretty"))


def HotelManagement(userName, userId, hotelName, bookingCost, rooms, locations, ratings, prices):
    hotels = []

    for i in range(5):
        h = Hotel()
        h.name = hotelName[i]
        h.roomAvl = rooms[i]
        h.location = locations[i]
        h.rating = ratings[i]
        h.pricePr = prices[i]
        hotels.append(h)

    SortHotelByName(hotels)
    SortHotelByRating(hotels)
    PrintHotelBycity("Dhakkaa", hotels)
    SortByRoomAvailable(hotels)
    PrintUserData(userName, userId, bookingCost, hotels)


if __name__ == '__main__':
    userName = ["U1", "U2", "U3", "U4", "U5"]
    userId = [2, 3, 4, 5, 6]
    hotelName = ["Pan Pacific Sonargaon Dhaka", "The Westin Dhaka", "InterContinental Dhaka",
                 "Radisson Blu Chattogram Bay View", "The Peninsula Chittagong Hotel"]
    bookingCost = [1000, 1200, 1100, 900, 950]
    rooms = [14, 2, 6, 3, 24]
    locations = ["Dhaka", "Dhaka", "Dhaka", "Chittagong", "Chittagong"]
    ratings = [5, 5, 5, 4, 4]
    prices = [200, 250, 180, 150, 160]


