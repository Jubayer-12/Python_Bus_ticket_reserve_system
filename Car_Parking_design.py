import time

class Car:
    def __init__(self,license,model,color):
        self.license = license
        self.model = model
        self.color = color

    def __repr__(self) -> str:
        return f"{self.license},{self.model},{self.color}"



class Garage:

    def __init__(self) -> None:
        self.sport = 10 # 10 place for 10 cars
        self.sport_name = {'A1':'Empty','B1':'Empty','C1':'Empty','D1':'Empty','E1':'Empty',
        'F1':'Empty','G1':'Empty','H1':'Empty','I1':'Empty','J1':'Empty'}
        self.car_added = []  #instance attribute
        self.car_infos = {'Tickets':[], 'License':[], 'Model':[], 'Color':[]}
        self.bill = 0
        

    def sport_available(self):
        return self.sport

    def garage_car_info(self):
        print(self.car_infos)


    def car_park_in_garage(self,cumtomer_car):

        if self.sport_available() > 0:
            car_data = str(cumtomer_car).split(',')
            self.car_added.append(car_data)
            self.sport-=1
            ticket = ''
            for park_sport in self.sport_name:
                if self.sport_name[park_sport] == 'Empty':
                    ticket = park_sport + car_data[0]
                    self.sport_name[park_sport] = ticket
                    self.car_infos['Tickets'].append(ticket)
                    self.car_infos['License'].append(car_data[0])
                    self.car_infos['Model'].append(car_data[1])
                    self.car_infos['Color'].append(car_data[2])
                    print(f'Your Car: {car_data[1]} Parked Successfully!\nYour Ticket: {ticket}')
                    break
        else:
            print('Currently We Are Full, Sorry!')


    def car_unpark_from_garage(self,cutomer_ticket,paked_hour):

        carFound = False
        for idx,ticket in enumerate(self.car_infos['Tickets']):
            if ticket == cutomer_ticket:
                carFound = True
                print('Got the Car!!')
                print(f"Your Car's License: {self.car_infos['License'][idx]}")
                print(f"Your Car's Model: {self.car_infos['Model'][idx]}")
                print(f"Your Car's Color: {self.car_infos['Color'][idx]}")
            
                if paked_hour <= 10:
                    total_bill = 5*paked_hour
                    print(f'Your Total Bill: ${total_bill}')
                    self.bill+=total_bill
                else:
                    total_bill = 5*paked_hour + 50 
                    print(f'Your Total Bill: total_bill')
                    self.bill+=total_bill

                while self.bill != 0 :
                    payment = int(input('Pay Bill Please(Amount): $'))
                    if payment >= self.bill:
                        self.bill -= payment
                        if self.bill < 0:
                            print(f'Here is your extra money: ${self.bill * -1}')
                        print('Thank you, bill paid successfully!')
                        print('Car is being unparked')
    
                        for car_ticket in self.sport_name:
                            if self.sport_name[car_ticket] == cutomer_ticket:
                                self.sport_name[car_ticket] = 'Empty'
                                time.sleep(2)
                                print('Here is your Car!')
                                time.sleep(2)
                                print(f"Your Car's License: {self.car_infos['License'][idx]}")
                                print(f"Your Car's Model: {self.car_infos['Model'][idx]}")
                                print(f"Your Car's Color: {self.car_infos['Color'][idx]}")
                                time.sleep(2)
                                print('Thank you,Have a nice Day!')
                                self.sport+=1
                                self.car_infos['Tickets'].pop(idx)
                                self.car_infos['License'].pop(idx)
                                self.car_infos['Model'].pop(idx)
                                self.car_infos['Color'].pop(idx)
                                return
                    else:
                        self.bill -= payment
                        print(f'Need: ${self.bill} More Money!')

        if carFound == False:
            print('No Car Found!\nInvalid Ticket,Give a Valid Ticket.')






My_garage = Garage()

print("\n****** Welcome To Our Car Parking Zoon! *****\n")

while True:

    print()
    print('OPTIONS')
    print("1.Garage's Sport Availablity Check")
    print('2.Park Your Car')
    print('3.UnPark Your Car')
    print()

    user_option = int(input('Enter An Option: '))

    if user_option == 1:
        print(f"Our Garage Has: {My_garage.sport_available()} Sport Left")

    elif user_option == 2:
        if My_garage.sport_available() > 0:
            car_license = input('Give Your License: ')
            car_model = input('Car Model/Brand: ')
            car_color = input('Car Color: ')
            new_car = Car(car_license,car_model,car_color)
            My_garage.car_park_in_garage(new_car)
        else:
            print('Currently We Are Full, Sorry!')
            break

    else:
        ticket = input('Enter Your Ticket Code: ')
        park_user_hour = int(input('How Many Hours Car has : '))
        My_garage.car_unpark_from_garage(ticket,park_user_hour)

