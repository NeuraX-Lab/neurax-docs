# NASA Space Apps 2026 — Decision Log

## 2026-11-12 — correction hiện hành: Mỹ Thành, ba reference và roles

Người dùng xác nhận giữ Mỹ Thành; R0 lúa-lúa-lúa, R1 lúa-bắp non-lúa, R2 lúa-đậu xanh-lúa là chuỗi tham khảo từ nghiên cứu vùng, không là baseline/thực hành đã xác minh tại block. Hưng-Việt cùng core/features/pipeline/kiến trúc/output demo; Bích Data/review src/features; Hiếu backend remote gián đoạn; An ESP/sensor demo; Luật thống kê/đánh giá/QA từng block. Các quyết định đề nghị về Đức Lập/cây khác ở log bên dưới là lịch sử, chưa thay correction này.

[START-HERE](planning/START-HERE.md) dẫn nguồn hiện hành. Trước T0 chỉ chuẩn bị/nghiên cứu theo rules; project sau giờ mở. NASA-to-comparison rule, điều kiện cây/nước và lịch giống còn thiếu; không tự chấm score/hiệu quả khi thiếu căn cứ. Các PDF proposal cũ đã có trang cảnh báo snapshot.

## 2026-11-12 — kết thúc vòng desk research, đề nghị scope prototype

Theo yêu cầu nghiên cứu tới mức propose với team, đã đối chiếu event mưa bằng ERA5 (qua Open-Meteo): 17,3 mm ngày 14/06 so POWER 494,17; sáu ngày 65,2 so 651,17 mm. Khác support, chưa ground truth, giữ WARN và raw. IAS cung cấp thêm cơ cấu mè, duration candidate và áp dụng lịch sử tại Đức Hòa. Đã tính exposure một cửa sổ giả định 75 ngày từ 15/01 trên 11 năm NASA; không là forecast hoặc water-deficit model.

Đề xuất quyết định: build reference/sandbox prototype với REF-RICE, REF-MAIZE (chuỗi ghép thiết kế), REF-SESAME (cấu trúc có nguồn), conditions/unknown/evidence và sensor tile riêng. R0 thực vẫn null. Đề xuất được đóng gói trong planning/team-proposal-2026-11-12.md và PDF riêng; đây không là ghi nhận team đã thông qua. Nhánh farm-specific chỉ mở sau soil/water/calendar/baseline review. Không tự liên hệ nông dân/chuyên gia hoặc nộp bài.

## 2026-11-12 — audit case và NASA theo yêu cầu người dùng

Đã tải NASA POWER Daily 2015–2025 tại điểm tham chiếu GeoNames Đức Lập Hạ, không là thửa đất. 4.018 ngày/16.072 giá trị qua kiểm completeness/unit/time và tính nhất quán; QA tổng thể WARN với mưa 494,17 mm/day ngày 14/06/2020 cần cross-check, không tự xóa. Raw, hash, manifest, CSV và script audit được lưu trong repo.

Nguồn khuyến nông mới xác nhận bắp chuyển đất lúa tại Đức Lập Hạ lịch sử. Khuyến nghị review C-MAIZE và C-SESAME, giữ C-PEANUT candidate; chưa là team chốt cây hoặc rotation. R0 vẫn null vì chưa có hộ/thửa/chuỗi thực tế; không đủ khóa hiện trạng + hai rotation cùng thửa. Xem case README và JSON trong planning/cases/duc-lap. Các PDF trước đó không tự được coi là có kết quả sample mới; giữ snapshot, cập nhật khi khóa evidence.

## 2026-11-12 — người dùng giao cải thiện phương án và đồng bộ PDF

Người dùng yêu cầu nâng chất lượng để cạnh tranh local và hướng tới global, cập nhật docs/PDF theo trao đổi. Nông dân là user đã xác nhận; HTTPSLAB đã đồng ý cho mượn theo người dùng và đang chờ thông số. Giữ Field Shift. Khuyến nghị mới: case Đức Lập Hạ cũ, farm 2D cho so luân canh, ba tương tác why-not/điều kiện đổi ý/missing và evidence packet; sensor thật ở ô live riêng.

