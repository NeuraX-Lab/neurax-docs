# Chuẩn bị thi NASA Space Apps với Field Shift

> Kiểm nguồn ngày 2026-11-06. Field Shift đã được chọn 04/11; hướng dẫn này phục vụ chuẩn bị và review, chưa ghi nhận sản phẩm chạy hay đảm bảo giải thưởng.

## Cuộc thi và cách tiếp cận

NASA mô tả Space Apps 2026 là hackathon toàn cầu hai ngày, 14–15/11, giải challenge do chuyên gia NASA đặt ra bằng dữ liệu mở; nhiều chuyên môn đều có thể đóng góp. [Thông báo NASA](https://science.nasa.gov/universe/nasa-welcomes-all-ages-experience-levels-for-space-apps-challenge/) xác nhận mô hình và ngày sự kiện.

Mục tiêu nội bộ: giải một quyết định có ý nghĩa, dùng NASA data thực chất, có phương pháp kiểm được và demo dễ hiểu. Tối ưu chất lượng bài thi theo bằng chứng, không tối ưu số model, số nguồn hay số skill.

## Tiêu chí và mức xác nhận

Năm tiêu chí Impact, Creativity, Validity, Relevance, Presentation xuất hiện trong [hướng dẫn chấm 2025](https://spaceapps-v2-staging.s3.amazonaws.com/media/documents/Final_Space_Apps_2025_Judging_Guidelines_for_web.pdf). Kết quả search trang [Ajmer 2026](https://www.spaceappschallenge.org/2026/local-events/ajmer/) cũng nêu năm tên này, nhưng mở trực tiếp trả 502. Chưa đọc được bộ hướng dẫn toàn cầu 2026 đầy đủ. Dùng bảng dưới làm khung review nội bộ, không gán trọng số hay luật loại trực tiếp của năm trước cho năm nay.

| Tiêu chí tham chiếu | Bằng chứng NeuraX cần chuẩn bị | Owner dẫn |
| --- | --- | --- |
| Impact — tác động | Một nhóm người dùng, một quyết định, vấn đề có nguồn; phỏng vấn nếu thực sự thực hiện | Hưng + Bích |
| Creativity — sáng tạo | So phương án hiện có có URL/ngày đọc; chỉ rõ cải tiến có ích, tránh claim 'đầu tiên' thiếu kiểm chứng | Hưng + Hiếu |
| Validity — tính đúng/khả thi | NASA sample truy nguồn, K1 nông học, QA, baseline và sensitivity; forecast có holdout riêng | Việt + Bích + Quang Luật |
| Relevance — bám đề | NASA-derived feature thực sự ảnh hưởng so luân canh; nêu contribution của từng nguồn | Việt + Hưng |
| Presentation — trình bày | Luồng demo, biểu đồ đọc được, nguồn và giới hạn; rehearsal với người chưa biết dự án | Hiếu + cả team |

Không dùng bảng này làm thang điểm NASA hay bằng chứng tăng năng suất. Hướng dẫn 2025 có các điều kiện về ngôn ngữ, link, demo và khai báo AI; tất cả điều kiện cụ thể phải kiểm lại với tài liệu 2026 trước khi khóa bản nộp.

## Scope Field Shift đề xuất

Một vùng, nhóm cây có nguồn, so ba chiến lược gồm hiện trạng; 1–2 nguồn NASA đủ cho lát cắt đầu. Baseline lọc ràng buộc rồi xếp hạng có giải thích. Chỉ thêm forecast khi có target, chuỗi và đánh giá hợp lệ. Node đo là context riêng, không xác nhận mọi pixel hay soil health.

Luồng demo: chọn vùng/hiện trạng → xem điều kiện và coverage → chỉnh ưu tiên → so phương án và lý do → xem nguồn, unknown và rủi ro. Chỉ giữ những bước đã được triển khai; storyboard không phải kết quả chạy.

## Trước khi nộp cần xác nhận

Hưng tổng hợp tài liệu 2026/HCMC về: thời điểm được bắt đầu làm project, deadline local/global và múi giờ, eligibility/team registration, ngôn ngữ, form và giới hạn demo, link truy cập, source/license, khai báo AI và tài nguyên được phép dùng. Đánh dấu verified / search-only / unknown kèm nguồn và ngày; chưa biết không tự đổi thành pass. Địa điểm NOVAWORLD là thông tin team cung cấp; trang HCMC chưa đọc được trong lượt này.

Repo nghiên cứu nội bộ không phải bản nộp. Chỉ xuất project page, demo và artifact được chọn khi được giao; không tự đổi visibility hoặc công bố nghiên cứu nội bộ.

## Skill và nhịp làm việc

Chọn từ [catalog](../../governance/skills-catalog.md): research cho nguồn/K1, idea-lab cho scope, architecture cho contract, team-planning cho owner, optimization khi có bottleneck, pitch-review cho rehearsal, docs-maintenance để đồng bộ. Skill ngoài dùng theo tác vụ EO/thống kê/notebook; không nạp tất cả cùng lúc.

Giữ các gate T+2/T+6/T+12 và D−8h theo [timeline](event-timeline.md). Nếu cần cắt, bỏ nguồn/model/animation phụ trước; bảo vệ NASA data → baseline → kết quả → demo → evidence. Chọn 'needs_review/unavailable' khi thiếu căn cứ.
