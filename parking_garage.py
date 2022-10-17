"""
Your parking garage class should have the following methods:
- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1

- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) 
   -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True

- leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary
"""

class Parking():
    tickets = ["open spaces"] * 10
    parkingSpaces = ["open spaces"] * 10
    currentTicket = {"paid": False}

    def takeTicket(self):
        Parking.tickets.pop()
        Parking.parkingSpaces.pop()
        
    def payForParking(self):
        payment = input("Please input payment amount: ")
        if payment != '':
            print("Thanks for paying, you may now leave the garage")
            Parking.currentTicket['paid'] = True
        else:
            print("Your ticket is not paid, you have 15 minutes to leave.")

    def leaveGarage(self):
        if Parking.currentTicket['paid'] == True:
            print("Thank you, have a nice day!")
        else:
            payment = input("Please input payment amount: ")
            if payment != '':
                print("Thank you, have a nice day!")
        Parking.tickets.append("open spaces")
        Parking.parkingSpaces.append("open spaces")

garage = Parking()

def run():
    while True:
        question = input("Please enter: Buy, Pay, or Leave: ")
        if question.lower() == 'buy':
            garage.takeTicket()
        elif question.lower() == 'pay':
            garage.payForParking()
        elif question.lower() == 'leave':
            garage.leaveGarage()
            break
        else:
            print('Please enter a valid input')

run()
