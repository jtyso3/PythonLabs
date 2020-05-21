'''
Jacob Tyson
10/1/2019
Title: Average Rainfall document.
Description: This program will calculate the average rainfall over a certain amount of years, and then calculates the
total average yearly rainfall and total average monthly rainfall. The input function will take in the users input, and the
processing function will take from the input function to process the user input to obtain monthly rainfall, and calculate
the monthly and yearly rainfall averages.

'''

def main():
    multiyear_total = 0  # used for challenge level - initialize 2 study-wide variables
    multiyear_avg = 0  # 2nd study-wide variable
    outputs()
#Gather User input, with validation
def inputs():
    num_years = input('How many years are in your rainfall sample? ')
    while num_years.isnumeric() is False or int(num_years) < 0:
        num_years = input("Please enter a whole number greater than zero.")
    num_years = int(num_years)
    return num_years

#Gathers monthly amount of rainfall, calculates average and total monthly and yearly rainfall.
def processing():
    multiyear_total = 0
    multiyear_avg = 0
    num_years = inputs()
    for year in range(num_years):
        total_rain_year = 0
        avg_rain_year = 0.00
        print(f'Rainfall info for year #{year + 1}: ')
        for month in range(12):
            rain_for_month = input(f'\tEnter rain for month #{month + 1}: ')
            while rain_for_month.isnumeric() is False or int(rain_for_month) < 0: #validation
                rain_for_month = input('please enter a whole number.')
                continue
            rain_for_month = int(rain_for_month)
            total_rain_year += rain_for_month
        avg_rain_year = total_rain_year / 12
        print(f'Total rain in inches for year #{year + 1} = {total_rain_year}')
        print(f'Year #{year + 1} Monthly Avg Rainfall = {avg_rain_year :<.2f}')
        multiyear_total += total_rain_year
        multiyear_avg = multiyear_total / num_years / 12  # calc. study avg.
    return multiyear_total, multiyear_total
#Gives output of total and average amount of rainfall.
def outputs():
    multiyear_total, multiyear_avg = processing()
    print(f'\nTotal rain, all years = {multiyear_total} inches')
    print(f'Average monthly rain, all years = {multiyear_avg} inches')
    print('Thanks for using the program!')  # exit msg.
main()