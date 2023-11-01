# AI_spam_filter
EDA_NB_SVM

# Thư rác ( Spam)
Định nghĩa: 
- Thư rác là các tin nhắn không liên quan hoặc không phù hợp được gửi trên internet tới một số lượng lớn người.

- Gửi thư rác là hành động lan truyền không được yêu cầu và không liên quan nội dung, đã được quan sát thấy trong một số lĩnh vực khác nhau như email, tin nhắn tức thời, trang web, điện thoại có kết nối Internet.(M. Sahami, S. Dumais, D. Heckerman, and E. Horvitz, "A Bayesian Approach to Filtering Junk E-Mail," in Learning for Text Categorization: Papers from the 1998 Workshop, 1998. - P. So Young, K. Jeong Tae, and K. Shin Gak, "Analysis of applicability of traditional spam regulations to VoIP spam," in Advanced Communication Technology, 2006. ICACT 2006. The 8th International Conference, 2006, pp. 3 pp.-1217.).

# Cách thức hoạt động của bộ lọc thư rác
Bộ lọc thư rác hoạt động bằng cách phân tích thư trước khi được đưa vào hộp thư đến của người dùng nhằm kiểm tra xem có phải thư rác hay không. Bộ lọc này phân tích nội dung, địa chỉ gửi thư, đầu thư (header), các tệp đính kèm, ngôn ngữ và các dấu hiệu khả nghi khác.

Có nhiều phương pháp phân loại thư rác, trong đó quy trình lọc thư rác tiêu chuẩn bao gồm những thành phần sau [2]:

- Lọc nội dung (content filter): phân loại thư rác dựa trên nội dung thư bằng các phương pháp như: thống kê truyền thống, học máy...;

- Lọc đầu thư (header filter): trích xuất thông tin từ đầu thư để lọc;

- Lọc theo danh sách đen (blacklist filter): xác định thư rác và địa chỉ thư gửi thư rác từ danh sách đen;

- Lọc dựa trên quy luật (rule-based filter): nhận diện người gửi cụ thể qua đầu thư sử dụng các tiêu chí do người dùng đặt ra;

- Lọc bằng cấp quyền (permission filter): gửi thư bằng cách có sự đồng ý của người nhận từ trước;

- Lọc nhờ xác thực bằng cách trả lời (challenge-response filter): kiểm tra thư được gửi tự động hay do người trực tiếp gửi (thông thường thư rác đều được tạo và gửi tự động thông qua phần mềm) qua việc người gửi trả lời để xác thực.
 
![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/c1262f0f-4a78-41f4-8552-ad73bff88e65)

Hình 1. Quy trình lọc thư rác tiêu chuẩn.

# Thủ tục của dự án Máy học ( Procedure of Machine Learning project)
![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/d0f41b4f-e391-44cd-a766-419bf442db52)

Hình 2. Thủ tục thực hiện tổng quát

## Bước 1: Chọn dữ liệu ( Collecting data)
- Gọi các thư viện cần thiết ( Import required libraries)

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/be84130c-e35b-4309-a17d-0d78ad815533)

Hình 3. Các thư viện  

## Bước 2: Chuẩn bị dữ liệu ( Preparing data)
- Mở tệp chứa dữ liệu spam_ham_dataset.csv ( load file )
- ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/abc3e1ee-bf03-49f4-a113-e7bda34a3084)

Hình 4. Hình code mở tệp chứa dữ liệu

--> Kết quả: 

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/53733f77-2c5a-44f9-a6bd-6f6016fa644a)

Hình 5. Mở tệp

Mô tả bộ dữ liệu có 5171 hàng và 4 cột:
 + Cột 1: Trống tên cột: chứa các số được sắp xếp cho tệp dữ liệu là duy nhất.
 + Cột 2: label là nhãn đánh dấu các ham-spam.
 + Cột 3: text là chuỗi ký tự.
 + Cột 4: label_num là cột mã hóa giá trị của ham thành 0 và spam thành 1.
 
- Biến đổi dữ liệu ( Convert it to a data frame)
 + Thêm tên cho cột bị trống
  ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/7fa3b045-82e0-41f2-8154-30c72ef4c04e)

Hình 6. Code thêm tên cho cột bị trống

--> Kết quả:

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/fd8f7978-9bad-480a-a648-717893d9f600)

Hình 7. Thêm tên cho cột

 + Tạo hàm loại bỏ ký tự Supject đứng đầu các chuỗi trong cột text

 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/0e915b9b-189f-41b2-8841-3729e722c2c3)

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/b3f95e89-65c9-4e6c-bbb3-24600acbc5d6)

Hình 8. Tạo hàm loại bỏ ký tự

--> Kết quả: 

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/51ab7d84-a5c6-4091-b8be-97619e0add41)

Hình 9. Thêm cột  Subject chứa chuỗi ký tự



