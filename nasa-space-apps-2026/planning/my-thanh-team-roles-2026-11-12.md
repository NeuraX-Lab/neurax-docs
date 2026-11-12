# Vai trò và bàn giao cho case Mỹ Thành

> 12/11/2026, bản 1.2 theo phân công mới của người dùng. Hưng và Việt cùng đóng góp chính cho team. Hiếu làm backend từ xa, có thời gian offline vì đi Đà Nẵng sáu ngày; chưa có khung online cụ thể. Khả năng tham gia remote theo lời Hiếu, chưa thay xác nhận của BTC. [Hồ sơ đội hình](../../team/team-profile.md).

## 11. Vai trò sáu thành viên và công việc hiện tại

**Hưng và Việt là hai người cùng phụ trách phần đóng góp chính:** cùng làm features, pipeline data, kiến trúc và output cho demo. Hưng xây workflow chính, chốt scope Data -> AI; Việt tập trung technical AI và Data Analysis. Cả hai có thể làm dashboard UI/UX và hỗ trợ backend cho Hiếu.

| Owner / role | Job và đầu ra chính | Bàn giao / phối hợp |
| --- | --- | --- |
| Hưng - workflow chính / scope Data -> AI | Chốt luồng, phạm vi và logic quyết định; cùng Việt làm features, pipeline, kiến trúc và A1; cùng làm dashboard khi cần | Đồng sở hữu core với Việt. Bích review data/feature; Luật kiểm từng block. Không chỉ làm điều phối hoặc pitch |
| Việt - technical AI / Data Analysis | Phân tích dữ liệu, kỹ thuật AI; cùng Hưng làm features, pipeline, kiến trúc và output demo; cùng làm UI/UX và hỗ trợ backend | D1/A1/contract do Hưng-Việt cùng thống nhất. Không là người duy nhất gánh toàn bộ tích hợp |
| Bích - Data / review feature và nguồn | Làm phần Data theo chuyên ngành: rà nguồn, ý nghĩa biến, chất lượng/phạm vi, feature và bảng đất-nước-cây-mùa | Data/evidence + K1: nguồn, phương pháp, giả định, unknown. Bàn giao cho Hưng-Việt; phối hợp Luật, không chỉ góp ý domain |
| Hiếu - Backend, remote gián đoạn | Backend/API/adapter dữ liệu và kết quả trong các khoảng online; ghi cách chạy và bàn giao phần đang làm | Hưng-Việt hỗ trợ/tiếp quản khi Hiếu offline. Không mặc định Hiếu sở hữu toàn bộ UI hoặc có mặt tại venue |
| Tiểu An - demo ESP / sensor | Demo thiết bị, probe, giao tiếp, firmware và log; tích hợp dữ liệu đo lab có nhãn với output demo | H1: raw/timestamp/đơn vị/trạng thái. Luật kiểm; Hưng-Việt nối dashboard. Có nhánh recorded/synthetic đúng nhãn nếu chưa live được |
| Quang Luật - thống kê / đánh giá từng block / QA | Theo dõi từng block của workflow: input/output, thống kê phù hợp, tiêu chí đánh giá, lỗi và trạng thái; hỏi từng người để hiểu luồng và vướng mắc | Q1/E1 + bảng QA theo block: owner, trạng thái, bằng chứng, blocker, việc tiếp theo. Không chỉ QA cuối hoặc kiểm sensor |

**Khi Hiếu offline:** dùng contract và mẫu output đã thống nhất để Hưng-Việt tiếp tục core/UI; backend có hướng dẫn chạy, trạng thái và phần việc dang dở để bàn giao. Không để tích hợp hoặc demo phụ thuộc việc Hiếu trả lời tin nhắn ngay. Nếu cần replay, hiển thị đúng nhãn thay vì giả backend/live data đã sẵn.

**Việc Luật cần nắm:** nguồn data -> tiền xử lý -> features -> AI/so sánh -> backend -> dashboard -> ESP/sensor. “Block” ở đây là khối chức năng trong workflow; không chỉ polygon ruộng. Luật ghi ai đang làm gì, input/output có khớp không và phần nào cần Hưng-Việt quyết định.

**Trước T0:** chuẩn bị/nghiên cứu, xác nhận lịch online và quy định remote/artifact với BTC; chưa triển khai submission project trước giờ cho phép. **Sau T0:** thực hiện các job trên. [GO Team, 05/11/2026](https://github.com/nasa/spaceapps/discussions/1813). Hưng giữ scope; mọi người dùng cùng bảng bằng chứng và contract, không mở thêm địa bàn.
