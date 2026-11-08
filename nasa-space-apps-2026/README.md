# NASA Space Apps 2026 — nghiên cứu NeuraX

> Trạng thái 2026-11-04: team đã chọn Field Shift theo xác nhận của người dùng. Dữ liệu, vùng và quy tắc nông học vẫn cần kiểm trước khi triển khai.

## Bắt đầu từ đây

- [Proposal sơ bộ toàn dự án](planning/project-brief.md) / [PDF A4 cho cả team](../output/pdf/NeuraX-AgroTwin-Preliminary-Proposal.pdf): người dùng/giả thuyết, scope, DATA/K1, baseline, UX, architecture, đánh giá, phase, nguồn lực, rủi ro và gate; bản 0.3 ngày 07/11/2026.
- [Paper kỹ thuật gửi An](planning/hardware-design-paper.md) và [PDF A4 đầy đủ](../output/pdf/NeuraX-AgroTwin-Technical-Paper-An.pdf): lý do chọn, alternatives, measurement/test plan, backup, phase và nguồn. [Brief cũ](planning/hardware-demo-brief.md) chỉ là tóm tắt phụ trợ.

Việt làm **Technical Lead / DATA + AI**, chia module AI với Hưng; Quang Luật kiểm QA/thống kê độc lập và hỗ trợ An kiểm thiết bị. Quyền sở hữu chi tiết nằm trong team-workstreams và từng workflow.

- [14 hồ sơ challenge](challenges/README.md): mỗi đề một file, phân tích + nguyên văn.
- [Nguồn đầu vào và mức xác nhận](sources/challenge-intake.md): Resources còn thiếu, truy cập trang challenge live trả lỗi.
- [Kết quả kiểm tra tài liệu](sources/review-record.md): coverage, links, score, skill và giới hạn kiểm Mermaid.
- [Shortlist v4](rankings/v4-data-qa-shortlist.md): cập nhật thế mạnh thống kê của Quang Luật; Field Shift, Earth Analog, MODIS/VIIRS được so theo điều kiện dữ liệu.
- [Ba workflow cụ thể](planning/workflows/README.md): DATA input/output, baseline AI, payload DEPLOY, owner và tiêu chí bàn giao.
- [Timeline HCMC](planning/event-timeline.md): 14–15/11/2026, NOVAWORLD theo team; baseline giờ có nghỉ và buffer, chưa là lịch BTC.
- [Phân công DATA → AI → DEPLOY](planning/team-workstreams.md): bảng sáu người, Mermaid, task và onboarding Quang Luật.
- [Kiến trúc đề xuất](planning/architecture.md): gói D1/Q1/A1/E1/H1, metadata, QA, version và cách làm khi thiếu data.
- [Hardware của An–Quang Luật](planning/hardware-preparation.md): BOM, chức năng, phép thử, thiết bị cần xác minh.
- [Challenge đã chọn](final-selection.md): problem framing, phạm vi và các gate dữ liệu còn mở.

- [Playbook cuộc thi](planning/competition-playbook.md): tiêu chí tham chiếu, evidence và ngôn ngữ bài nộp; cập nhật 06/11, chưa xác nhận đủ luật 2026/HCMC.

## 14 hồ sơ

1. [Abandoned but not Forgotten](challenges/01-abandoned-but-not-forgotten.md)
2. [Earth System Trend Detective](challenges/02-earth-system-trend-detective.md)
3. [Junior Astronaut Mission Trainer](challenges/03-junior-astronaut-mission-trainer.md)
4. [Lunar Landing Site Navigator](challenges/04-clps-lunar-mission-browser.md) — giữ slug CLPS cũ.
5. [Astronaut Health Monitoring](challenges/05-astronaut-health-monitoring.md)
6. [Dancing with the SARs](challenges/06-dancing-with-the-sars.md)
7. [Field Shift](challenges/07-field-shift.md)
8. [Flame in Freefall](challenges/08-flame-in-freefall.md)
9. [MODIS + VIIRS Hot Spots](challenges/09-modis-viirs-hot-spots.md)
10. [Earth Analog Locations](challenges/10-earth-analogs-moon-mars.md)
11. [Martian Map](challenges/11-martian-map.md)
12. [Planet X and SPHEREx](challenges/12-planet-x-spherex.md)
13. [Space Mission Design Game](challenges/13-space-mission-design-game.md)
14. [Earth Information Jukebox](challenges/14-earth-information-jukebox.md)

ID repo được giữ ổn định; thứ tự khác bản nguồn ở Lunar Landing. Xem bảng mapping ở mục lục challenge.

## Lịch sử quyết định

- [v1 — pre-release](rankings/v1-pre-release.md): MODIS/VIIRS #1.
- [v2 — team reassessment](rankings/v2-team-reassessment.md): Field Shift #1, baseline 5 người.
- [v3 — full supplied briefs + 6 members](rankings/v3-full-brief-six-members.md): snapshot trước khi nhận thế mạnh Quang Luật.
- [v4 — DATA QA shortlist](rankings/v4-data-qa-shortlist.md): hiện hành cho ba idea; không re-score 14 đề khi chưa có dữ liệu mới.
- [Decision log](decision-log.md): ghi ngày, trạng thái và lý do đổi.
- [Competitor research](competitor-research/README.md), [past winners](past-winners/README.md): các giả thuyết cũ cần nguồn dự án cụ thể trước khi dùng như bằng chứng.

## Điều cần hiểu đúng

Tên dataset có trong brief không đồng nghĩa phải dùng tất cả hoặc đã truy cập được. Analysis, forecast và scenario là ba loại kết quả khác nhau. An có một subsystem embedded để sở hữu; Quang Luật sở hữu QA/thống kê/báo cáo và hỗ trợ An kiểm log thiết bị. Prototype vẫn phải xử lý NASA data nếu sensor ngắt.

Ngày thi 14–15/11/2026 đã được NASA và team xác nhận; giờ khai mạc/local pitch/deadline HCMC vẫn cần BTC công bố. Không coi 48 giờ là thời gian làm việc liên tục; xem baseline timeline. Chưa có sản phẩm chạy, benchmark AI hoặc kết quả hardware trong đợt cập nhật docs này.

[Team profile](../team/team-profile.md) · [Skill catalog](../governance/skills-catalog.md).
