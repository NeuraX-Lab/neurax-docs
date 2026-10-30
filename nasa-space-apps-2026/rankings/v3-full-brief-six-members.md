# Xếp hạng v3 — 14 đề chi tiết, đội hình sáu người

> **Snapshot lịch sử trước khi biết thế mạnh Quang Luật.** [V4](v4-data-qa-shortlist.md) cập nhật ba idea theo vai trò DATA QA, thống kê và báo cáo; các giả định cơ khí/CAD cùng điểm v3 bên dưới không phải đánh giá hiện hành. [Timeline](../planning/event-timeline.md) thay giả định lịch cũ.

> 2026-10-30 · Đề xuất của trợ lý cho team, chưa phải quyết định tập thể.
> Thay v2 cho việc ra quyết định hiện tại; v1/v2 giữ nguyên lịch sử. Căn cứ nội dung là bản `docs/challenges.md` do người dùng cung cấp; Resources và sample datasets chưa được kiểm chứng đầy đủ.

## Khuyến nghị

**Chọn Field Shift để chuẩn bị sâu; Earth Analog là phương án thay thế ưu tiên, MODIS/VIIRS là lựa chọn thứ ba.** Field Shift có vòng công việc liền mạch cho sáu người: dữ liệu và domain → phân tích luân canh/dự báo có kiểm chứng → dashboard và node đo. Vai trò Quang Luật là cơ khí và phép thử có hướng dẫn, không mặc định một chuyên gia mô phỏng mới gia nhập.

Đây là khuyến nghị dựa trên độ phù hợp, không phải xác nhận data đã sẵn sàng hay đảm bảo giải thưởng. Nếu không có bảng đất/cây và nguồn nông học đủ tốt, Field Shift mất lợi thế. Earth Analog có thể vượt lên nếu lấy được dữ liệu Earth–Moon/Mars tương thích và xác định mục tiêu thử thiết bị.

## Cách chấm để team có thể sửa lại

Thang 1–5: 1 = thiếu năng lực/đầu ra khó phù hợp; 3 = làm được nếu thu hẹp, còn khoảng trống; 5 = rất phù hợp với brief và đội hình. Điểm 2/4 là mức trung gian. Các điểm là nhận định nội bộ, không phải kết quả benchmark hoặc điểm NASA.

| Mã | Tiêu chí | Trọng số |
| --- | --- | ---: |
| T | Sáu thành viên có đầu ra tự nhiên, kể cả người mới | 25% |
| C | Bám yêu cầu cốt lõi và vai trò dữ liệu NASA | 20% |
| F | Khả năng MVP trong 48 giờ giả định và mức khó dữ liệu/domain | 20% |
| A | Giá trị analysis, prediction hoặc tối ưu có kiểm chứng | 15% |
| H | Hardware/cơ khí tạo giá trị sử dụng thực | 10% |
| D | Demo dễ hiểu và quyết định có ý nghĩa | 10% |

**Tổng /100 = (25T + 20C + 20F + 15A + 10H + 10D) / 5.**
C là độ phù hợp tiềm năng với core, không chấm tình trạng truy cập dữ liệu. A không thưởng việc gắn ML tùy tiện; hình học và thống kê có thể giải quyết bài tốt hơn ML. Các gate dưới bảng quan trọng hơn điểm tổng.

