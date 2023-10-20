from datetime import datetime
from collections import defaultdict
from colorama import Fore


def get_birthdays_per_week(users):
    if not users:
        print("Your calendar is empty")
    users_birthdays_dict = defaultdict(list)
    dict_of_users = dict()
    
    current_date = datetime.today().date()
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=current_date.year)
        
        # replace users year for current year
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=(current_date.year + 1))
        
        # replace notice day
        birthday_this_year = replace_birthday_date(birthday_this_year)  
        
        # looking for different between current date and user's birthday
        delta_days = (birthday_this_year - current_date).days
        if delta_days < 7:
            weekday = birthday_this_year.weekday()
            birthday_weekday = birthday_this_year.strftime('%A')
            
            # if we already have this weekday we just add new user's birthday 
            # to birthday's list for current day
            if weekday in dict_of_users:
                dict_of_users[weekday][birthday_weekday].append(name)
            else:
                # if user's birthday is meet first time we check if we don't 
                # take user's birthday from previous day and add to dict
                users_birthdays_dict[birthday_weekday].append(name)
                if len(users_birthdays_dict) > 1:
                    key = list(users_birthdays_dict.keys())[0]
                    del users_birthdays_dict[key]
                dict_of_users[weekday] = dict(users_birthdays_dict)
    # sort user's birthdays from nearest to further
    dict_of_users = sorted_users_notes(sorted(dict_of_users.items()), current_date.weekday())
    
    #print days and list of users who have birthday in this day
    print_notes(dict_of_users)
    

# print days and list of users who have birthday in this day
def print_notes(notes_dict):
    for _, value in notes_dict.items():
        for weekday, names in value.items():
            weekdey_str = Fore.BLUE + '{: >10}'.format(weekday)
            names_str = Fore.YELLOW+ '{: <10}'.format(', '.join(names))
            print(f"{weekdey_str} : {names_str}")

# sort user's birthdays from nearest to further
def sorted_users_notes(users_birthdays_dict, current_day):
    first_dict = dict()
    second_dict = dict()
    for day, values in users_birthdays_dict:
        if day >= current_day:
            first_dict[day] = values
        else:
            second_dict[day] = values
    return first_dict | second_dict

# replace notice day if it is not convenient day
def replace_birthday_date(date):   
    """ replace notice day if birthday it is: 
    -weekend day
    -last day of the month
    -last day of the year
"""     
    if date.weekday() == 5:
        if date.month == 2 and date.day >= 27:
            if date.year % 2 == 0 and date.day == 28:
                date = date.replace(month=date.month + 1, day=1)
            elif date.year % 2 == 0 and date.day == 29: 
                date = date.replace(month=date.month + 1, day=2)   
            elif date.year % 2 != 0 and date.day == 27:
                date = date.replace(month=date.month + 1, day=1)
            elif date.year % 2 != 0 and date.day == 28: 
                date = date.replace(month=date.month + 1, day=2)  
        elif date.month in [1, 3, 5, 7, 8, 10, 12] and date.day >= 30:   
            if date.month == 12:
                if date.day == 30:
                    date = date.replace(year=date.year + 1, month=1, day=1)
                elif date.day == 31:
                    date = date.replace(year=date.year + 1, month=1, day=2)
            elif date.day == 30:
                date = date.replace(month=date.month + 1, day=1)
            elif date.day == 31:
                date = date.replace(month=date.month + 1, day=2)
        elif date.month in [4, 6, 9, 11] and date.day >= 29:
            if date.day == 29:
                date = date.replace(month=date.month + 1, day=1)
            elif date.day == 30:
                date = date.replace(month=date.month + 1, day=2)
        else:
            date = date.replace(day=date.day + 2)
    if date.weekday() == 6:    
        if date.month == 2 and date.day >= 28:
            if date.year % 2 == 0 and date.day == 29: 
                date = date.replace(month=date.month + 1, day=1)   
            elif date.year % 2 != 0 and date.day == 28: 
                date = date.replace(month=date.month + 1, day=1)  
        elif date.month in [1, 3, 5, 7, 8, 10, 12] and date.day >= 29:   
            if date.month == 12:
                if date.day == 31:
                    date = date.replace(year=date.year + 1, month=1, day=1)
            elif date.day == 31:
                date = date.replace(month=date.month + 1, day=1)
        elif date.month in [4, 6, 9, 11] and date.day == 30:
            date = date.replace(month=date.month + 1, day=1)
        else:
            date = date.replace(day=date.day + 1)
    return date
    

# test data for the week
users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 22)},
         {"name": "John Snow", "birthday": datetime(1990, 10, 15)},
         {"name": "Harry Potter", "birthday": datetime(1967, 10, 20)},
         {"name": "Rock", "birthday": datetime(1950, 10, 21)},
         {"name": "Silvester Stallone", "birthday": datetime(1955, 10, 20)},
         {"name": "Madonna", "birthday": datetime(1955, 10, 22)},
         {"name": "Rand Al'Tor", "birthday": datetime(1955, 10, 16)},
         {"name": "Monkey D.Luffy", "birthday": datetime(1955, 10, 18)}]

if __name__ == "__main__":
    get_birthdays_per_week(users)