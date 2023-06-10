from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    print(f'Информация по сотрудникам на дату: {datetime.now()}')
    get_employees()
    calculate_salary()