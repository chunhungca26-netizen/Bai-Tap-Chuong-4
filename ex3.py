class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        return "Undefined"

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, base_salary):
        super().__init__(emp_id, name)
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, work_hours, hourly_rate):
        super().__init__(emp_id, name)
        self.work_hours = work_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.work_hours * self.hourly_rate

# Lớp System Management ---

class EmployeeSystem:
    def __init__(self):
        self.employees = [] # Mảng chứa danh sách nhân viên

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Đã thêm nhân viên: {employee.name}")

    def show_all_salaries(self):
        print("\n--- DANH SÁCH LƯƠNG NHÂN VIÊN ---")
        if not self.employees:
            print("Hiện chưa có nhân viên nào trong hệ thống.")
        for emp in self.employees:
            # Tính đa hình thể hiện ở đây: gọi cùng 1 hàm nhưng kết quả trả về khác nhau tùy loại đối tượng
            salary = emp.calculate_salary()
            print(f"ID: {emp.emp_id} | Tên: {emp.name} | Lương: {salary}")
        print("----------------------------------\n")

system = EmployeeSystem()

while True:
    print("===== MENU QUẢN LÝ NHÂN VIÊN =====")
    print("1. Thêm nhân viên Full-time")
    print("2. Thêm nhân viên Part-time")
    print("3. Hiển thị danh sách và lương")
    print("4. Thoát")
    
    choice = input("Chọn chức năng (1-4): ")

    if choice == '1':
        eid = input("Nhập ID: ")
        name = input("Nhập tên: ")
        salary = float(input("Nhập lương cơ bản: "))
        ft_emp = FullTimeEmployee(eid, name, salary)
        system.add_employee(ft_emp)

    elif choice == '2':
        eid = input("Nhập ID: ")
        name = input("Nhập tên: ")
        hours = float(input("Nhập số giờ làm: "))
        rate = float(input("Nhập mức lương/giờ: "))
        pt_emp = PartTimeEmployee(eid, name, hours, rate)
        system.add_employee(pt_emp)

    elif choice == '3':
        system.show_all_salaries()

    elif choice == '4':
        print("Đang thoát hệ thống...")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")