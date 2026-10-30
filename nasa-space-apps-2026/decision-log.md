# NASA Space Apps 2026 — Decision Log

## 2026-10-30 — Việt là Technical Lead, làm DATA và AI

Người dùng xác nhận Việt biết xử lý DATA và làm AI, có thể đảm nhiệm Technical Lead. Kế hoạch hiện hành giao Việt kiến trúc/contract, pipeline và module AI cụ thể: Field Shift — forecast có gate và inference integration; Earth Analog — similarity implementation; MODIS/VIIRS — anomaly baseline. Hưng giữ hướng bài toán/scope và module AI còn lại, cùng review. Quang Luật giữ QA/E1 độc lập; Hiếu/An tự chủ trong contract để Việt không thành điểm nghẽn. Phân công chỉ coi Việt là người chuẩn hóa dữ liệu trong bản nháp trước đã được sửa.

## 2026-10-30 — cập nhật thế mạnh Quang Luật và workflow ba idea

- Theo lời Quang Luật được người dùng chuyển lại: phân tích thống kê/trực quan hóa với RStudio, MATLAB; AutoCAD; báo cáo LaTeX/Overleaf. Dùng tên hiển thị Quang Luật.
- Điều chỉnh phân công cũ dựa trên ngành Cơ khí: Quang Luật sở hữu DATA QA, đánh giá và báo cáo; cùng An kiểm dữ liệu thiết bị. An sở hữu hardware; vỏ/cọc/gá không còn là deliverable mặc định của Quang Luật.
- Dùng sáu skill repo-local để nghiên cứu thời gian, so idea, chia task, cập nhật docs, định nghĩa contract/kiến trúc và cắt scope theo deadline; cập nhật hai skill có giả định vai trò cũ.
- Thêm [ba workflow](planning/workflows/README.md) với schema DATA→AI, output AI→DEPLOY, baseline, ví dụ synthetic, QA, owner và gate thời gian. Không tạo code hoặc dataset giả thành bằng chứng.
- [V4 shortlist](rankings/v4-data-qa-shortlist.md) thay v3 cho quyết định ba idea hiện tại, không giả vờ đã re-score cả 14.
- Team xác nhận HCMC, NOVAWORLD, 14–15/11/2026; [lịch](planning/event-timeline.md) ghi rõ nguồn năm 2025, ngày 2026 và các giờ local chưa biết. Lịch theo giờ trong docs là đề xuất nội bộ, không agenda của BTC.

Các ghi nhận phân công cơ khí ở phần trước của lịch sử bên dưới đã được thay bằng quyết định này.

## 2026-10-30 — full supplied briefs, sixth member and v3 proposal

- Read all 14 detailed briefs in the user-supplied `docs/challenges.md`; retained each original section in its dossier. The input lacks the Resources tab; live NASA challenge pages returned 502 during verification. See [provenance](sources/challenge-intake.md).
- Added Quang Luật, second-year Mechanical Engineering student with limited competition experience. Advanced mechanical/CAD skills remain unconfirmed.
- Updated the existing 14 dossiers; preserved stable IDs, including 04 for Lunar Landing Site Navigator. Separated core requirements from optional suggestions and NeuraX proposals.
- Published the local [v3 recommendation](rankings/v3-full-brief-six-members.md): Field Shift first, Earth Analog second, MODIS/VIIRS third. This is a recommendation, not a team-approved selection.
- Added [six-member ownership and onboarding](planning/team-workstreams.md), [proposed architecture](planning/architecture.md), and [An–Quang Luật hardware preparation](planning/hardware-preparation.md).
- Created six repo-local planning skills, documented in [the catalog](../governance/skills-catalog.md). Scope is Markdown/Mermaid; no product code, model training, equipment purchase or external assignments.
- Data access/validation, domain sources, availability, equipment inventory, event timing and submission rules are open gates. No spike or live hardware result is claimed.

Earlier entries below preserve the historical decision process. The 2026-10-28 gate was a planned checkpoint, not a completed audit.

## 2026-10-26 — v1 preliminary research

Initial ranking after researching all 14 published summaries:

1. MODIS/VIIRS Hot Spots
2. Dancing with the SARs
3. Earth Analog Locations
4. Earth System Trend Detective
5. Field Shift

At this stage Environmental Science/GIS membership was still treated as conditional.

## 2026-10-26 — team baseline changed

**Vo Thi Ngoc Bich — Environmental Science** is now part of the active team. NeuraX's working structure is:

- Le Nguyen Gia Hung — AI / Team Owner
- Huynh Quoc Viet — AI
- Vo Thi Ngoc Bich — Environmental Science
- Ho Minh Hieu — Software Engineering
- Nguyen Thanh Hang (Tiểu An) — Hardware

This materially changes challenge-fit scoring because environmental validity/GIS context is now a real team capability rather than a hypothetical boost.

## 2026-10-26 — v2 reassessment

The decision lens was expanded to emphasize practical impact, multidisciplinary coverage, simulation/decision-support potential, public competitive overlap, and patterns observed in recent high-performing NASA Space Apps projects.

Updated Top 6:

1. **Field Shift**
2. **Earth Analog Locations**
3. **MODIS/VIIRS Hot Spots**
4. **Dancing with the SARs**
5. **Earth System Trend Detective**
6. **Martian Map**

Working concepts:

- Field Shift → **NeuraX AgroTwin**
- Earth Analog → **NeuraX TerraTwin**
- MODIS/VIIRS → **NeuraX FireSense**

## 2026-10-28 — next decision gate

Do not lock the final challenge before auditing the full official statements/resources.

For the leading candidates, verify:

- exact required deliverable;
- official datasets/resources;
- accessibility and data volume;
- realistic evaluation/ground truth;
- whether AI is necessary rather than decorative;
- whether simulation is native to the challenge;
- competitor differentiation;
- 48-hour end-to-end feasibility.

After this audit, produce ranking v3 and run a small technical feasibility spike for the leading options before final lock.
