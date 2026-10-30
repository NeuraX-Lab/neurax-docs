# Lịch chuẩn bị và vận hành — HCMC, 14–15/11/2026

> Cập nhật 2026-10-30 · Múi giờ Asia/Saigon (UTC+7).
> Team xác nhận đăng ký Ho Chi Minh City, địa điểm **NOVAWORLD**, ngày **14–15/11/2026**. Tên địa điểm do người dùng cung cấp; chưa xác minh địa chỉ chi tiết, giờ mở cửa, giờ pitching và hạn nộp local.

## Bằng chứng và lịch năm trước

| Thông tin | Nguồn / mức xác nhận |
| --- | --- |
| Sự kiện toàn cầu 14–15/11/2026 | Đã đọc [NASA Science](https://science.nasa.gov/universe/nasa-welcomes-all-ages-experience-levels-for-space-apps-challenge/) ngày 2026-10-30 |
| Cách gọi hackathon 48 giờ | Đã đọc [Canadian Space Agency](https://www.asc-csa.gc.ca/eng/events/2026/2026-11-14-space-apps-challenge.asp); không suy ra 48 giờ làm liên tục hoặc venue mở qua đêm |
| Khung nộp 09:00 14/11 → 23:59 15/11 giờ địa phương | Kết quả tìm kiếm của [trang 2026 chính thức](https://www.spaceappschallenge.org/2026/) hiển thị mốc này; mở trực tiếp trả 502. **Chưa coi là deadline HCMC đã xác nhận** |
| HCMC 2025: 4–5/10 tại VNG Campus | [HCMUS](https://en.hcmus.edu.vn/pre-hackathon-meet-up-nasa-space-apps-challenge-ho-chi-minh-2025/) xác nhận và mô tả pre-hackathon ngày 28/9; không có agenda theo giờ của hai ngày thi trong trang |
| 2025 toàn cầu | [NASA 2025](https://www.nasa.gov/nasa-space-apps-challenge-2025/) nêu ngày 4–5/10; không thay thế lịch 2026 |
| HCMC 2025/2026 local pages | Đã thử hai trang local-events/ho-chi-minh-city, công cụ chưa đọc được |
| Ranh giới chuẩn bị trước | [Local organizer Tel Aviv 2026](https://space.tau.ac.il/SpaceApps2026) phân biệt khám phá challenge/data/idea trước sự kiện với project work khi hackathon bắt đầu; cần đối chiếu hướng dẫn HCMC |

Không tìm được lịch chi tiết HCMC 2025 đủ tin cậy để chép giờ khai mạc/mentoring/pitch. Một listing bên thứ ba nói meetup 21/9, khác bài HCMUS về meetup 28/9; không dùng giờ meetup làm giờ hackathon. Không lấy lịch 2024 hoặc FAQ 2023 trên staging làm quy định 2026.

Nếu khung 09:00–23:59 ở trên đúng, thời gian trôi qua chỉ **38 giờ 59 phút**, không phải 48 giờ. Local pitch có thể sớm hơn; cần bản demo sẵn trước mốc đó.

## Mốc điều hành do NeuraX đề xuất

- **T0:** giờ được bắt đầu làm project do BTC xác nhận.
- **D_local:** hạn local nộp/pitch cần bản ổn định; **D_global:** hạn nộp nền tảng.
- **D = min(D_local, D_global)** để khóa feature và rehearsal; vẫn quản lý riêng việc nộp global sau local nếu hai thủ tục khác nhau.
- Nếu BTC chưa đưa giờ: lấy 09:00 ngày 14/11 làm **ví dụ tính lịch**, và đặt mục tiêu **demo local sẵn 12:00 ngày 15/11**, không coi đây là agenda chính thức.
- Khi có lịch thật, Hưng sửa T0/D, Việt (Technical Lead) và Hiếu tính lại mốc freeze/upload; task phụ tự cắt để giữ integration và thời gian nghỉ.

## Chuẩn bị 30/10–13/11 — nghiên cứu, docs và logistics

| Ngày đề xuất | Owner | Đầu ra | Giới hạn |
| --- | --- | --- | --- |
| 30/10–02/11 | Hưng, Bích, Việt, Quang Luật | Review shortlist, câu hỏi domain, nguồn candidate và skill profile | Chưa tuyên bố chọn bài hoặc data ready |
| 03–06/11 | Việt + Quang Luật + Bích | Data dictionary, mapping source, QA/evaluation protocol | Ghi rõ điều chưa biết; không tải/huấn luyện sản phẩm trong kế hoạch docs hiện tại |
| 07–10/11 | Việt (TL), Hiếu + Hưng; An | Storyboard, A1 mẫu trên giấy/docs, interface H1, inventory | Không triển khai submission project trước giờ được BTC cho phép |
| 11–12/11 | Cả team | Review một idea chính + fallback, owner/backup, laptop/tài khoản/cáp có sẵn | Chỉ readiness/logistics; không giả fixture thành kết quả NASA |
| 13/11 | Hưng + Hiếu | Kiểm giờ HCMC, venue, wifi/điện, local/global submission, hình thức pitch và quy định chuẩn bị | Cập nhật bảng lịch; không suy ra quy định từ năm trước |

Mỗi phiên chuẩn bị có thể 45–90 phút theo lịch rảnh; chưa đặt calendar hay giao việc bên ngoài. Không cần mọi thành viên họp tất cả các phiên.

## Baseline 2 ngày — ví dụ, không phải agenda BTC

Giả sử T0 = 09:00 14/11 tại UTC+7; giờ local pitch chưa biết.

| Giờ ví dụ | Mốc | Việc theo owner | Kết quả / quyết định |
| --- | --- | --- | --- |
| 14/11 09:00–11:00 | T+0→2 | Hưng chốt 1 idea; Bích ràng buộc; Việt chốt kiến trúc/sample/contract; Quang Luật QC; Hiếu/An integration plan | Gate data, schema v0.1 và một đường demo; chưa đạt thì giảm nguồn |
| 11:00–15:00 | T+2→6 | Việt D1 và module AI theo idea; Quang Luật Q1; Hưng module baseline còn lại; Hiếu UI với mẫu; An device độc lập | D1 thật đầu tiên, A1 baseline tối thiểu |
| 15:00–21:00 | T+6→12 | Việt dẫn ghép baseline thật cùng Hưng/Hiếu; Bích rà; Quang Luật kiểm metric; An thử log tối đa một phiên chung | Demo đầu cuối; không có thì bỏ model nâng cao |
| 21:00–23:00 | T+12→14 | Sửa lỗi chặn, lưu snapshot, phân rõ việc sáng | Baseline ổn định, backup |
| 23:00–05:00 ngày 15/11 | T+14→20 | Nghỉ khoảng 6 giờ, không lên task đường găng | Không cần người trực khi batch đã dừng; điều chỉnh theo venue |
| 15/11 05:00–09:00 | T+20→24 | Quang Luật E1/report; Hưng kiểm claim; Hiếu UX lỗi; An trạng thái display; Bích evidence | Freeze feature sớm, chỉ fix quan trọng |
| 09:00–12:00 | T+24→27 | Rehearsal, pitch/video/refs, test offline; Hưng kiểm form | Bản sẵn sàng local theo mục tiêu nội bộ |
| Sau 12:00 đến D | Theo lịch thật | Pitch/mentor/nộp, chỉ sửa cần thiết | Không mở thêm idea/model; nộp trước hạn an toàn |
| D−4h / D−2h / D−1h | Quy tắc ưu tiên | Rehearsal / nộp bản đầu / kiểm link-quyền truy cập | Nếu sớm hơn giờ ví dụ, ưu tiên các mốc D này |

Ăn uống và di chuyển nằm trong các block, không tính tất cả giờ là productive time. Capacity dự kiến khoảng 18–22 giờ tập trung/người cho hai ngày, phải sửa theo availability; không dùng phép tính 6 × 48 giờ để cam kết khối lượng.

Nếu local pitch buổi sáng 15/11, freeze ngay tối 14/11 và giữ khoảng nghỉ; bỏ forecast/3D/extra sensors. Nếu chỉ có 24 giờ usable, giữ các mốc gate đầu 2 giờ, baseline đầu cuối trước 8 giờ, phần còn lại QA, demo, báo cáo và nộp.

## Gate để không phí thời gian

| Khi | Quyết định | Owner |
| --- | --- | --- |
| T+2 | Data thực có truy cập được, feature/core đủ làm không? Không thì thu hẹp hoặc chọn fallback có sẵn | Hưng sau input Việt/Bích/Quang Luật |
| T+6 | Có D1 pass và baseline đang ra output không? Nếu chưa: không thêm nguồn/model | Hưng + Việt |
| T+12 | Có demo A1 thật chưa? Nếu chưa: dừng candidate, tập trung baseline | Việt + Hiếu; Hưng chốt scope |
| D−8h | Khóa feature; thiết bị hỏng chuyển replay/đơn giản hóa có nhãn | Việt + An; Hưng chốt scope |
| D−4h | Rehearsal nguồn/claim/links, lưu snapshot và video nếu quy định cho phép | Cả team |
| D−2h | Nộp bản đầu và kiểm xác nhận; không chờ phút cuối | Hưng + Hiếu |
| D−1h | Rà quyền truy cập, nguồn, team/challenge association và receipt | Hưng |

Khung này dùng chung ba idea; [workflow](workflows/README.md) xác định deliverable D1/A1/E1 riêng từng bài.
