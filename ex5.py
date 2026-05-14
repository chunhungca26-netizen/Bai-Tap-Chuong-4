# ==========================================
# 1. MODELS LAYER (Thực thể dữ liệu)
# ==========================================
class Pet:
    def __init__(self, pet_id, name, species, price):
        # Thuộc tính được đóng gói (Private)
        self.__pet_id = pet_id
        self.__name = name
        self.__species = species
        self.__price = price

    # Getters cho các thuộc tính private
    def get_id(self): return self.__pet_id
    def get_name(self): return self.__name
    def get_species(self): return self.__species
    def get_price(self): return self.__price

    def display_info(self):
        print(f"ID: {self.__pet_id} | Tên: {self.__name} | Loài: {self.__species} | Giá: {self.__price}")

# ==========================================
# 2. SERVICES LAYER (Xử lý logic nghiệp vụ)
# ==========================================
class StoreService:
    def __init__(self):
        self.inventory = []  # Mảng quản lý thú cưng
        self.revenue = 0.0   # Quản lý doanh thu

    def add_pet(self, pet):
        self.inventory.append(pet)
        print(f"--- Đã nhập thêm thú cưng: {pet.get_name()} ---")

    def view_inventory(self):
        print("\n--- DANH SÁCH THÚ CƯNG TRONG KHO ---")
        if not self.inventory:
            print("Kho hiện đang trống.")
        for pet in self.inventory:
            pet.display_info()
        print("------------------------------------")

    def sell_pet(self, pet_id):
        # Tìm thú cưng theo ID
        for pet in self.inventory:
            if pet.get_id() == pet_id:
                self.revenue += pet.get_price() # Cộng dồn doanh thu
                self.inventory.remove(pet)      # Xóa khỏi kho
                print(f"--- Bán thành công: {pet.get_name()} | Thu về: {pet.get_price()} ---")
                return True
        
        print(f"--- Lỗi: Không tìm thấy ID {pet_id} trong hệ thống ---")
        return False

    def get_revenue(self):
        return self.revenue

# ==========================================
# 3. VIEWS LAYER (Giao diện người dùng)
# ==========================================
def main():
    service = StoreService()

    while True:
        print("\n===== PET STORE MANAGEMENT MENU =====")
        print("1. Thêm thú cưng mới")
        print("2. Xem danh sách trong kho")
        print("3. Bán thú cưng (Theo ID)")
        print("4. Xem tổng doanh thu")
        print("5. Thoát")
        
        choice = input("Lựa chọn của bạn: ")

        if choice == '1':
            pid = input("Nhập mã ID: ")
            name = input("Nhập tên: ")
            spec = input("Loài (Dog/Cat/Bird...): ")
            price = float(input("Giá bán: "))
            new_pet = Pet(pid, name, spec, price)
            service.add_pet(new_pet)

        elif choice == '2':
            service.view_inventory()

        elif choice == '3':
            pid_to_sell = input("Nhập mã ID thú cưng muốn bán: ")
            service.sell_pet(pid_to_sell)

        elif choice == '4':
            print(f"\n>>> TỔNG DOANH THU HIỆN TẠI: {service.get_revenue()} <<<")

        elif choice == '5':
            print("Cảm ơn bạn. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()