# V4 — reassessment shortlist khi Quang Luật có vai trò DATA QA

> 2026-10-30 · Cập nhật sau khi người dùng cung cấp thế mạnh thật của Quang Luật.
> Bản này điều chỉnh **ba idea** và workflow, không chấm lại cả 14 bằng điểm số. [V3](v3-full-brief-six-members.md) giữ lịch sử rubric/đội hình trước thông tin mới; điểm v3 không phải điểm đã tái đánh giá hôm nay.

## Điều cần sửa trong lập luận cũ

Quang Luật báo thế mạnh thống kê, RStudio/MATLAB, AutoCAD và LaTeX/Overleaf. Giao phần lớn thời gian làm vỏ/cọc/gá chỉ từ ngành Cơ khí là phân công chưa sát. Vai trò chính hiện tại là **QC/EDA, kiểm metric và trực quan hóa/báo cáo khoa học**, hỗ trợ An phân tích phép đo. An vẫn sở hữu hardware.

Công cụ là phương tiện, không ép team deploy R/MATLAB. Quang Luật xuất CSV/JSON/figures và phương pháp; Hiếu dùng cùng artifacts với các block khác.

Người dùng cũng xác nhận **Việt biết cả DATA và AI, có thể làm Technical Lead**. Phân công hiện hành giao Việt kiến trúc/contract, pipeline và module AI; Hưng giữ định hướng/scope và module mô hình còn lại. Đây là thay đổi vai trò, không phải bằng chứng mới về độ sẵn sàng dataset.

## So sánh theo bằng chứng và thời gian

| Tiêu chí | Field Shift | Earth Analog | MODIS/VIIRS |
| --- | --- | --- | --- |
| Đầu ra QA của Quang Luật | Coverage, seasonality, feature correctness, ranking sensitivity | Unit/scale, distance audit, ranking stability | Overlap QC, bias/MAE, temporal split, seasonality |
| Bài toán core | Ra quyết định luân canh có nguồn domain | Analog theo một mục tiêu cụ thể | Hài hòa record và calendar |
| Chỗ dễ tắc | Bảng nông học có nguồn | Feature Earth–planetary so sánh được | Coverage/overlap và khác biệt sampling |
| Baseline nhỏ | Rule + weighted ranking | Weighted scaled distance | Identity rồi correction minh bạch |
| Prediction | Có thể thêm forecast mưa khi đủ lịch sử | Không cần; rank không phải forecast | Forecast activity optional sau harmonization |
| Hardware của An | Node đo + output display | Controller/đo nghiêng minh họa | Display lịch sử/anomaly |
| Phần nên cắt trước | Model phức tạp, actuator, cây/vùng phụ | 3D/global search/rover | Forecast, thêm nhiều platform/AOI |
| Gate chọn | D1 khí hậu và K1 cây/đất đủ căn cứ | D1 có dimensions cùng meaning/scale | D1 có overlap và evaluation khả thi |

**Khuyến nghị có điều kiện:** chuẩn bị Field Shift làm chính; Earth Analog và MODIS/VIIRS làm phương án thay thế. Thế mạnh mới khiến MODIS/VIIRS đáng cân nhắc hơn v3; không còn lý do xem Quang Luật thiếu việc chỉ vì bài ít cần chế tạo.

Không tuyên bố điểm/chênh lệch số khi chưa có sample và thực nghiệm. Nếu T+2 Field Shift thiếu K1 nhưng FIRMS overlap dùng được, ưu tiên MODIS/VIIRS trước việc cố dựng cơ khí. Nếu Earth Analog có cặp data/mục tiêu rõ và team thích bài không gian, chọn Earth Analog; không bắt nó phải có forecast để đủ chữ AI.

## Các thay đổi có thể hành động ngay

- Đọc [ba workflow](../planning/workflows/README.md), chốt một scope, không xây ba nhánh.
- Bích kiểm domain; Việt dẫn kỹ thuật DATA + AI và source mapping; Quang Luật sở hữu Q1/E1 thay vì phụ trách gá.
- Hiếu và An dùng cùng A1 schema từ sớm; thiết bị không là dependency để AI chạy.
- Hưng dùng [lịch HCMC](../planning/event-timeline.md): mốc baseline, integration, nghỉ, local pitch và nộp sớm.
- Quyết định cuối vẫn chưa khóa; ghi vào final-selection khi team thực sự chọn.

Hồ sơ [team](../../team/team-profile.md), [phân công](../planning/team-workstreams.md) và [kiến trúc](../planning/architecture.md) là nguồn hiện hành cho vai trò và handoff.

