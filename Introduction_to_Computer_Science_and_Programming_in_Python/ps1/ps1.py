# Problem Set 1

from os import system

system("clear")


# Part A: House Hunting


def monthsToPay(annual_salary, portion_saved, total_cost):
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    nb_months = 0
    while current_savings < portion_down_payment*total_cost:
        # investment winning funds (r)
        current_savings += current_savings*r/12
        # portion saved % of annual salary
        current_savings += portion_saved*annual_salary/12
        nb_months += 1
    return nb_months


def monthsToPayTest():
    a_s = float(input("Enter your annual salary: "))
    p_s = float(
        input("Enter the percent of your salary to save, as a decimal: "))
    t_c = float(input("Enter the cost of your dream home: "))
    print(f"Number of months: {monthsToPay(a_s,p_s,t_c)}")


# Part B: Saving, with a raise

def monthsToPayRaise(annual_salary, portion_saved, total_cost,
                     semi_annual_raise):
    current_salary = annual_salary
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    nb_months = 0
    while current_savings < portion_down_payment*total_cost:
        # Check if we have a raise this month (!= 0 and = 0 mod 6)
        if nb_months != 0 and nb_months % 6 == 0:
            current_salary *= (1+semi_annual_raise)
        # investment winning funds (r)
        current_savings += current_savings*r/12
        # portion saved % of annual salary
        current_savings += portion_saved*current_salary/12
        nb_months += 1
    return nb_months


def monthsToPayRaiseTest():
    a_s = float(input("Enter your annual salary: "))
    p_s = float(
        input("Enter the percent of your salary to save, as a decimal: "))
    t_c = float(input("Enter the cost of your dream home: "))
    s_a_r = float(input("Enter the semi-annual-raise, as a decimal: "))
    print(f"Number of months: {monthsToPayRaise(a_s,p_s,t_c,s_a_r)}")


# Part C: Finding the right amount to save away
