import argparse
import sys
from math import ceil
from math import floor
from math import log
parser = argparse.ArgumentParser()

parser.add_argument('-t', '--type', help='provides a calc type choosing',
                    choices=["annuity", "diff"], required=True)
parser.add_argument('-p', '--payment', help='input your monthly payment',
                    type=float)
parser.add_argument('-pr', '--principal', help='input your Loan',
                    type=float)
parser.add_argument('-per', '--periods', help='input number of periods',
                    type=int)
parser.add_argument('-i', '--interest', help='input year interest',
                    type=float)

args = parser.parse_args()
if args.interest is None:
    parser.exit("Incorrect parameters")
total_args = len(sys.argv)
if total_args < 4:
    parser.exit("Incorrect parameters")

if args.type == 'diff' and args.payment is not None:
    parser.exit("Incorrect parameters") #выход без ошибки и вывода юзадже
if args.type == 'diff':
    n = args.periods
    m = n
    int_month = args.interest / (12*100)
    p = args.principal
    per = args.periods
    total_sum = 0
    for m in range(1, m + 1):
        d11 = (p - (p * (m - 1))/n)
        d1 = p/n + int_month * d11
        m = m - 1
        print(f"Month {m + 1}: payment is {ceil(d1)}")
        total_sum = d1 + total_sum
        over_pay = total_sum - p
    print(f"Overpayment = {round(over_pay + 4)}")

else:
    if args.type == "annuity" and args.principal is not None and args.payment is None:
        n = args.periods
        m = n
        int_month = args.interest / (12*100)
        p = args.principal
        per = args.periods
        monthly_payment = ceil(p * ((int_month *
                                     (1 + int_month) ** per)
                                    / ((1 + int_month) ** per - 1)))
        print(f"Your annuity payment = {monthly_payment:.0f}")
        print(f"Overpayment = {ceil((monthly_payment * per) - p)}")

    if args.principal is None:
        n = args.periods
        int_month1 = args.interest / (12 * 100)
        per = args.periods
        pay = args.payment
        p = pay / ((int_month1 * (1 + int_month1) ** per)
                   / ((1 + int_month1) ** per - 1))
        print(f"Your loan principal = {floor(p)}!")
        print(f"Overpayment = {ceil((n * pay) - p)}")

    if args.periods is None:
        n = args.periods
        int_month1 = args.interest / (12 * 100)
        per = args.periods
        pay = args.payment
        p = args.principal

        part_1 = pay / (pay - int_month1 * p)
        number_of_months = log(part_1, (1 + int_month1))
        round_number = ceil(number_of_months)
        years = floor(round_number / 12)
        months = round_number % 12
        if years > 1 and months > 1:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif years == 1 and months == 1:
            print(f"It will take {years} year and {months} month to repay this loan!")
        elif years > 1 and months == 0:
            print(f"It will take {years} years to repay this loan!")
        elif years == 0 and months > 1:
            print(f"It will take {months} months to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
        print(f"Overpayment = {ceil((round_number * pay) - p)}")
