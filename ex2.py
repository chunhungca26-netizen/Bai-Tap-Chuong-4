class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        """Khởi tạo tài khoản với tên chủ thẻ và số dư mặc định."""
        self.account_holder = account_holder  # Public
        self.__balance = initial_balance        # Private

    def deposit(self, amount):
        """Nạp tiền vào tài khoản."""
        if amount > 0:
            self.__balance += amount
            print(f"Nạp thành công {amount}. Số dư mới: {self.__balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        """Rút tiền khỏi tài khoản."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Rút thành công {amount}. Số dư còn lại: {self.__balance}")
        else:
            print(f"Rút tiền thất bại! Số dư không đủ hoặc số tiền không hợp lệ.")

    def get_balance(self):
        """Getter để xem số dư (vì __balance là private)."""
        return self.__balance
my_account = BankAccount("Trần Đức Hiếu", 1000)
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(2000) 
print(f"Số dư cuối cùng của {my_account.account_holder}: {my_account.get_balance()}")