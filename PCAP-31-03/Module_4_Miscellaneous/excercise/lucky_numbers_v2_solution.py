import random
import datetime
import time

todays_draw = []
available_nums = [x + 1 for x in range(25)]
results = dict()


class InvalidTicketException(Exception):
    pass


def lotto_draw():

    delta = datetime.date.today() - datetime.date(1970, 1, 1)
    random.seed(delta.days)
    global todays_draw
    todays_draw = random.sample(available_nums, k=3)
    todays_draw.sort()

    todays_date = datetime.date.today()
    print(f"The result of today's draw on {datetime.date.strftime(todays_date, '%d/%m/%Y')} is........\n\n")

    for number in todays_draw:
        time.sleep(3)
        print(f'* {number} *')


def check_numbers():

    correct_nums = 0

    print('\nPlease enter your lotto numbers, separated by commas')
    user_input = input()

    your_numbers = user_input.split(',')

    try:
        if len(your_numbers) != 3: 
            raise InvalidTicketException('\nInvalid Ticket:\tShould contain three numbers')

        for i in range(len(your_numbers)):
            your_numbers[i] = int(your_numbers[i])

        for num in your_numbers:
            assert num in available_nums, '\nThis ticket contains numbers that are not in the draw (1 to 25)'

    except(InvalidTicketException, ValueError) as e:
        print('\n', e.args[0])
        return
    except Exception as e:
        print(e.args[0])
        return
    else:
        print('\nThank you for providing your lotto numbers. We will check them now.....')

    for num in your_numbers:
        if num in todays_draw:
            print(f'\n***{num} was drawn***')
            correct_nums += 1

    print(f'\nYou got {correct_nums} number/s correct!')

    if correct_nums == 3:
        print(f'\nWow, you have won the lotto!')


def load_historical_draws():

    file = open('lotto_results.txt', 'r')

    for line in file:
        result = line.split(':')
        results[result[0]] = result[1].strip()

    file.close()


if __name__ == '__main__':

    payouts = [10, 75, 1000]
    new_payouts = list(map(lambda x: x * 1.2, payouts))
    print(f'Payouts as follows:\n1 number: €{new_payouts[0]}\n2 numbers: €{new_payouts[1]}\n3 numbers: €{new_payouts[2]}\n')

    lotto_draw()
    check_numbers()

    print("Would you like to check the numbers for a previous draw? "
          "If so, please press the 'y' key and then press enter.")
    old_draws = input()

    if old_draws.lower() == 'y':
        print('Please enter the date for the draw that you wish to check. '
              'It should be entered in the following format: dd/mm/yyyy')
        date_of_draw = input()
        load_historical_draws()

        if date_of_draw in results.keys():
            print(f'The numbers drawn on {date_of_draw} were: {results[date_of_draw]}')
        else:
            print("There wasn't a draw on that particular date.")
