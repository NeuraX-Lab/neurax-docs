# NeuraX Knowledge Base

`neurax-docs` là kho nghiên cứu, hồ sơ team và quyết định của **NeuraX-Lab**: vì sao chọn hướng đi, giải quyết vấn đề gì và chuẩn bị ai làm gì.

Hiện tại chỉ làm **Markdown + Mermaid**, gồm cả kiến trúc đề xuất và chuẩn bị hardware. Code sản phẩm và tài liệu hệ thống đã triển khai thuộc [nasasac26-neurax](https://github.com/NeuraX-Lab/nasasac26-neurax).

## NASA Space Apps 2026 — cập nhật 2026-10-30

- Đã phân tích **14 đề chi tiết** từ bản `docs/challenges.md` do người dùng cung cấp; nguyên văn từng đề ở cuối mỗi dossier.
- Đội hình **6 người**: AI ×2, Khoa học Môi trường, Software Engineering, Hardware và Quang Luật — sinh viên Cơ khí năm 2, thế mạnh thống kê/trực quan hóa (RStudio, MATLAB), AutoCAD và báo cáo LaTeX/Overleaf.
- Khuyến nghị v4 (định tính, vai trò DATA QA): **Field Shift → Earth Analog → MODIS/VIIRS Hot Spots**.
- **Chưa khóa lựa chọn của team**; chưa audit đầy đủ Resources/dataset, chưa build, huấn luyện hay thử phần cứng.
- Luồng sản phẩm mong muốn: **DATA → AI (analysis/prediction có kiểm chứng) → DEPLOY (dashboard/demo/hardware)**. Prediction và phần cứng phải phục vụ bài toán, có giới hạn rõ.

## Đọc theo thứ tự

1. [Hồ sơ team](team/team-profile.md).
2. [Mục lục 14 challenge](nasa-space-apps-2026/challenges/README.md).
3. [Shortlist v4 theo thế mạnh Quang Luật](nasa-space-apps-2026/rankings/v4-data-qa-shortlist.md).
4. [Sơ đồ phân công, onboarding Quang Luật và task chuẩn bị](nasa-space-apps-2026/planning/team-workstreams.md).
5. [Kiến trúc DATA–AI–DEPLOY](nasa-space-apps-2026/planning/architecture.md).
6. [BOM và đầu việc hardware của An–Quang Luật](nasa-space-apps-2026/planning/hardware-preparation.md).
7. [Ba workflow: input/output, baseline và owner](nasa-space-apps-2026/planning/workflows/README.md).
8. [Lịch HCMC 14–15/11 và mốc bàn giao](nasa-space-apps-2026/planning/event-timeline.md).
9. [Bản đề xuất chọn challenge](nasa-space-apps-2026/final-selection.md).

Team xác nhận thi tại **NOVAWORLD, local event Ho Chi Minh City**, ngày **14–15/11/2026**; giờ cụ thể chưa có. Quang Luật ưu tiên DATA QA/thống kê và cùng An kiểm thiết bị; không mặc định phụ trách vỏ/cọc/gá.

**Việt là Technical Lead / DATA + AI**: kiến trúc/contract, dữ liệu, module AI và review tích hợp. Hưng giữ hướng bài toán/scope và cùng Việt phát triển AI; Hiếu và An vẫn sở hữu software/embedded của mình.

## Bộ skill dùng lại

Sáu skill ở `.agents/skills/`: research challenge, brainstorm idea, chia task/onboarding, cập nhật docs, kiến trúc và tối ưu hệ thống. [Catalog](governance/skills-catalog.md) có đường dẫn, cách gọi và kết quả khảo sát skill bên ngoài.

Đây là workflow theo yêu cầu trong repo, không phải tác vụ nền đã lên lịch. Làm việc trong thư mục neurax-docs để dùng bộ skill của repo.

## Cấu trúc

```text
neurax-docs/
├── .agents/skills/             # 6 SKILL.md
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
