# Kho kiến thức nội bộ NeuraX

> **ĐIỂM BẮT ĐẦU HIỆN HÀNH:** [Đọc trạng thái, vai trò và ba tài liệu cần dùng](nasa-space-apps-2026/planning/START-HERE.md). Mỹ Thành; Hưng-Việt cùng core; Hiếu backend remote. Các proposal/PDF cũ là snapshot, không dùng ghép phân công.


`neurax-docs` là kho nghiên cứu, hồ sơ team và quyết định của **NeuraX-Lab**: vì sao chọn hướng đi, giải quyết vấn đề gì và chuẩn bị ai làm gì.

Hiện tại chỉ làm **Markdown + Mermaid**, gồm cả kiến trúc đề xuất và chuẩn bị hardware. Code sản phẩm và tài liệu hệ thống đã triển khai thuộc [nasasac26-neurax](https://github.com/NeuraX-Lab/nasasac26-neurax).

## NASA Space Apps 2026 — cập nhật 2026-11-12

Kết quả kiểm case mới nhất: [Đức Lập — đất/cây/mùa và NASA](nasa-space-apps-2026/planning/cases/duc-lap/README.md). Đã tải POWER 2015–2025, 4.018 ngày, kiểm kỹ thuật đạt nhưng QA tổng thể WARN do một ngày mưa cần đối chiếu. Chưa đủ baseline thật và hai rotation hợp lệ cùng thửa; ưu tiên review bắp/mè, giữ đậu phộng candidate. Đây là bổ sung sau snapshot PDF proposal 0.4, chưa xuất lại PDF trong lượt audit dữ liệu.

- Đã phân tích **14 đề chi tiết** từ bản `docs/challenges.md` do người dùng cung cấp; nguyên văn từng đề ở cuối mỗi dossier.
- Đội hình **6 người**: AI ×2, Khoa học Môi trường, Software Engineering, Hardware và Quang Luật — sinh viên Cơ khí năm 2, thế mạnh thống kê/trực quan hóa (RStudio, MATLAB), AutoCAD và báo cáo LaTeX/Overleaf.
- Khuyến nghị v4 (định tính, vai trò DATA QA): **Field Shift → Earth Analog → MODIS/VIIRS Hot Spots**.
- **Team đã chọn Field Shift**, theo xác nhận ngày 2026-11-04 được ghi trong [decision log](nasa-space-apps-2026/decision-log.md). Chưa audit đầy đủ Resources/dataset, chưa build, huấn luyện hay thử phần cứng.
- Luồng sản phẩm mong muốn: **DATA → AI (analysis/prediction có kiểm chứng) → DEPLOY (dashboard/demo/hardware)**. Prediction và phần cứng phải phục vụ bài toán, có giới hạn rõ.

## Đọc theo thứ tự

**Đầu việc đang mở:** hoàn thiện [hồ sơ địa phương Đức Lập](nasa-space-apps-2026/planning/cases/duc-lap/README.md) về địa điểm–đất–nước–cây–mùa để đề xuất case với team. [Đề xuất tổng hợp 1.0](nasa-space-apps-2026/planning/team-proposal-2026-11-12.md) và [PDF tương ứng](output/pdf/NeuraX-AgroTwin-Team-Decision-Proposal.pdf) là tài liệu phụ trợ đã soạn trước khi làm rõ phạm vi; không là kết luận hoàn tất nghiên cứu địa phương. Không gọi reference baseline là hiện trạng ruộng đã xác minh.

Phương án cải thiện hiện hành: [kế hoạch local/global](nasa-space-apps-2026/planning/local-to-global-strategy.md). Ba tương tác ưu tiên: vì sao loại, khi nào đổi ý, còn thiếu gì. Farm 2D là giao diện quyết định; sensor thật ở ô live riêng. Case Đức Lập là đề xuất nghiên cứu; HTTPSLAB đã đồng ý cho mượn theo team, đang chờ thông số.

Đọc dự án: [proposal sơ bộ AgroTwin 0.4](nasa-space-apps-2026/planning/project-brief.md) · [PDF proposal cho cả team](output/pdf/NeuraX-AgroTwin-Preliminary-Proposal.pdf), cập nhật 12/11/2026. Riêng hardware: [PDF kỹ thuật gửi An](output/pdf/NeuraX-AgroTwin-Technical-Paper-An.pdf) · [Markdown nguồn](nasa-space-apps-2026/planning/hardware-design-paper.md). Brief sáu trang là bản đọc nhanh phụ trợ.

1. [Hồ sơ team](team/team-profile.md).
2. [Mục lục 14 challenge](nasa-space-apps-2026/challenges/README.md).
3. [Shortlist v4 theo thế mạnh Quang Luật](nasa-space-apps-2026/rankings/v4-data-qa-shortlist.md).
4. [Sơ đồ phân công, onboarding Quang Luật và task chuẩn bị](nasa-space-apps-2026/planning/team-workstreams.md).
5. [Kiến trúc DATA–AI–DEPLOY](nasa-space-apps-2026/planning/architecture.md).
6. [BOM và đầu việc hardware của An–Quang Luật](nasa-space-apps-2026/planning/hardware-preparation.md).
7. [Ba workflow: input/output, baseline và owner](nasa-space-apps-2026/planning/workflows/README.md).
8. [Lịch HCMC 14–15/11 và mốc bàn giao](nasa-space-apps-2026/planning/event-timeline.md).
9. [Challenge đã chọn và các gate còn mở](nasa-space-apps-2026/final-selection.md).

Team xác nhận thi tại **NOVAWORLD, local event Ho Chi Minh City**, ngày **14–15/11/2026**; giờ cụ thể chưa có. Quang Luật ưu tiên DATA QA/thống kê và cùng An kiểm thiết bị; không mặc định phụ trách vỏ/cọc/gá.

**Hưng-Việt cùng đóng góp chính:** features, pipeline, kiến trúc, output demo; Hưng workflow/scope Data -> AI, Việt technical AI/Data Analysis. Bích Data/review nguồn-feature; Hiếu backend remote gián đoạn; An ESP/sensor demo; Luật thống kê/đánh giá/QA từng block.

## Bộ skill dùng lại

Bảy skill NeuraX được theo dõi trong `.agents/skills/`: nghiên cứu, idea/scope, chia việc, cập nhật docs, kiến trúc, tối ưu và pitch/review. Bốn skill ngoài đã cài local: jupyter-notebook, geomaster, statistical-analysis và scientific-critical-thinking. [Catalog](governance/skills-catalog.md) có cách gọi, nguồn pin và cách cài lại.

Đây là workflow theo yêu cầu trong repo, không phải tác vụ nền đã lên lịch. Làm việc trong thư mục neurax-docs để dùng bộ skill của repo.

## Cấu trúc

```text
neurax-docs/
├── .agents/skills/             # 7 SKILL.md, theo dõi trong Git
├── AGENTS.md
├── team/team-profile.md
├── governance/
│   ├── repository-strategy.md
│   └── skills-catalog.md
└── nasa-space-apps-2026/
    ├── README.md
    ├── challenges/             # 14 dossier + mục lục
    ├── sources/                # provenance và mức xác nhận
    ├── planning/               # phân công, kiến trúc, hardware
    ├── rankings/               # v1/v2/v3 lịch sử; v4 shortlist hiện hành
    ├── competitor-research/
    ├── past-winners/
    ├── decision-log.md
    └── final-selection.md
```

## Quy ước bằng chứng và quyền sở hữu

Tách **theo bản đề**, **nguồn web đã đọc**, **candidate/cần kiểm**, **đề xuất NeuraX** và **kết quả đã thử**. Nguồn được nhắc tên chưa đồng nghĩa đã tải hay kiểm chứng; yêu cầu “may/could” không tự thành bắt buộc. Xem [nguồn đầu vào](nasa-space-apps-2026/sources/challenge-intake.md).

V1/v2/v3 là lịch sử; v4 cập nhật shortlist và vai trò, không chấm lại toàn bộ 14 đề. Các nhận định đối thủ/winner cũ chưa có hồ sơ nguồn từng dự án; không dùng như bằng chứng đã xác minh trong quyết định hiện hành.

[Repository strategy](governance/repository-strategy.md) phân biệt nghiên cứu/proposal ở đây với code và as-built docs ở repo sản phẩm. Hồ sơ tổ chức và community defaults thuộc NeuraX-Lab/.github.

Repo dùng nội bộ; tài liệu điều phối hiện hành bằng tiếng Việt, giữ nguồn/thuật ngữ tiếng Anh và snapshot lịch sử. Bài nộp đối ngoại chuẩn bị tiếng Anh riêng theo quy định đúng năm. Xem [ngôn ngữ và bằng chứng](governance/language-and-evidence.md).
