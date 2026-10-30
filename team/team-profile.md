# NeuraX — hồ sơ đội hình sáu người

> Cập nhật 2026-10-30. Vai trò là phân công đề xuất, chưa phải cam kết thời gian của từng thành viên.

| Thành viên | Vai trò chính đề xuất | Năng lực/bằng chứng hiện có | Đầu ra sở hữu |
| --- | --- | --- | --- |
| Hưng — Le Nguyen Gia Hung | AI / Team Owner | AI, tối ưu, nghiên cứu theo baseline repo | Baseline, mô hình quyết định, scope và tích hợp khoa học |
| **Việt — Huynh Quoc Viet** | **Technical Lead / DATA + AI** | Người dùng xác nhận biết xử lý DATA và làm AI; ML/data modeling theo baseline repo | Kiến trúc/contract, pipeline dữ liệu, module AI theo idea, review và gỡ vướng tích hợp |
| Bích — Vo Thi Ngoc Bich | Domain / Environmental Science | Môi trường, GIS theo baseline repo | Định nghĩa biến, nguồn domain, giả định, kiểm tính hợp lý |
| Hiếu — Ho Minh Hieu | Software / DEPLOY | Backend, frontend và deployment theo baseline repo | Contract tích hợp, dashboard, đóng gói demo |
| Tiểu An — Nguyen Thanh Hang | Hardware / Embedded | Sensing và tích hợp thiết bị theo baseline repo | Board, wiring, firmware, log, kết nối và hiển thị |
| **Quang Luật** | **DATA QA / thống kê / đánh giá** | Sinh viên Cơ khí năm 2; tự báo cáo phân tích thống kê, trực quan hóa với RStudio/MATLAB, AutoCAD, LaTeX/Overleaf | Báo cáo QA, kiểm thống kê độc lập, biểu đồ và báo cáo khoa học; cùng An kiểm thiết bị |

## Cập nhật từ Quang Luật

Người dùng chuyển lời ngày 2026-10-30: thế mạnh gồm **phân tích thống kê và trực quan hóa dữ liệu với RStudio, MATLAB; AutoCAD; soạn báo cáo khoa học bằng LaTeX/Overleaf**. Tên hiển thị dùng **Quang Luật** trong tài liệu.

Đây là năng lực tự báo cáo, đủ căn cứ để phân công phù hợp; chưa phải benchmark kỹ năng. Quang Luật mới tham gia cuộc thi, không đồng nghĩa mới học thống kê. Chưa xác nhận firmware, robotics, viễn thám chuyên sâu, nông học hay combustion.

Vai trò chính chuyển từ cơ khí chế tạo sang **DATA QA và đánh giá**. AutoCAD là khả năng hỗ trợ khi thực sự cần bản vẽ; không giao mặc định vỏ/cọc/gá. An giữ quyền sở hữu hardware; Quang Luật kiểm log, thiết kế phép đo lặp, tính độ phân tán và so với tham chiếu nếu có.

## Ranh giới để tránh trùng việc

- Việt làm pipeline tạo dữ liệu; Quang Luật kiểm một mẫu độc lập, missingness, đơn vị, thống kê và kết quả xuất ra.
- Hưng và Việt cùng làm AI, chia module theo idea: Hưng ưu tiên bài toán/ràng buộc và tiêu chí khoa học; Việt ưu tiên triển khai mô hình và kết nối dữ liệu–inference. Quang Luật kiểm metrics/holdout độc lập.
- Bích quyết định ý nghĩa khoa học/giả định; Quang Luật kiểm số liệu, không thay chuyên gia domain.
- Hiếu làm giao diện; Quang Luật cung cấp chart specification và bảng số, không bắt Hiếu nhúng RStudio/MATLAB vào sản phẩm.
- An thiết kế/đọc thiết bị; Quang Luật phân tích chất lượng phép đo; không ôm cả DATA và cơ khí.

Ngân sách công việc đề xuất cho Quang Luật: khoảng 60% QA/thống kê, 25% đánh giá/báo cáo, 15% kiểm thiết bị. Đây là phân bổ công suất, chưa phải giờ rảnh đã xác nhận; ưu tiên DATA khi có xung đột.

## Technical Lead không có nghĩa làm mọi thứ

Việt chốt kiến trúc, schema, lựa chọn kỹ thuật và điều phối integration; Hưng chốt mục tiêu, ưu tiên, scope, tiêu chí đánh giá và quyết định chọn bài cùng team. Hiếu vẫn sở hữu dashboard/deployment, An sở hữu embedded, Quang Luật sở hữu QA/E1. Việt có đầu việc AI thực trong từng workflow, không chỉ hỗ trợ khi rảnh.

Review kỹ thuật theo mốc T+2/T+6/T+12, không yêu cầu Việt duyệt mọi chỉnh sửa nhỏ. Nếu ingestion kéo dài, Hưng nhận phần model của Việt để bảo vệ đường găng; Việt không gánh thêm tất cả test/UI/hardware.

## Công cụ và bàn giao

Quang Luật có thể dùng R trong RStudio hoặc MATLAB theo thế mạnh. Chọn một công cụ cho mỗi phân tích; xuất **CSV UTF-8, JSON, SVG/PNG và ghi phương pháp**. Không cần viết lại cùng một phép tính trên cả hai môi trường. Runtime demo không phụ thuộc giấy phép MATLAB hay phiên đăng nhập Overleaf.

LaTeX/Overleaf phục vụ báo cáo khoa học; Markdown trong repo giữ quyết định và phương pháp nguồn. Báo cáo là đầu ra xuất bản từ một bộ nội dung, tránh hai bản phương pháp khác nhau.

## Cách chọn challenge

Cả sáu người cần có đầu ra hữu ích. Luật không cần chế tạo để có đất diễn: QA, trực quan hóa, so baseline và kiểm thiết bị đều có thể ảnh hưởng trực tiếp đến kết quả. Những năng lực chưa có bằng chứng vẫn được ghi là cần kiểm.

Đọc [phân công](../nasa-space-apps-2026/planning/team-workstreams.md), [shortlist cập nhật](../nasa-space-apps-2026/rankings/v4-data-qa-shortlist.md) và [lịch sự kiện](../nasa-space-apps-2026/planning/event-timeline.md).
