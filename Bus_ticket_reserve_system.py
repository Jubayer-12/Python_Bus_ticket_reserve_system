
class User:

    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password


class Bus:

    def __init__(self,coach,driver,arrival,departure,des_from,des_to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.des_from = des_from
        self.des_to = des_to
        self.seat = ["Empty" for i in range(20)]




class PhitronCompany:

    total_bus = 5
    total_bus_list = [] #Company Databese Eg: [{'coach': 12, 'driver': 'Jubayer', 'arrival': '10 am', 'departure': '12 pm', 'des_from': 'Dhaka', 'des_to': 'Cumilla', 'seat': ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']}]
    
    def bus_install(self):
        bus_no = int(input("Enter Bus No: "))
        flag = 1
        for bus in self.total_bus_list: # Checking bus is already exist
            if bus_no == bus['coach']: #bus['coach'] = 1,2,5,7
                print('Bus is alreay installed!')
                flag = 0
                break

        if flag:
            bus_driver = input("Enter Bus Driver Name: ")
            bus_arrival = input("Enter Bus Arrival Time: ")
            bus_departure = input("Enter Bus Departure Time: ")
            bus_from = input("Enter Bus Destination From: ")
            bus_to = input("Enter Bus Destination To: ")
            #created bus
            self.new_bus = Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            #adding bus to total_bus_list by making disct 
            self.total_bus_list.append(vars(self.new_bus))
            print('Bus install Successfully! Great')



class BusCounter(PhitronCompany):
    user_list = [] #User Databese   
    bus_seat = 20
    
    def reservation(self):
        bus_no = int(input('Enter Bus Number: '))
        flag = 1
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                seat_no = int(input('Enter Seat Number: '))
                seat_no -= 1 
                if seat_no > self.bus_seat:
                    print('There are 20 seats in the bus!')
                elif bus['seat'][seat_no] != 'Empty': #Checking seat Booked or not
                    print('This seat is already Booked,Sorry!')
                else:
                    passenger = input('Enter Your Name: ')
                    bus['seat'][seat_no] = passenger
            else:
                flag = 0
                break

        if flag == 0:
            print('This Number Bus is not Available!')
 
    def showBusInfo(self): #one bus info
        bus_no = int(input("Enter Bus No: ")) 
        for bus in self.total_bus_list:
            if bus['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} Bus Info {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t  Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t\t  Departure : {bus['departure']}")
                print(f"From : {bus['des_from']} \t\t  To : {bus['des_to']}")
              
                #Making Bus seat as Real
                idx = 1

                for i in range(5):
                    for j in range(2):
                        print(f"{idx}. {bus['seat'][idx-1]}",end="\t")
                        idx+=1

                    print("\t",end="")

                    for j in range(2):
                        print(f"{idx}. {bus['seat'][idx-1]}",end="\t")
                        idx+=1
                    print()

    def get_users(self):
        return self.user_list

    def create_account(self):
        name = input('Enter your name: ')
        flag = 0
        for username in self.user_list:
            if username == name:
                print('Username Already Exists!')
                flag = 1
                break

        if flag == 0:
            password = input('Enter password: ')
            self.new_user = User(name,password)
            self.user_list.append(vars(self.new_user))
            print("Account Create Successfully!!")
 

    def Available_buses(self): # All bus info
        if len(self.total_bus_list) == 0:
            print("No Bus Available!")
        else:
            for bus in self.total_bus_list:
                    print('*'*50)
                    print()
                    print(f"{' '*10} {'#'*10} Bus Info {'#'*10}")
                    print(f"Bus Number : {bus['coach']} \t\t  Driver : {bus['driver']}")
                    print(f"Arrival : {bus['arrival']} \t\t  Departure : {bus['departure']}")
                    print(f"From : {bus['des_from']} \t\t  To : {bus['des_to']}")
                
                    #Making Bus seat as Real
                    idx = 1

                    for i in range(5):
                        for j in range(2):
                            print(f"{idx}. {bus['seat'][idx-1]}",end="\t")
                            idx+=1

                        print("\t",end="")

                        for j in range(2):
                            print(f"{idx}. {bus['seat'][idx-1]}",end="\t")
                            idx+=1
                        print()






""" 
1. Create An account -> Create_new_account()[]

2. Login to your account -> Authentic User
                         -> 1.Available Buses
                         -> 2.Reservation
                         -> 3.Show Bus info

                         -> Adminstrator (UN: Admin, Pas: 123)
                         -> 1.install buses
                         -> 2.See Available Buses
                         -> 3.See total userList

3. Exist 

"""


while True:

    ticket_counter = BusCounter()
    print("1.Create An Account \n2.Login To Your Account \n3.Exit")
    user_input = int(input('Enter Your choice: '))
    if user_input == 1:
        ticket_counter.create_account()
    elif user_input == 2:
        name = input('Enter your name: ')
        password = input('Enter your password: ')
        isAdmin = False
        flag = 0
        if name == 'admin' and password == 'admin123':
            isAdmin = True
        if isAdmin == False: #Means normal user
            for user in ticket_counter.user_list: #orginal normal user check
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break

            if flag:
                while True:
                    print(f"1.Available Buses \n2.Show Bus info \n3.Reservation \n4.Exit")
                    service = int(input('Select A Service: '))
                    if service == 1:
                        ticket_counter.Available_buses()
                    elif service == 2:
                        ticket_counter.showBusInfo()
                    elif service == 3:
                        ticket_counter.reservation()
                    elif service == 4:
                        break

            else:
                print("Wrong User info!")

        else:
            while True:
                print('Hi Admin,You are welcom!')
                print(f"1.Install Buse \n2.Available Buses \n3.Show Bus \n4.Show user list \n5.Exit")
                admin_service = int(input('Enter A Service: '))
                if admin_service == 1:
                    ticket_counter.bus_install()
                elif admin_service == 2:
                    ticket_counter.Available_buses()
                elif admin_service == 3:
                    ticket_counter.showBusInfo()
                elif admin_service == 4:
                    ticket_counter.get_users()
                else:
                    break