| Hạng | Challenge | T | C | F | A | H | D | Tổng | Lý do chính |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | [07 — field-shift](../challenges/07-field-shift.md) | 5 | 5 | 3 | 5 | 5 | 5 | 92 | Luân canh, NASA EO và đo tại chỗ tạo sáu đầu ra tự nhiên; nông học là gate. |
| 2 | [10 — earth-analogs-moon-mars](../challenges/10-earth-analogs-moon-mars.md) | 5 | 5 | 2 | 4 | 5 | 5 | 85 | Cơ khí/embedded có mục tiêu thử thiết bị rõ; khó ghép dữ liệu liên hành tinh. |
| 3 | [09 — modis-viirs-hot-spots](../challenges/09-modis-viirs-hot-spots.md) | 4 | 5 | 4 | 5 | 2 | 4 | 83 | Core và baseline đo được; hardware/cơ khí ít trung tâm. |
| 4 | [11 — martian-map](../challenges/11-martian-map.md) | 4 | 5 | 3 | 4 | 4 | 5 | 82 | Route/map và fixture hợp team; dữ liệu Marswalk chi tiết là rủi ro. |
| 5 | [08 — flame-in-freefall](../challenges/08-flame-in-freefall.md) | 4 | 5 | 3 | 5 | 2 | 4 | 79 | Core AI tri thức rõ; domain cháy vẫn thiếu người kiểm chuyên sâu. |
| 6 | [02 — earth-system-trend-detective](../challenges/02-earth-system-trend-detective.md) | 3 | 5 | 4 | 5 | 1 | 4 | 76 | Baseline thống kê mạnh; không cần hardware và prediction. |
| 7 | [04 — clps-lunar-mission-browser](../challenges/04-clps-lunar-mission-browser.md) | 4 | 5 | 2 | 3 | 4 | 5 | 75 | An–Quang Luật có mô hình cơ khí, nhưng ephemeris/horizon phức tạp. |
| 8 | [06 — dancing-with-the-sars](../challenges/06-dancing-with-the-sars.md) | 4 | 5 | 2 | 4 | 2 | 5 | 74 | NISAR là gate cứng; xử lý SAR có thể chặn toàn bộ MVP. |
| 9 | [03 — junior-astronaut-mission-trainer](../challenges/03-junior-astronaut-mission-trainer.md) | 4 | 3 | 4 | 2 | 4 | 5 | 72 | Game trade-off cho trẻ rõ; prediction khoa học không phải trọng tâm. |
| 10 | [13 — space-mission-design-game](../challenges/13-space-mission-design-game.md) | 4 | 3 | 3 | 3 | 4 | 5 | 71 | Thiết kế module hợp cơ khí; game và cân bằng dễ phình phạm vi. |
| 11 | [14 — earth-information-jukebox](../challenges/14-earth-information-jukebox.md) | 3 | 4 | 4 | 2 | 4 | 5 | 71 | Tactile/audio có đất diễn; thiếu kinh nghiệm audio đã xác nhận. |
| 12 | [05 — astronaut-health-monitoring](../challenges/05-astronaut-health-monitoring.md) | 4 | 4 | 1 | 3 | 4 | 4 | 65 | Sensor/AI hợp nhưng thiếu dữ liệu và chuyên môn y tế để kiểm nội dung. |
| 13 | [12 — planet-x-spherex](../challenges/12-planet-x-spherex.md) | 2 | 5 | 2 | 4 | 1 | 4 | 60 | Core data rõ, nhưng WCS/astronomy và multi-epoch là rủi ro. |
| 14 | [01 — abandoned-but-not-forgotten](../challenges/01-abandoned-but-not-forgotten.md) | 2 | 3 | 5 | 1 | 2 | 4 | 57 | MVP kể chuyện khả thi, không hợp mong muốn prediction/environment. |

Game Design và Jukebox bằng điểm: tạm ưu tiên Game Design vì phần cơ khí của Quang Luật gắn trực tiếp hơn với cấu trúc/module; đây không phải khác biệt có ý nghĩa thống kê. Chỉ đổi F một mức đã đổi 4 điểm, nên chênh lệch nhỏ không đáng coi là thứ hạng chắc chắn.

## Điều đã thay đổi so với v2

- Quang Luật bổ sung góc nhìn cơ khí và tính lặp lại phép đo, nhưng chưa có căn cứ nâng năng lực CAD/robotics/combustion lên mức thành thạo.
- Field Shift đã nêu nhiều dataset và gợi ý so 3 luân canh, ưu tiên nông dân, bằng chứng và uncertainty: hỗ trợ concept AgroTwin, không chứng minh mô hình năng suất.
- Earth Analog nhấn mạnh analog không cần giống mọi chiều và phải nói rõ chỗ khác: phù hợp hơn với một mục tiêu test thiết bị hẹp.
- Martian Map có cửa cho map tĩnh và ba loại dữ liệu là gợi ý; không cần làm công cụ điều hướng đạt chuẩn bay.
- Flame in Freefall có core dashboard SI/ranking rõ; phần cứng không cần thực nghiệm đốt. Vị trí tăng nhờ brief rõ hơn và góc đọc apparatus, không phải vì Quang Luật đã biết combustion.
- NISAR phải là nguồn trung tâm của SAR. Chưa có data analysis-ready là lý do F thấp.
- Planet X cần viewer và thử 5 targets; không bắt tìm hành tinh.
- Các tuyên bố về đối thủ/past winners trong v2 chưa có hồ sơ nguồn từng dự án. V3 không dùng chúng để cộng/trừ điểm hoặc khẳng định độ độc đáo đã kiểm chứng.

## So sánh shortlist

