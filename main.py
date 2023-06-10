from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print(f'Информация по сотрудникам на дату: {datetime.now()}')
    get_employees()
    calculate_salary()
