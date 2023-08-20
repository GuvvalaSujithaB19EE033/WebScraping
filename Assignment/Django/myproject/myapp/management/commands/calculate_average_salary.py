from django.core.management.base import BaseCommand
from myapp.models import Candidate
import numpy as np
import re

class Command(BaseCommand):
    help = 'Calculate and display the average salary for candidates in Hyderabad'

    def handle(self, *args, **options):
        candidates = Candidate.objects.filter(Location__icontains='Hyderabad')
        #print("Number of candidates:", candidates.count())  # Debug print
       #print("Candidates:", candidates)  # Debug print
        salaries = [parse_salary(candidate.Salary) for candidate in candidates]
        #print("Salaries:", salaries)  # Debug print
        average_salary = np.nanmean(salaries)  # Use np.nanmean to handle NaN values
        self.stdout.write(self.style.SUCCESS(f'Average Salary in Hyderabad: {average_salary:.2f}'))

def parse_salary(salary_string):
    if salary_string is None:
        return np.nan

    salary_string = str(salary_string).replace(',', '').replace('₹', '')
    if 'year' in salary_string:
        match = re.match(r'([\d.-]+)\s*-\s*([\d.-]+)\s*a year', salary_string)
        if match:
            min_salary, max_salary = map(float, match.groups())
            return (min_salary + max_salary) / 2
    elif 'month' in salary_string:
        match = re.match(r'([\d.-]+)\s*-\s*([\d.-]+)\s*a month', salary_string)
        if match:
            min_salary, max_salary = map(float, match.groups())
            return (min_salary + max_salary) * 12
    elif 'day' in salary_string:
        match = re.match(r'Up to ₹([\d.-]+)\s*a day', salary_string)
        if match:
            return float(match.group(1)) * 30 * 12
    return np.nan
