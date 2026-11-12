# NeuraX — hồ sơ đội hình sáu người

> Phân công hiện hành theo người dùng ngày 12/11: [vai trò, job và bàn giao Mỹ Thành](../nasa-space-apps-2026/planning/my-thanh-team-roles-2026-11-12.md), bản 1.2. **Hưng và Việt cùng đóng góp chính**, cùng features, pipeline data, kiến trúc và output demo. Hiếu backend remote gián đoạn; Hưng-Việt cùng làm UI/UX và hỗ trợ backend khi cần. Trước T0 chỉ chuẩn bị/nghiên cứu trong phạm vi BTC; triển khai submission sau giờ cho phép.

Vai trò bên dưới đã được người dùng làm rõ; năng lực giữ nguồn tự báo cáo/baseline, không phải benchmark. Chưa có giờ online cụ thể của Hiếu hoặc cam kết giờ rảnh từng thành viên.

| Thành viên | Vai trò hiện hành | Năng lực/bằng chứng đã có | Đầu ra sở hữu |
| --- | --- | --- | --- |
| Hưng — Le Nguyen Gia Hung | Workflow chính / scope Data -> AI; cùng Việt đóng góp chính | AI, tối ưu, nghiên cứu theo baseline repo; phân công mới từ người dùng | Workflow, scope; cùng Việt features/pipeline/kiến trúc/A1 và demo; UI/UX/backend support khi cần |
| Việt — Huynh Quoc Viet | Technical AI / Data Analysis; cùng Hưng đóng góp chính | Người dùng xác nhận DATA và AI; ML/data modeling theo baseline | Cùng Hưng features/pipeline/kiến trúc/output demo; kỹ thuật AI và phân tích; UI/UX/backend support |
| Bích — Vo Thi Ngoc Bich | Data / review features và nguồn | Chuyên ngành môi trường; GIS theo baseline | Data/evidence, ý nghĩa/chất lượng/phạm vi nguồn, review feature và K1 đất-cây-nước-mùa |
| Hiếu — Ho Minh Hieu | Backend; remote gián đoạn | Backend/frontend/deploy theo baseline; tự báo bận đi xa, không dự trực tiếp | Backend/API/adapter, cách chạy và handoff; không mặc định giao toàn bộ UI |
| Tiểu An — Nguyen Thanh Hang | Demo ESP / sensor / embedded | Sensing và tích hợp theo baseline | Thiết bị/firmware, H1 log lab, hiển thị và tương tác demo; backup có nhãn |
| Quang Luật | Thống kê từng block / đánh giá / QA workflow | Tự báo RStudio/MATLAB, AutoCAD, LaTeX/Overleaf; cơ khí năm 2 | Q1/E1, thống kê/đánh giá theo block, hỏi owner để nắm luồng/trạng thái/blocker; cùng An kiểm đo |

## Cập nhật từ Quang Luật

Người dùng chuyển lời ngày 2026-10-30: thế mạnh gồm **phân tích thống kê và trực quan hóa dữ liệu với RStudio, MATLAB; AutoCAD; soạn báo cáo khoa học bằng LaTeX/Overleaf**. Tên hiển thị dùng **Quang Luật** trong tài liệu.

Đây là năng lực tự báo cáo, đủ căn cứ để phân công phù hợp; chưa phải benchmark kỹ năng. Quang Luật mới tham gia cuộc thi, không đồng nghĩa mới học thống kê. Chưa xác nhận firmware, robotics, viễn thám chuyên sâu, nông học hay combustion.

Vai trò chính chuyển từ cơ khí chế tạo sang **DATA QA và đánh giá**. AutoCAD là khả năng hỗ trợ khi thực sự cần bản vẽ; không giao mặc định vỏ/cọc/gá. An giữ quyền sở hữu hardware; Quang Luật kiểm log, thiết kế phép đo lặp, tính độ phân tán và so với tham chiếu nếu có.

## Ranh giới để tránh trùng việc

- Hưng-Việt cùng làm pipeline/features/kiến trúc; Bích làm Data và review nguồn/feature. Quang Luật kiểm từng block, thống kê phù hợp và kết quả xuất ra.
- Hưng và Việt cùng làm AI, chia module theo idea: Hưng ưu tiên bài toán/ràng buộc và tiêu chí khoa học; Việt ưu tiên triển khai mô hình và kết nối dữ liệu–inference. Quang Luật kiểm metrics/holdout độc lập.
- Bích quyết định ý nghĩa khoa học/giả định; Quang Luật kiểm số liệu, không thay chuyên gia domain.
- Hiếu phụ trách backend trong các khoảng online; Hưng-Việt có thể làm dashboard UI/UX và hỗ trợ backend. Quang Luật cung cấp chart/bảng số, không bắt runtime demo phụ thuộc RStudio/MATLAB.
- An thiết kế/đọc thiết bị; Quang Luật phân tích chất lượng phép đo; không ôm cả DATA và cơ khí.

Ngân sách công việc đề xuất cho Quang Luật: khoảng 60% QA/thống kê, 25% đánh giá/báo cáo, 15% kiểm thiết bị. Đây là phân bổ công suất, chưa phải giờ rảnh đã xác nhận; ưu tiên DATA khi có xung đột.

## Phần core và phối hợp khi Hiếu offline

Hưng chốt workflow chính và scope Data -> AI; Việt tập trung technical AI và Data Analysis. Hai người cùng sở hữu features, pipeline, kiến trúc và output demo; cùng thống nhất contract và review chéo. Nhãn Technical Lead trong hồ sơ trước không có nghĩa Việt làm một mình hoặc Hưng chỉ điều phối.

Hiếu không dự trực tiếp trong hai ngày thi theo thông tin chuyển lời, làm remote và có lúc không xem tin nhắn; chưa có lịch online cụ thể. Backend cần cách chạy, trạng thái và handoff để Hưng-Việt hỗ trợ khi Hiếu vắng. Khả năng dự remote do Hiếu báo, chưa thay xác nhận BTC. Luật chủ động hỏi từng người, ghi input/output, tiêu chí đánh giá và blocker của từng block; không chỉ kiểm cuối.

## Công cụ và bàn giao

Quang Luật có thể dùng R trong RStudio hoặc MATLAB theo thế mạnh. Chọn một công cụ cho mỗi phân tích; xuất **CSV UTF-8, JSON, SVG/PNG và ghi phương pháp**. Không cần viết lại cùng một phép tính trên cả hai môi trường. Runtime demo không phụ thuộc giấy phép MATLAB hay phiên đăng nhập Overleaf.

LaTeX/Overleaf phục vụ báo cáo khoa học; Markdown trong repo giữ quyết định và phương pháp nguồn. Báo cáo là đầu ra xuất bản từ một bộ nội dung, tránh hai bản phương pháp khác nhau.

## Cách chọn challenge

Cả sáu người cần có đầu ra hữu ích. Luật không cần chế tạo để có đất diễn: QA, trực quan hóa, so baseline và kiểm thiết bị đều có thể ảnh hưởng trực tiếp đến kết quả. Những năng lực chưa có bằng chứng vẫn được ghi là cần kiểm.

Đọc [phân công](../nasa-space-apps-2026/planning/team-workstreams.md), [shortlist cập nhật](../nasa-space-apps-2026/rankings/v4-data-qa-shortlist.md) và [lịch sự kiện](../nasa-space-apps-2026/planning/event-timeline.md).
