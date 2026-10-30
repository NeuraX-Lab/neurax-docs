# Đề xuất chọn challenge — Field Shift / NeuraX AgroTwin

> 2026-10-30 · **Khuyến nghị, chưa phải team đã chốt.**
> Căn cứ: [brief chi tiết](challenges/07-field-shift.md), [đội hình sáu người](../team/team-profile.md) và [shortlist v4](rankings/v4-data-qa-shortlist.md).

## Vấn đề và người dùng

Nông dân hoặc người tư vấn cần so luân canh khi điều kiện nước/nhiệt thay đổi, nhưng dữ liệu vệ tinh, đất, cây và ưu tiên thường tách rời. Concept giúp xem **luân canh nào hợp với ràng buộc và ưu tiên, bằng chứng nào hỗ trợ, chỗ nào chưa đủ thông tin**.

Địa phương/cây mục tiêu chưa chốt: Bích chọn một vùng và bảng đất/cây có nguồn trước khi team tuyên bố phương án phù hợp thực tế. Người dùng mục tiêu là giả thuyết cần kiểm, chưa có phỏng vấn nông dân.

[Link challenge ứng viên](https://www.spaceappschallenge.org/2026/challenges/field-shift-adapting-farms-with-nasa-data/) đã được thử truy cập nhưng trả lỗi; nội dung đánh giá dựa trên bản người dùng cung cấp.

## Vì sao nên chọn

- NASA EO là căn cứ lịch sử điều kiện môi trường, không chỉ là ảnh nền.
- Việt là Technical Lead, làm DATA và AI: kiến trúc/contract, EO features và baseline forecast có điều kiện. Hưng phụ trách ranking/ràng buộc và scope; Quang Luật kiểm QA/metrics độc lập và báo cáo.
- Bích tham gia trực tiếp vào tính đúng của cây–đất–mùa và diễn giải; kiến thức môi trường vẫn cần nguồn nông học chuyên biệt.
- Hiếu có demo rõ: chọn vùng/ưu tiên → so chiến lược → xem lý do.
- An có node đo, QA, truyền và hiển thị kết quả.
- Quang Luật dùng thống kê, RStudio/MATLAB và LaTeX/Overleaf cho QA, trực quan hóa, đánh giá/báo cáo; hỗ trợ An kiểm log. AutoCAD chỉ dùng nếu có nhu cầu thiết bị thực.

## Dữ liệu dự kiến

| Nguồn | Vai trò | Mức xác nhận | Còn phải kiểm |
| --- | --- | --- | --- |
| NASA POWER | Lịch sử khí hậu cho vùng mẫu | Đề nhắc tên; đã đọc [API overview](https://power.larc.nasa.gov/docs/services/api/) | Parameter, product/version, resolution, period, QA, access và sample |
| GPM hoặc SMAP | Thêm precipitation/soil-moisture context nếu cần | Đề nhắc tên, chưa chốt product | Coverage, units, scale, missingness và cách aggregate |
| Bảng đất/cây/mùa địa phương | Ràng buộc luân canh và giải thích | Chưa có bảng được rà | Nguồn, quyền dùng, mùa vụ, pest/market/water constraints |
| Node tại chỗ | Bối cảnh điểm đo và demo tích hợp | BOM đề xuất, chưa đo | Module, calibration, tọa độ context, quality và timestamp |

Chọn 1–2 nguồn NASA phù hợp; không tích hợp mọi mission trong đề. Không biến node demo thành xác thực mọi pixel; không nói đất khỏe chỉ vì sensor ẩm.

Workflow vận hành mới: [Field Shift](planning/workflows/field-shift.md). Lịch HCMC 14–15/11/2026 và các giờ còn chờ xác nhận: [event-timeline](planning/event-timeline.md).

## Sản phẩm nhỏ nhất

1. Chọn một vùng và luân canh hiện tại.
2. Đọc lịch sử climate/EO với nguồn, đơn vị và thời gian.
3. Nhập ưu tiên nước/đất và ràng buộc cây.
4. So 3 chiến lược gồm hiện trạng, trình bày evidence, risk và missing information.
5. Thay một giả định khí hậu để xem scenario khác; tách khỏi forecast.
6. Nhận log node vào một khung context riêng, hiển thị kết quả trên dashboard/thiết bị.
7. Kết thúc bằng điều cần kiểm tại địa phương, thay vì khẳng định một lựa chọn đúng tuyệt đối.

Ba chiến lược là acceptance criterion NeuraX chọn từ gợi ý “may” của brief. Demo 2–3 phút là mục tiêu nội bộ, không phải giới hạn nộp đã xác minh.

## AI và kiểm chứng

Baseline: scoring có ràng buộc và giải thích, tính feature từ dữ liệu có QA. Forecast đề xuất cho một chỉ số stress khí hậu: chỉ giữ khi có target/horizon rõ, split theo thời gian, so seasonal-naive và công bố lỗi ngoài mẫu. Không dự báo năng suất/thu nhập khi thiếu nhãn; không coi scenario sliders là prediction đã được kiểm chứng.

Thành công MVP: một luồng truy được nguồn, chiến lược không vi phạm ràng buộc đã công khai, đổi ưu tiên có giải thích, missing/stale hiện rõ, và demo chạy được với snapshot đúng nhãn. Thử node xác minh tích hợp/độ lặp tương đối, không là thẩm định nông học.

## Phạm vi cắt

Một vùng, ít cây/mùa, dashboard và một node. Chưa có autonomous irrigation, custom chip/PCB, rover, mô hình nền huấn luyện mới, cam kết năng suất hoặc coverage toàn cầu. Hardware và prediction có gate riêng; NASA-data analysis vẫn phải hoàn chỉnh.

## Đất diễn và kiến trúc

[Phân công sáu thành viên](planning/team-workstreams.md) chứa owner, reviewer, dependency và onboarding. [Kiến trúc](planning/architecture.md) chứa Mermaid, contract và fallback. [Hardware preparation](planning/hardware-preparation.md) là danh sách An–Quang Luật kiểm/mượn/mua sau khi biết inventory/ngân sách.

## Quyết định còn mở

| Trường | Trạng thái |
| --- | --- |
| Challenge được khuyến nghị | Field Shift |
| Ngày đề xuất | 2026-10-30 |
| Người quyết định cuối | Team NeuraX, Hưng tổng hợp |
| Challenge team đã chốt | Chưa xác nhận |
| Ngày chốt | Chưa xác nhận |
| Gate trước khi build | G1–G6 trong v3 còn là checklist tham chiếu; lịch ngày thi đã xác nhận, giờ local và gate dữ liệu chưa hoàn tất; xem v4/timeline |
| Điểm khác biệt đề xuất | So luân canh có evidence/uncertainty và context điểm đo; chưa xác minh khác biệt so đối thủ |
| Rủi ro chính | Dữ liệu nông học và diễn giải sai scale |
| Fallback ưu tiên | Earth Analog nếu dữ liệu so sánh/mục tiêu test tốt; MODIS/VIIRS nếu overlap khả dụng |

Không chuyển trạng thái thành “approved/selected” chỉ vì đã có tài liệu. Cập nhật bảng này và decision-log khi team thực sự chọn; sau đó triển khai trong repo sản phẩm theo scope được giao.