| | Field Shift | Earth Analog | MODIS/VIIRS |
| --- | --- | --- | --- |
| Người dùng | Nông dân/người tư vấn | Nhóm chuẩn bị thử thiết bị/thí nghiệm | Người quản lý đất, nhà nghiên cứu, người theo dõi hoạt động cháy |
| Quyết định | So luân canh theo ràng buộc/ưu tiên | Chọn địa điểm test cho một đặc tính cụ thể | Nhận biết mùa/chu kỳ và bất thường trong chuỗi hotspot |
| NASA centrality | Lịch sử điều kiện khí hậu/EO thay đổi đánh giá chiến lược | Đặc trưng Earth và planetary làm căn cứ analog | MODIS/VIIRS là cốt lõi |
| Hưng–Việt | Ranking/ràng buộc và forecast có holdout | Similarity và sensitivity | Harmonization và anomaly |
| Bích | Đất/cây/mùa, kiểm claim | Terrain/environment, giới hạn analog | Diễn giải nguồn nhiệt và mùa |
| An–Quang Luật | Node đo + gá/vỏ + quy trình lặp | IMU/fixture dốc gắn mục tiêu thử | Thiết bị hiển thị, ít cần phép đo cơ khí |
| Rủi ro lớn nhất | Chưa đủ nguồn nông học | So dữ liệu khác hành tinh sai scale/ý nghĩa | Hiệu chỉnh làm mất thay đổi thật |
| Giá trị khác biệt đề xuất | Cho thấy nguồn và uncertainty dẫn đến lựa chọn khác nhau, kèm context điểm đo | Analog theo nhu cầu thử, nói rõ chiều tương đồng và giới hạn | Calendar có bằng chứng độ ổn định trước/sau sensor change |

Các điểm khác biệt là giả thuyết thiết kế; chưa phải kết quả khảo sát đối thủ.

## Gate chọn bài — trước khi chuyển sang code

| Gate | Người kiểm | Field Shift đạt khi | Nếu chưa đạt |
| --- | --- | --- | --- |
| G1 — Dữ liệu NASA | Việt | Chỉ rõ product, quyền truy cập, sample/metadata, vùng, kỳ, đơn vị, QA và cách aggregate | Thu hẹp nguồn/vùng; không viết “data ready” |
| G2 — Domain | Bích + Hưng | Bảng đất/cây/mùa có nguồn, ít nhất 3 chiến lược có cơ sở gồm hiện trạng, rủi ro ghi rõ | Xem Earth Analog; không bịa quy tắc cây |
| G3 — Baseline | Hưng + Việt | Định nghĩa score, ràng buộc, đánh giá; target forecast chỉ giữ khi có dữ liệu kiểm | Giữ analysis; bỏ claim prediction chưa có cơ sở |
| G4 — Đội hình | Mỗi thành viên, Hưng tổng hợp | Owner/backup, thời gian và mức học việc đã xác nhận | Giảm số deliverable, ghép cặp |
| G5 — Demo/thiết bị | Hiếu + An + Quang Luật | Một demo path, BOM khả dụng, contract và phương án mất mạng | Dùng snapshot/replay đúng nhãn; không để hardware chặn data |
| G6 — Quy định | Hưng | Xác nhận link challenge/Resources, lịch, yêu cầu nộp, giới hạn việc chuẩn bị trước | Chỉ coi hiện tại là nghiên cứu và tài liệu |

**Hiện trạng:** G1–G6 chưa được xác nhận hoàn tất. Nhiệm vụ hiện tại đã phân tích brief và chuẩn bị docs; chưa chạy data spike, huấn luyện model, đo node hay chốt deadline thi.

Nếu Field Shift trượt G2 nhưng Earth Analog có cặp dữ liệu và một mục tiêu test rõ: ưu tiên Earth Analog. Nếu cả hai thiếu nguồn domain mà FIRMS overlap dùng được: chọn MODIS/VIIRS. Nếu cần phương án thiên software/statistics với hardware hạn chế: xét Trend Detective; không cố thêm cảm biến vô nghĩa.

## Kết luận hành động

Hưng dẫn buổi review theo [phân công](../planning/team-workstreams.md); Bích và Việt kiểm G1/G2 trước; An–Quang Luật kiểm inventory và thiết kế bộ gá. Dùng [bản chọn đề](../final-selection.md) để ghi quyết định thực tế của team. Cho đến lúc đó, trạng thái là **khuyến nghị Field Shift, chưa khóa chính thức**.

