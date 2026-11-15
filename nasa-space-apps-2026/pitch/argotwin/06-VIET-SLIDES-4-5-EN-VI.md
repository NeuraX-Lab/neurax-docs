# Việt — kịch bản bám slide 4–5, tối đa mục tiêu 75 giây

Đã đối chiếu trực tiếp hình slide 4 và 5 hiện hành. Chỉ nói nội dung có trên hai trang. Chọn một ngôn ngữ để thuyết trình, không đọc hai bản nối tiếp.

Phân bổ: **slide 4: 0–35 giây; slide 5: 35–72 giây; chuyển sang Hưng trước giây 75.** Các khoảng là mốc tập nói, chưa phải thời lượng đo từ giọng của Việt. Đọc rõ khoảng 140–150 từ tiếng Anh/phút; dành vài giây chỉ vào visual. Các số thập phân và tên thuật toán cần tập trước, không đọc vội để chạy giờ.

## English — slide 4, 0–35s

NASA POWER provides rainfall, temperature and humidity across 514 months, from 1984 to October 2026. We check units, missing days and the calendar, then fit same-month historical averages. These are regional estimates; drainage and salinity need local information. The December rainfall estimate is 33.68 millimetres, ranging from zero to 93.27. Nominal coverage is 80 percent; diagnostic rainfall coverage was 67.7 percent.

## English — slide 5, 35–72s

Here, the climate branch feeds the decision layer. The second branch searches seventeen bilingual evidence cards using BM25 and character TF-IDF, checks support and source hashes, then returns a cited answer or refusal. Farm constraints also enter the decision layer. The local API returns options and citations; the dashboard is pending. In the example, poor drainage conflicts with the mungbean guideline, so mungbean is blocked. Hưng will continue.

## Tiếng Việt — slide 4, 0–35 giây

NASA POWER cung cấp mưa, nhiệt độ và độ ẩm trong 514 tháng, từ năm 1984 đến tháng 10 năm 2026. Chúng tôi kiểm đơn vị, ngày thiếu và lịch, rồi tính trung bình lịch sử theo cùng tháng. Đây là ước tính vùng; thoát nước và độ mặn cần thông tin địa phương. Ước tính mưa tháng 12 là 33,68 milimét, với khoảng từ 0 đến 93,27. Độ bao phủ mục tiêu là 80%; độ bao phủ mưa trong đánh giá đạt 67,7%.

## Tiếng Việt — slide 5, 35–72 giây

Nhánh khí hậu đưa kết quả vào tầng quyết định. Nhánh còn lại tìm trong 17 thẻ bằng chứng song ngữ bằng BM25 và TF-IDF theo ký tự, kiểm mức hỗ trợ và hash nguồn, rồi trả câu có trích dẫn hoặc từ chối. Các ràng buộc ruộng cũng đi vào tầng quyết định. API trả phương án và trích dẫn; dashboard đang chờ cập nhật. Trong ví dụ, thoát nước kém xung đột với quy trình đậu xanh, nên phương án đậu xanh bị chặn. Mời Hưng trình bày tiếp.

## Chỉ theo visual, không thêm lời ngoài slide

| Mốc | Chỉ vào đâu | Nội dung lời nói |
|---|---|---|
| 0–10s | 514 và ba biến khí hậu | Nguồn NASA POWER, khoảng thời gian |
| 10–19s | Flow căn giữa bên trái và ô thông tin vùng | Kiểm dữ liệu, trung bình cùng tháng, giới hạn địa phương |
| 19–35s | Khối seasonal baseline dưới biểu đồ mưa | 33.68, khoảng 0–93.27, nominal 80% và diagnostic 67.7% |
| 35–54s | Hai nhánh và dòng RAG method | Climate, 17 cards, hybrid search, checks, cited answer/refusal |
| 54–62s | Decision layer, Local API, Dashboard UI | Farm constraints, outputs, UI pending |
| 62–72s | Ba ô worked example | Poor drainage → guideline → mungbean blocked, chuyển Hưng |
| 72–75s | Chuyển người nói | Dự phòng ngắt câu, chuyển slide |

Nếu tập thực tế bị trễ, bỏ câu “The local API returns options and citations; the dashboard is pending.” / “API trả phương án và trích dẫn; dashboard đang chờ cập nhật.” để lấy lại vài giây. Không cắt số liệu coverage vì 80% không phải accuracy.

Bản này không thêm farmer benefits, yield, forecast superiority, live demo hoặc kết quả không xuất hiện trên slide. Bản Việt dùng “độ bao phủ” cho coverage; không đổi thành “độ chính xác”.
