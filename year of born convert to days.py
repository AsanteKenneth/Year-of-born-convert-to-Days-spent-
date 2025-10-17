year=int(input("enter your year of birth: "))
current_year=int(input("enter thr current year we are right now: "))

main_year=current_year-year

leap_year=main_year//4
non_leap_year=main_year - leap_year

days_in_leap_year=leap_year*366
days_in_non_leap_year=non_leap_year*365

total_days=days_in_leap_year+days_in_non_leap_year
print(f"YOUR TOTAL DAYS SPENT FROM {year} TO {current_year} IS {total_days} DAYS THANK YOUR CREATURE")
