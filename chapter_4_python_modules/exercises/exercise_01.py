#Solved exercise: calculating the dates and installments of a loan
# Maria took a loan of 1,000,000
# to make the payment in 5 years.
# The date she took the loan was
# 12/20/2020 and the maturity of each installment
# is on the 20th of every month.
# - Create the loan date
# - Create the loan end date
# - Show all due dates and the value of each installment

from datetime import datetime

from dateutil.relativedelta import relativedelta

full_value = 1_000_000
date_loan = datetime(2020, 12, 20)
delta_years = relativedelta(years=5)
end_date = date_loan + delta_years

date_installments = []
date_installment = date_loan

while date_installment < end_date:
    date_installments.append(date_installment)
    date_installment += relativedelta(month=1)

number_installments = len(date_installments)
value_installment = full_value / number_installments

for date in date_installments:
    print(date.strftime('%d/%m/%Y'), f'R$ {value_installment:,.2f}')

