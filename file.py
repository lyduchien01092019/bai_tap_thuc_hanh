#. Viết chương trình Simple Notepad. Yêu cầu người dùng nhập vào một chuỗi ghi 
#chú và lưu nó vào file note.txt. 
# try: 
#     with open('nhat_ky.txt', 'w', encoding='utf-8') as f: 
#         f.write("Hôm nay là một ngày đẹp trời.\n") 
#     with open('nhat_ky.txt', 'r', encoding='utf-8') as f: 
#         print(f.read()) 
# except IOError as e: 
#     print(f"Lỗi file: {e}")

#câu 1
def note():
    a = input("Nhap mot chuoi bat ki: ")
    try:
        with open('notepad.txt', 'w', encoding='utf-8') as f:
            f.write(a)
    except EOFError as e:
        print(f"Lỗi: {e}")        
#câu 2

def output_file():
    try:
        with open('note.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            print("Nội dung file: ",content)
    except FileNotFoundError:
        print("Không tìm thấy file!")     

#câu 3


# bài 1
# a = input("Nhập vào nội dung: ")

# try:
#     # Ghi nội dung vào file
#     with open('note.txt', 'w', encoding='utf-8') as f:
#         f.write(a)

#     # Đọc lại nội dung từ file
#     with open('note.txt', 'r', encoding='utf-8') as f:
#         print("Nội dung trong file:", f.read())

# except IOError as e:
#     print("Lỗi:", e)

# bài 3

try:
    # Nên dùng raw string (r"…") để tránh lỗi ký tự đặc biệt trong đường dẫn
    with open(r"D:\hello.txt", "r", encoding="utf-8") as f:
        content = f.read()              # Đọc toàn bộ nội dung file
        words = content.split()         # Tách nội dung thành danh sách các từ
        print(f"Số từ trong file: {len(words)}")  # In ra tổng số từ
        print(f"Danh sách các từ: {words}")       # (Tuỳ chọn) In ra danh sách từ

except IOError as e:
    print("Lỗi khi đọc file:", e)


# Viết chương trình yêu cầu người dùng nhập vào các con số cho đến khi họ nhập chữ 
#"done". Lưu tất cả các số đã nhập vào file numbers.txt, mỗi số trên một dòng.          

def ghi_so_vao_file():
    with open("numbers.txt", "w", encoding="utf-8") as file:   # mở file
        while True:
            nhap = input("Nhập một số (hoặc gõ 'done' để kết thúc): ") # nhập 
            
            if nhap.lower() == "done":  # nếu nhập bằng lower
                print("Đã kết thúc nhập dữ liệu.")
                break # kết thúc
            
            # Kiểm tra xem người dùng nhập có phải là số không
            try:
                so = float(nhap)  # Dùng float để nhận cả số thập phân
                file.write(f"{so}\n")
            except ValueError:
                print("Giá trị không hợp lệ, vui lòng nhập số hoặc gõ 'done'.")
    try:
        with open("numbers.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except ValueError:
        print("Không thể đọc file")        

#. Viết chương trình đọc file numbers.txt, tính tổng và trung bình cộng của các số trong file đó. 


def read_file_numbers():
    try:
        with open(r"numbers.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            
            numbers = []
            for line in lines:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    pass  # Bỏ qua dòng không hợp lệ

            if not numbers:
                print("File không có số hợp lệ!")
                return

            tong = sum(numbers)
            tb = tong / len(numbers)

            print("Các số trong file:", numbers)
            print("Tổng =", tong)
            print("Trung bình =", tb)

    except FileNotFoundError:
        print("File không tồn tại!")

def copy_file(source_file, destination_file):
    try:
        # Mở file nguồn để đọc
        with open(source_file, "r", encoding="utf-8") as src:
            content = src.read()

        # Mở (hoặc tạo) file đích để ghi
        with open(destination_file, "w", encoding="utf-8") as dest:
            dest.write(content)

        print(f"✅ Sao chép thành công từ '{source_file}' sang '{destination_file}'")

    except FileNotFoundError:
        print(f"❌ Lỗi: File nguồn '{source_file}' không tồn tại!")
    except IOError as e:
        print("❌ Lỗi khi xử lý file:", e)

# 10. Viết chương trình sao chép nội dung từ file này sang file khác. Hàm nhận vào tên 
#file nguồn và tên file đích. 

def copy_file2 (file1, file2):
    try:
        with open(file1, "r", encoding="utf-8") as f1:
            content1 = f1.read()
        with open(file2, "w", encoding="utf-8") as f2:
            f2.write(content1)
        with open(file2, "r", encoding="utf-8") as f2:           
            content2 = f2.read()
        print("Sao chép thành công")
        print("Nội dung file1: ", content1)
        print("Nội dung file2:", content2)
    except FileNotFoundError:
        print("Không tìm thấy file nguồn!")   

if __name__ == "__main__":
    # ghi_so_vao_file()
    # read_file_numbers()
    copy_file2("numbers.txt", "num2.txt")

