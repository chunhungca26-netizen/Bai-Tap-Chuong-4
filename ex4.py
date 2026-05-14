# --- 1. Lớp Book (Entity) ---
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Available"  # Trạng thái mặc định

    def display_info(self):
        """In thông tin chi tiết của sách."""
        print(f"[{self.book_id}] - Tên sách: {self.title}")
        print(f"    Tác giả: {self.author} | Trạng thái: {self.status}")
        print("-" * 30)

# --- 2. Lớp LibraryManager (System Management) ---
class LibraryManager:
    def __init__(self):
        self.book_list = []

    def add_book(self, new_book):
        """Thêm một đối tượng Book vào danh sách."""
        self.book_list.append(new_book)
        print(f"Đã thêm sách: {new_book.title} thành công!")

    def display_all(self):
        """Hiển thị toàn bộ sách trong thư viện."""
        print("\n===== DANH SÁCH SÁCH TRONG THƯ VIỆN =====")
        if not self.book_list:
            print("Thư viện hiện đang trống.")
        for book in self.book_list:
            book.display_info()

    def borrow_book(self, book_id):
        """Tìm sách theo ID và đổi trạng thái sang Borrowed."""
        for book in self.book_list:
            if book.book_id == book_id:
                if book.status == "Available":
                    book.status = "Borrowed"
                    print(f"Bạn đã mượn thành công cuốn: {book.title}")
                    return
                else:
                    print(f"Lỗi: Cuốn sách '{book.title}' đã có người mượn rồi.")
                    return
        
        print(f"Lỗi: Không tìm thấy sách có mã ID: {book_id}")

# --- 3. Hàm main() và Menu tương tác ---
def main():
    manager = LibraryManager()

    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ THƯ VIỆN ---")
        print("1. Thêm sách mới")
        print("2. Hiển thị tất cả sách")
        print("3. Mượn sách")
        print("4. Thoát")
        
        choice = input("Nhập lựa chọn của bạn (1-4): ")

        if choice == '1':
            bid = input("Nhập mã ID sách: ")
            title = input("Nhập tên sách: ")
            author = input("Nhập tên tác giả: ")
            new_book = Book(bid, title, author)
            manager.add_book(new_book)

        elif choice == '2':
            manager.display_all()

        elif choice == '3':
            bid_to_borrow = input("Nhập mã ID sách muốn mượn: ")
            manager.borrow_book(bid_to_borrow)

        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()