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

- Các tính năng và mục tiêu đầu vào riêng biệt

 
![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/e762a5a6-532a-40dc-87f3-ed302bb8d367)

Hình 10. Input data

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/a9e44bd5-3348-43ca-9aa0-3e7946f15374)

Hình 11. Output data

## Bước 3: Chọn mô hình ( Choosing model)

### EDA
EDA: Exploratory Data Analysis – Phân tích Khám phá Dữ liệu
- EDA là phương pháp giúp xác định cấu trúc dữ liệu bao gồm số lượng, kiểu dữ liệu, trường dữ liệu, sự liên kết giữa các trường dữ liệu,... Khi xác định được cấu trúc dữ liệu, các nhà phân tích dữ liệu có thể hiểu được mối quan hệ giữa các dữ liệu trong tệp.

- Phân tích tỷ lệ ham - spam

 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/87038eaa-99ee-4286-bf7b-a8818a6b1169)
 
Hình 12. Code phân tích tỷ lệ ham - spam 

--> Kết quả:

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/7a884fb0-899e-4425-8c87-dc6a253834ca)

Hình 13. Biểu tròn thể hiện tỷ lệ ham - spam

- Một số chỉ số thống kê cơ bản

 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/ce43fa2a-998f-4825-a588-1849bd64c650)


 Hình 14. Code thống kê cơ bản

 --> Kết quả:

 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/ad72b202-395b-4778-a3a2-a84e11c8ffbb)

Hình 15. Bảng thống kê cơ bản

- Đo độ dài chuỗi bằng nltk: ( Natural Language Toolkit - xử lý ngôn ngữ tự nhiên thống kê )
 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/1a0c8d70-ec86-4dee-8340-66a8b150d240)

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/ff6db293-d028-4c54-b9d4-458371635aa3)

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/dbc29969-62d4-4b0c-baa9-9728829ff898)

Hình 16. Code đo độ dài chuỗi tròng cột Subjects

--> Kết quả:

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/382569ac-e693-46b1-89c8-7ab45ab98552)

Hình 17. Thể hiện thêm các cột đo độ dài vừa tạo

- Thống kê về spam
 
 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/eec4aeb2-3a7d-4f84-8170-92e41eede939)

 Hình 18. Thống kê cơ bản về spam

 --> Kết quả:
 
 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/aeb2f99f-4842-4022-8373-3ea64d56cb0a)

 Hình 19. Kết quả thống kê về 

 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/945a7039-cb88-4186-aa11-518da9f51a70)

Hình 20. Code heatmap 

--> Kết quả: 

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/80930660-9081-42d5-b4bd-6d0c25d86c5d)

Hình 21. Heatmap 

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/287dda11-38ed-4698-8c86-ed86d35c9b1d)

Hình 22. Code ngôn ngữ tự nhiên

--> Kết quả:

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/0d43b5fb-36b3-43ff-8ce7-01605e71ba82)

Hình 23. Chuỗi ngôn ngữ tự nhiên 

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/6de40f83-d63a-4af9-ba2a-95400b86eb90)

Hình 24. Code chuỗi ký tự đặc biệt

--> Kết quả:

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/b875b32e-72c2-477d-9a7f-ad0a2769acf4)

Hình 25. Chuỗi ký tự đặc biệt

- Tạo hàm chuyển đổi loại bỏ những ký tự đậc biệt

 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/309fde52-b7f5-4ec1-afc5-c0d76fc8e0ad)

 Hình 26. Code tạo hàm chuyển đổi loại bỏ những ký tự đậc biệt

--> Kết quả:

 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/ff798de1-13fc-493a-a055-6d18797ed4f3)

Hình 27. Tạo thêm cột  chứa chuỗi đã được chuyển 
   

- Từ khóa có thể là spam

   ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/92fc8e68-147a-43ec-9907-bab3583c875a)

Hình 29. Code biểu diễn mức độ xuất hiện của các từ có thể là spam

--> Kết quả:
 

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/2d9c66e7-1e22-4c70-b390-7a4fdc82c216)
![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/55217bef-358f-4324-aeb4-ed395ddd2542)

Hình 30.  Biểu đồ biểu diễn mức độ xuất hiện của các từ có thể là spam

 - Từ khóa là ham

 ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/27d86148-cfc9-458c-82bb-5b3f7608626e)

Hình 31. Code biểu diễn mức độ xuất hiện của các từ có thể là ham

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/ee2d517e-a9d0-4351-a79e-bb62638adb78)
![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/20522f90-c953-47bd-b7bb-7c4588ff57dd)

Hình 30.  Biểu đồ biểu diễn mức độ xuất hiện của các từ có thể là 

### NB
NB: Naive Bayes

- Đánh giá ma trận ( Evaluation Matrix)

  ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/04beb03c-c153-486a-8042-3ff199620657)

Hình . Naive Bayes

  ![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/915a75e6-1fae-4aa3-8e57-ccef2a8e8810)

  Hình . Công thức 

### SVM 

SVM: Support Vector Machine

Nguồn: https://machinelearningcoban.com/2017/04/09/smv/

![image](https://github.com/hanlucyen/AI_spam_filter/assets/92861887/f269dedb-74ea-4091-b04a-974dd9d0bbaa)

Hình . Support Vector Machine