[Kế hoạch local/global](planning/local-to-global-strategy.md) ghi owner, gate, protocol đánh giá và cắt scope. Đây là phương án đề xuất được soạn theo yêu cầu, chưa suy toàn đội đã phê duyệt hoặc có sản phẩm chạy. Proposal 0.4 và hardware paper 0.3 đồng bộ ngày 12/11; không hứa giải hay tính độc nhất. Luật/format HCMC và global 2026 còn cần BTC xác nhận.

## 2026-11-07 — proposal sơ bộ toàn dự án

Theo yêu cầu người dùng, mở rộng [project-brief.md](planning/project-brief.md) thành proposal 0.3 của toàn AgroTwin và xuất [PDF A4](../output/pdf/NeuraX-AgroTwin-Preliminary-Proposal.pdf) từ cùng nguồn. Nội dung gồm người dùng/giả định, phạm vi, DATA/K1, baseline và ví dụ synthetic, UX, architecture, evaluation, ownership, phase, nguồn lực, rủi ro và acceptance. Paper hardware của An giữ vai trò tài liệu subsystem riêng.

Đây là baseline để review, chưa xác nhận team approve toàn bộ scope hoặc có dữ liệu/model chạy. Không đổi quyết định chọn Field Shift; chưa chốt vùng/cây, NASA sample, nông học, inventory, availability hay giờ/luật local. Kế hoạch còn lại tính từ 07/11, không coi các mốc trước đó đã hoàn thành. Bước tiếp theo giải các gate người dùng/vùng/cây, K1, NASA sample và evaluation trước build theo thời gian được phép.

## 2026-11-06 — bộ skill dùng lại và thống nhất tài liệu nội bộ

Người dùng xác nhận repo này dùng nội bộ, yêu cầu search/cài skill phục vụ mục tiêu thi tốt. Đã cài jupyter-notebook từ openai/skills và geomaster, statistical-analysis, scientific-critical-thinking từ K-Dense ở revision pin trong [catalog](../governance/skills-catalog.md). Không cài scientific runtime, không build sản phẩm.

Sáu skill được mô tả trước đây không có trong checkout do `.agents` bị ignore. Tạo lại sáu workflow theo tài liệu hiện hành và thêm pitch-review; theo dõi cả bảy trong Git. Tài liệu nội bộ dùng tiếng Việt, giữ nguyên nguồn tiếng Anh và lịch sử; bản đối ngoại chuẩn bị riêng. Không đổi visibility GitHub.

Bản Field Shift gửi lại trùng bản đã lưu sau chuẩn hóa khoảng trắng, không có Resources mới; xem [intake](sources/challenge-intake.md). Giữ quyết định chọn Field Shift; đồng bộ v4/workflow index, thêm [playbook](planning/competition-playbook.md) và ghi rõ giới hạn xác minh luật 2026. Không xem skill như bảo đảm thắng giải.

## 2026-11-04 — team chọn Field Shift

Người dùng xác nhận team NeuraX đã chọn **Field Shift: Adapting Farms with NASA Data**. Ghi nhận quyết định này thay trạng thái “khuyến nghị, chưa chốt” trong [final-selection](final-selection.md). Chưa có biên bản biểu quyết từng thành viên trong repo; không suy ra dữ liệu, vùng/cây, product NASA hoặc quy tắc nông học đã được xác minh.

Bước tiếp theo: chốt một vùng và phạm vi cây/đất có nguồn; kiểm NASA POWER hoặc nguồn EO phù hợp bằng sample, unit, coverage và provenance; chỉ sau đó khóa D1/K1/A1 trong repo sản phẩm. Forecast, sensor và phương án luân canh thực tiếp tục qua các gate riêng.

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
