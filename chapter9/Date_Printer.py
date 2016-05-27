def main():
    date = raw_input("Enter the a date in the following format 'mm/dd/yyy': ")
    new_date = date.split('/')
    print verify_month(new_date) + new_date[1] + ', ' + new_date[2]

def verify_month(rr):
    if rr[0] == '01':
        return 'January '
    if rr[0] == '02':
        return 'February '
    if rr[0] == '03':
        return 'March '
    if rr[0] == '04':
        return 'April '
    if rr[0] == '05':
        return 'May '
    if rr[0] == '06':
        return 'June '
    if rr[0] == '07':
        return 'July '
    if rr[0] == '08':
        return 'August '
    if rr[0] == '09':
        return 'September '
    if rr[0] == '10':
        return 'October '
    if rr[0] == '11':
        return 'November '
    if rr[0] == '12':
        return 'December '
main()