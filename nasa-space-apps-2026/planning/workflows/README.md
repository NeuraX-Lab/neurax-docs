# Workflow chính Field Shift và hai phương án dự phòng

> 2026-10-30 · Spec dự kiến cho sự kiện HCMC 14–15/11/2026. Không triển khai ba sản phẩm song song.
> Trạng thái 2026-11-06: Field Shift đã chọn ngày 04/11; Earth Analog và MODIS/VIIRS giữ làm dự phòng. Các spec chưa phải kết quả triển khai.
> Điểm bắt đầu: [team](../team-workstreams.md), [contract D1/Q1/A1/E1/H1](../architecture.md), [lịch và mốc cắt](../event-timeline.md).

## Đầu vào → đầu ra từng block

| Idea | DATA nhận gì? | DATA giao AI — D1 | Baseline AI | AI giao DEPLOY — A1 | DEPLOY |
| --- | --- | --- | --- | --- | --- |
| [Field Shift](field-shift.md) | Climate/EO, đất/cây/mùa, ưu tiên | region-month features + constraints/rotations + QA/provenance | Lọc ràng buộc, utility và weighted ranking | 3 chiến lược, score thành phần, eligibility, evidence, risk; forecast riêng nếu đạt | So luân canh + node context/hiển thị |
| [Earth Analog](earth-analog.md) | Earth/planetary data theo một mục tiêu test | site-feature table cùng unit/method/scale + QA | Weighted distance, similarity, sensitivity | Rank, feature contributions, chỗ giống/khác, missing dimensions | Map Earth + target profile + controller/log thiết bị |
| [MODIS/VIIRS](modis-viirs.md) | Hai sensor có overlap, QA và coverage | cell-month-sensor counts + provenance + split | B0 raw, B1 correction trên train, kiểm heldout | Calendar raw/corrected, source policy, reference index, anomaly | AOI/calendar/CSV + display có timestamp |

Output DATA không phải chỉ là ảnh/chart hoặc “data sạch” chung chung: phải là bảng có grain, unit, keys, metadata và QA pass theo từng feature. Output AI không phải chỉ notebook hay model.pkl: phải có **kết quả để render**, version, bằng chứng và giới hạn.

## Ai đi cùng block nào - hiện hành

- Hưng workflow/scope Data -> AI; Việt technical AI/Data Analysis. **Hưng-Việt cùng core**, features, pipeline, kiến trúc và output demo; cùng UI/UX và hỗ trợ backend khi cần.
- Bích làm Data, review src/features/ý nghĩa và K1; không chỉ góp ý domain.
- Hiếu backend remote gián đoạn, có contract/lệnh chạy/handoff; không mặc định chủ UI hoặc online liên tục.
- An demo ESP/sensor/log; Luật thống kê, đánh giá và QA từng block, hỏi owner để nắm workflow/trạng thái.

[Roles và ranh giới đầy đủ](../my-thanh-team-roles-2026-11-12.md) · [Bắt đầu ở đây](../START-HERE.md). Các bảng ba idea phía trên là tham khảo thiết kế; hiện chỉ Field Shift được chọn.

## Khi chưa có data

1. Viết schema và ví dụ synthetic trong docs; chốt core, QA và phương pháp đánh giá.
2. Khi bắt đầu build trong thời gian được phép, Hiếu/An dùng fixture A1, Hưng/Việt dùng fixture D1/K1; ghi synthetic rõ.
3. Việt tiếp nhận nguồn thật, chỉ thay adapter/metadata; Quang Luật và Bích kiểm trước khi AI nhận.
4. Thay bằng A1 thật cùng schema; vẫn giữ màn hình thiếu dữ liệu/partial.
5. Chưa có data thật đạt yêu cầu thì nói prototype contract, không công bố thành tích khoa học.

## Nên ưu tiên thế nào sau khi biết thế mạnh Quang Luật?

Field Shift vẫn là hướng chuẩn bị sâu vì kết nối quyết định người dùng và hardware tự nhiên. Earth Analog mạnh nếu có cặp dữ liệu tương thích. MODIS/VIIRS được lợi rõ từ khả năng thống kê/QA của Quang Luật và có thể là lựa chọn tốt hơn nếu overlap dễ kiểm còn nông học khó lấy.

[Shortlist v4](../../rankings/v4-data-qa-shortlist.md) ghi thay đổi lý do; không dùng lại điểm v3 như điểm đã chấm theo vai trò mới.

