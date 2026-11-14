# NASA Space Apps 2026 — NeuraX Research

## DATA và AI research v1 — 14/11 tối

Hai báo cáo tách riêng: [DATA NASA + LOCAL + FARM preferences mô phỏng](planning/data-report-ai-v1.md) và [kiến trúc, training, evaluation, demo AI](planning/ai-report-v1.md). User đã cho phép mô phỏng mục tiêu FARM. HGB mưa và LLM selector đã được thử, nhưng baseline đơn giản tốt hơn nên giữ baseline; chưa có crop winner hoặc xác nhận canh tác tại ruộng. Các trạng thái “chưa train/chờ FARM” phía dưới là lịch sử trước bước này.

## Quyết định DATA v1 — 14/11/2026

[Workflow được user đồng ý, LOCAL tập trung và DATA v1](planning/data-block-v1.md): chốt thứ tự DATA trước AI, chọn features A8/B10, preprocessing và fusion theo đúng grain. Các trạng thái chưa chọn features trong snapshot cũ bên dưới đã được cập nhật bằng quyết định này. FARM INPUT chờ user cung cấp; chưa train hoặc build RAG.

## Local evidence và ML/RAG — 14/11 chiều

[Bích bản có nguồn và bổ sung dữ liệu địa phương](planning/local-evidence-review-2026-11-14.md): source audit, soil/station/study tables, corpus Anh–Việt và workflow forecast/recommender/RAG dự tính. Chưa chốt features hoặc train.

## EDA vệ tinh và kiến trúc ML + RAG — 14/11

[Review Bích, MODIS/SMAP/Sentinel-2 và đề xuất ML + RAG](planning/satellite-bich-ml-rag-2026-11-14.md). Người dùng yêu cầu cùng chốt features sau khi xem EDA và kiến trúc dự tính; chưa training hoặc chốt output.

## Resources và EDA — bổ sung 13/11/2026

[Snapshot, shortlist và Q&A](resources/README.md) cập nhật tab Resources do người dùng cung cấp và case MT-BLOCK-01 / Mỹ Thành, Đồng Tháp. Lab khảo sát POWER, MODIS, SMAP, IMERG và SoilGrids từ pack; **không chốt source/model hoặc đổi trạng thái chọn challenge**. Nội dung 30/10 bên dưới là snapshot cũ.

> Trạng thái 2026-10-30: đã phân tích đủ 14 đề chi tiết từ bản người dùng cung cấp; đội hình sáu người; đề xuất Field Shift, chưa khóa lựa chọn.

## Bắt đầu từ đây

Việt làm **Technical Lead / DATA + AI**, chia module AI với Hưng; Quang Luật kiểm QA/thống kê độc lập và hỗ trợ An kiểm thiết bị. Quyền sở hữu chi tiết nằm trong team-workstreams và từng workflow.

- [14 challenge dossiers](challenges/README.md): mỗi đề một file, phân tích + nguyên văn.
- [Nguồn đầu vào và mức xác nhận](sources/challenge-intake.md): Resources còn thiếu, truy cập trang challenge live trả lỗi.
- [Kết quả kiểm tra tài liệu](sources/review-record.md): coverage, links, score, skill và giới hạn kiểm Mermaid.
- [Shortlist v4](rankings/v4-data-qa-shortlist.md): cập nhật thế mạnh thống kê của Quang Luật; Field Shift, Earth Analog, MODIS/VIIRS được so theo điều kiện dữ liệu.
- [Ba workflow cụ thể](planning/workflows/README.md): DATA input/output, baseline AI, payload DEPLOY, owner và tiêu chí bàn giao.
- [Timeline HCMC](planning/event-timeline.md): 14–15/11/2026, NOVAWORLD theo team; baseline giờ có nghỉ và buffer, chưa là lịch BTC.
- [Phân công DATA → AI → DEPLOY](planning/team-workstreams.md): six-owner matrix, Mermaid, task và onboarding Quang Luật.
- [Kiến trúc đề xuất](planning/architecture.md): gói D1/Q1/A1/E1/H1, metadata, QA, version và cách làm khi thiếu data.
- [Hardware của An–Quang Luật](planning/hardware-preparation.md): BOM, chức năng, phép thử, thiết bị cần xác minh.
- [Đề xuất chọn bài](final-selection.md): problem framing và điều kiện chốt của team.

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
