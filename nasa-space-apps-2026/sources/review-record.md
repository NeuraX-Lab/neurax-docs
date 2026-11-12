# Kiểm tra tài liệu — 2026-10-30

## 2026-11-12 — inventory repo, kiểm toolkit thật và cho phép tiếp tục

- Người dùng báo đã confirm BTC và yêu cầu cứ làm/commit/push; ghi user-reported authorization, không hỏi lại cùng quyền và không bịa văn bản sửa global rules. Gói Resources mới ngày mai theo kỳ vọng người dùng chưa có; snapshot POWER/SoilGrids công khai đã có.
- Ba checkout local: docs; fieldshift-lab; readiness-kit cùng origin/commit lab cũ, 86 file khớp bỏ CRLF. Lab đã fast-forward main ddc6512 có AI-first/native review. Chọn lab chính, giữ readiness-kit nguyên. Không có .NET/C# trong ba checkout. Product main/dev trên GitHub mới là docs scaffold, .github là org profile cũ; chưa sửa hai repo remote đó.
- Tạo native Windows .venv riêng lab theo dependency, không đổi system/WSL. 15 tests pass sau sửa test SQLite đóng connection đúng; synthetic workflow partial/blocked khi thiếu evidence. POWER thật 4018ngày ->132tháng, independent monthly sums pass, SHA/UTC/unit đúng; source rain WARN giữ trong manifest. API TestClient 200 status/fit/inventory, forecast chưa train404. Không gọi model phụ/thuê API, không training NASA, không browser/server/dashboard/ESP test.
- Lab context/roles đồng bộ MyThanh/HVjointcore/BichData/HieuBackendremote/AnESP/LuatblockQA. Vẫn thiếu K1/approval ingestion/ranking/domain rule; không bypass guardrails. Thêm runtime snapshot/check script/Windows CI cho toolkit.
- Thêm `repository-inventory-and-next-step-2026-11-12.md` và nội dung email `bich-review-message.md`. Đã nghiên cứu tài liệu CTU cho reference và gói review1.3; chưa có review của Bích hoặc data mới. Chưa gửi email, không có địa chỉ xác định. Docs integrity recheck pass với 5 upstream warnings; không tạo PDF mới trong lượt này.


## 2026-11-12 — kiểm định tổng thể challenge/data/flow/roles/MD-PDF-ZIP

- Thêm `planning/full-readiness-verification-2026-11-12.md`: traceability theo brief đã cung cấp, flow/owner/artifact/gate, walkthrough không số giả và việc còn lại. Chính thức vẫn 502, GO Team rules đã đọc lại; không giả Resources/local agenda được verified.
- Sửa workflow hiện hành còn Đức Lập, baseline/is_current như đã biết và ownership cũ; cập nhật final-selection/decision-log theo Mỹ Thành. Contract thêm source_kind/evidence_scope, is_current=null và score=null khi thiếu. Chốt NASA feature phải liên hệ phép so có căn cứ; chart riêng chưa đủ, core chưa hoàn tất.
- PDF Bích 1.3 vẫn 13 trang, bìa và vai trò giữ đúng; thêm gate NASA-to-comparison, bỏ lời văn như node đã chứng minh chạy. Ba notice PDF snapshot trỏ 1.3, các trang gốc giữ nguyên. ZIP 26 entries đồng bộ; sửa bốn link profile bị hỏng.
- Script audit cached-source integrity kiểm Markdown NASA/team/root, links/fences, 16 raw hashes/4018days/units constraints, geometry nguồn/pixeltransform/KML/15soilcellvalues,12CSVrows/PDFsourcehashes/snapshotoriginaltext/ZIPCRC-hash-links. Kết quả lưu consistency-audit.json, 5 warning link upstream giữ nguyên. Render/review toàn bộ PDF hiện hành và ba notice. Không model/product/user/hardware/field test; không cài dependency, push hoặc gửi liên hệ.


## 2026-11-12 — gỡ mâu thuẫn tài liệu và tách bản hiện hành/snapshot

- Tạo `planning/START-HERE.md`: một điểm bắt đầu, trạng thái case, ba tài liệu cần đọc, vai trò đã chốt và việc tiếp theo; không tạo proposal mới. README gốc/index trỏ tới đây.
- Rút gọn team-workstreams về phân công hiện hành và remote handoff; sửa ownership UI/contract/QA trong architecture, workflow index và audit. Bỏ chỉ dẫn cũ Hiếu tự chủ UI/deploy và Việt tự chốt toàn bộ; giữ Hưng-Việt cùng core/UI khi cần, Bích Data, Hiếu backend remote gián đoạn, An demo ESP, Luật thống kê/đánh giá từng block.
- Đánh dấu proposal tổng thể/team/hardware, intake/case strategy cũ và workflow không chọn là snapshot/tham khảo. Không viết lại nghiên cứu lịch sử thành kết quả Mỹ Thành. Ba PDF snapshot thêm một trang cảnh báo có case/roles hiện hành; archive giữ bản trước nhãn, manifest ghi SHA và số trang. Bản PDF Mỹ Thành 1.2 không thay nội dung, vẫn 13 trang.
- Kiểm 103 link entry/current, Markdown fences, hash archive/output, và text của toàn bộ trang gốc trong ba PDF vẫn khớp sau thêm notice. Render/kiểm ba trang notice; PDF Mỹ Thành và các input hash không đổi. `git diff --check` đạt. Không build sản phẩm/model, nghiên cứu thêm, cài dependency, commit/push hoặc gửi tin.


## 2026-11-12 — sửa phân công theo người dùng và Hiếu remote

- Bản roles/PDF 1.2: Hưng-Việt cùng đóng góp chính, cùng features/pipeline/kiến trúc/output demo. Hưng workflow/scope Data -> AI; Việt technical AI/Data Analysis. Bích làm Data và review features/src; Hiếu backend; An demo ESP/sensor; Luật thống kê/đánh giá từng block và hỏi owner để nắm workflow, tình hình, blocker.
- Hiếu không dự trực tiếp hai ngày theo lời chuyển, làm remote nhưng có lúc offline; chưa biết khung online. Hưng-Việt cùng UI/UX và hỗ trợ/tiếp quản backend khi cần, giữ contract/handoff/cách chạy để demo không chờ phản hồi ngay. Không tự xác nhận đủ điều kiện dự remote thay BTC.
- Đồng bộ team-profile, team-workstreams, roles, ownership workflow/architecture; các bảng idea cũ được ghi snapshot. Giữ bảng đất-nước-cây-mùa và ô review trống; không nghiên cứu địa bàn mới. PDF giữ 13 trang/bìa, ZIP đồng bộ; không triển khai sản phẩm, push hoặc gửi liên hệ ngoài.


## 2026-11-12 — bảng review R0/R1/R2, bìa PDF và vai trò

- Theo yêu cầu mới nhất, giữ Mỹ Thành; tạo `rotation-evidence-for-bich.md` và CSV 12 hàng đất/nước/cây/mùa. Tách HISTORICAL/MODEL/UNKNOWN/SCENARIO, có câu hỏi và gate. Bích chưa review: các cột reviewer/decision/note/date để trống. Không thêm ngưỡng nông học, số ngày giống hoặc % tiết kiệm nước chưa có bằng chứng.
- Đọc lại methods/bảng mùa CTU 597 từ cache đã tải và CTU 605 từ nguồn trường. R0/R1/R2 là đối chứng/chuỗi lịch sử, không là hiện trạng block. Không đổi bắp non thành bắp hạt hoặc đậu xanh thành đậu phộng. Không ghép hai bài thành cùng thửa.
- Cập nhật PDF bàn giao 1.1, 13 trang gồm bìa navy/teal/logo theo mẫu proposal có sẵn, 12 mục nội dung với bảng riêng cho ba phương án và vai trò sáu người. Nguồn Markdown dùng include để giữ bảng/roles một bản. Metadata/hash manifest bao gồm các file include và CSV. ZIP đã đồng bộ.
- Vai trò giữ Việt TL/DATA+AI; Hưng Team Owner/AI; Bích K1; Hiếu software/deploy; An H1; Quang Luật QA/đánh giá. Ghi rõ chuẩn bị trước T0 và triển khai sau T0 theo hướng dẫn GO Team. Không xác nhận giờ rảnh/kỹ năng hoặc khả năng thiết bị chưa có thông số.
- Native Windows/bundled runtime; không cài dependency hoặc chạy sản phẩm/model. Render đủ trang, rà contact sheet, bìa, trang R1 và roles ở cỡ lớn; sửa mép bìa. Kiểm links, 12 CSV rows/cột review trống, PDF sections/pages và input/output hashes. Chưa push hoặc gửi tin cho ai.

## 2026-11-12 — sửa polygon và bàn giao địa bàn/demo cho Bích

- Hạ hình thoi 17 ha cũ xuống illustrative. Giữ ranh xã nguồn AOI-MT-ADMIN-v1, thêm MT-BLOCK-01 khoảng 1,996 ha số hóa theo mép khối canh tác nhìn thấy trên ảnh 2025. Cạnh được review thị giác, không là ranh thửa/đất đồng nhất đã kiểm; có thể chứa nhiều ô nhỏ.
- Lấy riêng 15 giá trị SoilGrids tại tâm block mới từ cache và lưu SHA/raw values/CSV. Không có mẫu đất hoặc EC/nước ruộng; không tái dùng giá trị điểm cũ như đo tại block. Demo đất tại HCM có nhãn lab, không bắt buộc lấy đất Mỹ Thành.
- Tạo hồ sơ Markdown và PDF nghiên cứu riêng 9 trang gửi Bích, có logo, bản đồ xã/block, tọa độ, quy trình lab, backup, R0/R1/R2 tham khảo, ENSO có ngày, so sánh Cần Giờ và bảng câu hỏi cụ thể. Không ghi đè proposal tổng thể/hardware snapshot cũ.
- Native Windows bundled Python 3.12.14/Pillow 13.0.0, ReportLab/pypdf, Poppler. Không cài dependency mới hoặc gọi lại API dữ liệu. Geometry/CSV/KML, links, source hashes và PDF metadata được kiểm; đã render và rà mọi trang, sửa danh sách bước demo thành các đoạn riêng. Chưa kiểm thiết bị/model/nông học thực địa. Chưa commit/push hoặc gửi cho người khác.

## 2026-11-12 — đề xuất để team quyết định sau desk research

- Hoàn tất vòng nghiên cứu công khai để đề nghị scope, không tự nhận field validation. Thêm team-proposal-2026-11-12.md và PDF riêng 1.0: reference/sandbox prototype, ba menu có provenance, farm-specific gated, method, demo, owner, gate và buổi họp đề xuất. R0 thật vẫn null, không có team approval tự sinh.
- ERA5 models=era5 qua Open-Meteo, daily UTC 12–17/06/2020: ngày 14/06 là 17,3 mm so POWER 494,17; tổng cửa sổ 65,2 so 651,17 mm. Lưu raw/retrieval/CSV/summary; grid/support khác, giữ warn_model_disagreement_unresolved, không sửa NASA hoặc coi một model là truth.
- IAS mè ĐH-1 có thêm cấu trúc mùa và duration candidate; reference menu giữ ba chuỗi season-tag, ghi rõ chuỗi bắp là ghép thiết kế chưa được xác nhận cùng thửa. Nhãn UI tham chiếu thay hiện trạng thật. Giữ nguồn lịch sử, không chuyển thành khuyến cáo 2026.
- Tính exposure từ raw NASA cho cửa sổ giả định 15/01 dài 75 ngày trên 11 năm: rain median 12 mm, mean 27,42 mm, min/max 0,35/112,84; T2M mean 29,295 C. Không có ET/soil storage/irrigation nên không water-deficit/forecast/yield claim. Hai ví dụ calendar 90/75 ngày trống là synthetic, arithmetic kiểm riêng và overall unknown vẫn giữ.
- PDF đề xuất 9 trang A4, 12 bookmarks, bảy source references, source hash khớp. Render đủ trang, rà contact sheet và trang bảng ở kích thước lớn; sửa wrap ngày trong bảng trước xuất cuối. Không ghi đè hai PDF proposal tổng thể/hardware snapshot trước.
- Cached replay event/exposure giữ nguyên hash; raw/script hash khớp, JSON và arithmetic/reference baseline checks đạt. Rà checkout 361 relative links không thiếu, 13 JSON file parse đạt; fences/git diff --check đạt. Nghiên cứu/script audit native Windows Python standard library; không cài dependency mới, không build sản phẩm/model/sensor hoặc gửi liên hệ ngoài.

## 2026-11-12 — audit thực tế case Đức Lập và sample NASA

- Lấy NASA POWER API v2.10.3 tại 10.91123 N / 106.44351 E, tham chiếu địa danh GeoNames, không farm. Period 2015–2025 UTC; bốn biến T2M/T2M_MAX/T2M_MIN/PRECTOTCORR; raw 268.042 bytes, 4.018 ngày, 16.072 giá trị. File raw/retrieval/manifest/QA/dictionary và daily/monthly/annual/reference CSV trong sources/data-audits/duc-lap-2026-11-12.
- Không thiếu keys/fill/nonfinite/duplicate JSON key; units/time/order/sign và tổng tháng so ngày đạt. Quality WARN: PRECTOTCORR 494,17 mm/day ngày 14/06/2020 vượt threshold review khám phá 200, chưa chứng minh sai. Không sửa raw; sensitivity bỏ đóng góp ngày đó không là corrected data hoặc dữ liệu dùng rank. Chưa cross-check trạm/GPM đúng support/time.
- Đọc nguồn địa phương primary bắp Đức Lập Hạ 2013–2014, đậu phộng 2015–2016; bản tin 11/2016 có rice-sesame structures cấp Long An; đọc nghiên cứu bắp và luận văn đất/suitability. Đã bắt lỗi scope: câu vụ bắp Xuân Hè ở nghiên cứu nằm trong đoạn Đồng Tháp, không chuyển sang Đức Lập. Bản đồ đất cũ trong luận văn chưa có MapInfo, chưa có pH/texture tại thửa. HARC PDF trả HTML; một số FAO crop URLs 404/redirect; native download PDF địa phương gặp TLS verify fail, không tắt xác minh.
- Thêm case sheet và candidate register JSON. R0 null, hai hướng bắp/mè là menu review, đậu phộng candidate; chưa có recommendation/score. Update index/workflow/decision-log, giữ PDF trước audit làm snapshot có nhãn.
- Audit script dùng standard-library Python 3.12.14 native Windows, không cài GIS/science runtime; không huấn luyện model hoặc thử sensor. Cách chạy ở scripts/research/README.md. Cached replay cho 10 file JSON/CSV giữ nguyên hash; raw và script hash khớp manifest; row counts daily/monthly/reference/annual là 4018/132/12/11. Rà 334 relative links không thiếu, tám JSON file parse đạt, fences và git diff --check đạt. WARN vẫn còn, không diễn giải replay/check pass là data validity hoặc nông học pass.

## 2026-11-12 — chiến lược local/global và xuất PDF đồng bộ

- Thêm local-to-global-strategy.md: case Đức Lập đề xuất, ba tương tác vì sao loại/khi nào đổi ý/còn thiếu gì, owner, gate, cắt scope, gói review độc lập và protocol usability nhỏ. Đây là kế hoạch, chưa là kết quả đội thi hoặc cam kết giải.
- Proposal 0.4 tích hợp thông tin người dùng, vùng, ENSO, HTTPSLAB, audit novelty/winners và kế hoạch hành động; PDF 33 trang A4, 24 bookmarks, 15 nguồn trong source register, thêm farm wireframe và chuỗi evidence, vẽ lại kiến trúc lớn bằng vector. Paper An 0.3 có 22 trang, 22 bookmarks, intake thiết bị mượn; ESP32/wiring/ảnh cũ là cấu hình tham chiếu backup. Cả hai có logo/theme, ngày 12/11 và SHA-256 source khớp metadata.
- Đồng bộ README/index, decision-log, architecture, workflow và hardware preparation. Sửa hai link PDF brief cũ bị thiếu trong checkout sang paper hiện hành. .gitattributes đánh dấu PDF là binary; .gitignore bỏ cache Python và giữ preview ngoài Git.
- Lưu generator và sơ đồ trong scripts/pdf, kèm cách chạy/QA. Native Windows bundled Python 3.12.14, ReportLab 4.4.9, Pillow 13.0.0, pypdf 6.21.4; không cài dependency hoặc chọn runtime sản phẩm. Chạy build_project_proposal.py/build_technical_paper.py rồi render toàn bộ bằng Poppler; rà contact sheets cả 55 trang và trang kiến trúc/farm/intake ở kích thước lớn, không thấy chồng/cắt hoặc lỗi font. Sau sửa pagination proposal, đã render lại và rà phần thay đổi.
- Check heading đủ 24/22, không có replacement glyph, source hash khớp. Rà links Markdown toàn checkout: 312 link tương đối, không còn đích thiếu sau sửa; năm JSON blocks hợp lệ; scripts Python parse và build đạt; git diff --check đạt. Mermaid được minh họa lại bằng vector, chưa xác nhận bằng Mermaid engine.
- Resources live 502 và trang HCMC không đọc được trong lượt thử; chưa xác nhận guide 2026 đầy đủ. Không tải/kiểm sample NASA, chạy model/hardware hoặc user test. Các source đã đọc không thay case sheet/K1 thật. Chưa commit/push.

## 2026-11-12 — audit nhánh docs, đội thắng và tính mới

- Fetch origin; nhánh docs/skills-and-alignment-2026-11-06 tại 1472b6c đồng bộ remote cùng nhánh (0/0); main tại 7d691d3. Giữ các thay đổi working tree; không commit/push/merge.
- Thêm hồ sơ trong past-winners và competitor-research; cập nhật index và cảnh báo novelty trong proposal. Nguồn global NASA 2024/2025, local Ninh Bình/BTC SEPA, NCI Dublin và BTC Seattle; tách giải local, nominee và giải global. HCMC chưa đủ nguồn winner/project để kết luận.
- Đọc README Orion commit 4a80fa8ddb7dab99e2bf27cdfb95432a94fe6001 và GreenOrbit commit c9b3961caaa061a8a3af28963f7743bcdbecf91f qua GitHub connector. Orion có ENSO/provenance/scenario; MODEL_CARD vẫn ghi validating khác mức khẳng định built của README. Không chạy tests/metrics của đối thủ.
- Kết luận: nhiều thành phần AgroTwin có tiền lệ; giá trị địa phương và flow quyết định là giả thuyết cần chứng minh. Chưa chứng minh độc nhất hoặc ưu thế kỹ thuật. Có lời judge local NCI được đăng; các nguyên nhân thắng global vẫn là suy luận, không có phiếu điểm.
- Trang project Space Apps và một số nguồn địa phương lỗi 502/timeout; không giả vờ đã đọc video/deck/code đầy đủ. Không xuất lại PDF; proposal đã báo PDF chưa chứa review mới.
- git diff --check cho Markdown đạt. Không tải/kiểm sample NASA, không chạy model/sensor/user test trong lượt audit.

## 2026-11-07 — proposal tổng thể và PDF cùng nguồn

- project-brief.md được viết lại thành proposal 0.3: khoảng 7.500 từ theo tách khoảng trắng, 20 phần chính và hai phụ lục. Giữ ownership schema/method ở architecture/workflow, hardware chi tiết ở paper An. Chưa chốt thêm quyết định team hoặc triển khai sản phẩm.
- PDF NeuraX-AgroTwin-Preliminary-Proposal.pdf có 24 trang A4, logo/theme, mục lục với 23 bookmark, bốn nguồn ngoài và sáu visual tương ứng Markdown. Bốn flow Mermaid trong nguồn được minh họa lại bằng vector ReportLab; không gọi đó là đã render/validate bằng Mermaid engine.
- Bảng/weights synthetic được đọc từ Markdown để vẽ chart. Đã tính lại hai bộ score: 0.5050/0.7350/0.6775 và 0.6200/0.6600/0.7400; đây là arithmetic minh họa, không metric thật. PDF metadata lưu SHA-256 nguồn và đã đối chiếu khớp; mọi heading chính có trong text PDF.
- Đọc NASA Science, POWER Daily/Monthly và FAO Species diversification ngày 07/11. Trang challenge live 502; không gọi Resources/sample verified. Nguồn nông học tổng quát không được biến thành rule cây/vùng đã xác nhận.
- Render đủ 24 trang bằng Poppler, rà contact sheets và trang chart ở kích thước lớn; không phát hiện chồng/cắt, lỗi font tiếng Việt hoặc thiếu nội dung. Kiểm nội bộ tại lượt chính: 282 liên kết tương đối có đích, fences và JSON hợp lệ, git diff --check đạt. Những link thêm vào log sau lượt này được rà tiếp khi bàn giao.
- Runtime dùng Python/ReportLab/Pillow/pypdf bundled Windows như các lượt PDF trước; không cài dependency mới. Generator tạm `%TEMP%/neurax-agrotwin-brief-20261106/build_project_proposal.py`; nguồn dài hạn là project-brief.md, preview trong output/pdf/preview/proposal/ được ignore. Không chạy hardware/data/model, chưa commit/push.

## 2026-11-06 — sửa brief thành paper kỹ thuật sau review

- Người dùng yêu cầu thuyết minh chi tiết, lý do lựa chọn và backup thay vì brief trực quan đơn giản. Thêm hardware-design-paper.md làm nguồn chính; PDF A4 mới NeuraX-AgroTwin-Technical-Paper-An.pdf có 21 trang, khoảng 2.54 MB, 18 phần chính và hai phụ lục. Brief sáu trang giữ làm tóm tắt phụ trợ; README/index/BOM đã trỏ tới paper chính.
- Mở rộng project-brief.md với lập luận scope/baseline, phase P0–P6, gate, backup và nghiệm thu giai đoạn chuẩn bị. Không tuyên bố phase build đã hoàn tất.
- Paper giải thích probe/MCU/sensor bổ sung/display, alternatives theo inventory, USB/Wi-Fi, nguồn/ADC, calibration hai tầng, thiết kế phép thử, trạng thái lỗi, backup B0–B4, risk matrix, BOM và phân công. Mọi số lấy mẫu/timeout pilot là đề xuất; ví dụ JSON là synthetic. H1 0.2-proposed được ghi là đề xuất mở rộng, chưa đổi schema hiện hành ngầm định.
- Đọc nguồn DFRobot, Espressif, Adafruit, Arduino và NASA POWER; tám mục tham khảo có URL. Thông số hãng tách khỏi suy luận/thiết kế NeuraX, không báo giá hay xác nhận tương thích mọi module.
- Đã render bản cuối và rà đủ 21 trang qua contact sheets; xem thêm trang board, contract JSON, backup và references ở kích thước đầy đủ. Chữ Việt, bảng, sơ đồ, ảnh, mục lục/bookmarks và nguồn hiển thị được, không phát hiện chồng/cắt nội dung.
- Tạo bằng ReportLab/Pillow trong runtime bundled Windows; script tạm `%TEMP%/neurax-agrotwin-brief-20261106/build_technical_paper.py`. Render bằng Poppler; bản nguồn dài hạn là Markdown paper. Chưa chạy hardware/model hoặc phép đo thực. Chưa commit/push.

## 2026-11-06 — phân tích dự án và PDF hardware cho An

- Theo yêu cầu mới, thêm project-brief.md với flow sơ bộ, phân công và ranh giới node/NASA; hardware-demo-brief.md là nội dung nguồn cho PDF sáu trang. User yêu cầu PDF và hình ảnh, nên scope lượt này gồm artifact PDF và asset ảnh; không thêm code sản phẩm.
- PDF dùng logo do người dùng cung cấp; ảnh mẫu SEN0193, ESP32-S3 và SHT31 từ DFRobot, Espressif, Adafruit có nguồn tại brief. Không giả inventory, giá, wiring đã thử hoặc ảnh hệ thống đã lắp.
- Chốt mức tối thiểu một probe ẩm đất + ESP32/USB và laptop; SHT31/OLED tùy chọn. Sensor bàn demo là context riêng, không tự thay ranking của vùng. Kịch bản 90 giây là rehearsal nội bộ, không phải giới hạn demo BTC.
- Tạo bằng ReportLab/Pillow trong Python bundled runtime Windows; render bằng Poppler pdftoppm. Đã xem đủ sáu trang PNG, kiểm tiếng Việt, ảnh, khoảng cách và nguồn; PDF sáu trang, khoảng 2.4 MB, text trích được, ba link nguồn ngoài truy cập từ PDF.
- Bản PDF tại output/pdf/NeuraX-AgroTwin-Hardware-Brief-An.pdf; asset gốc tại output/pdf/assets/. Preview kiểm bố cục ở output/pdf/preview/ được ignore. Generator tạm ở `%TEMP%/neurax-agrotwin-brief-20261106/build_brief.py`; nội dung dài hạn để sửa là project-brief.md và hardware-demo-brief.md.
- Runtime: `C:/Users/ghcoo/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`; renderer `dependencies/native/poppler/Library/bin/pdftoppm.exe` cùng bundle. Gói dùng: reportlab, Pillow, pypdf có sẵn; không cài thêm dependencies hay firmware. Khi chỉnh PDF, chạy generator trong runtime tương ứng, render lại và kiểm ảnh trước bàn giao.

## 2026-11-06 — cài skill và đồng bộ tài liệu nội bộ

- Nhánh local `docs/skills-and-alignment-2026-11-06`; chưa commit/push. Không chạy data/model/hardware.
- Bảy skill NeuraX mới qua `quick_validate.py` của skill-creator; jupyter-notebook đã cài cũng qua validator này. Ba skill K-Dense có field compatibility mà validator cũ không hỗ trợ: đã parse YAML/name/description và Python AST của helper; không gọi đó là đạt validator chuẩn.
- Bốn skill ngoài cài bằng skill-installer, pin revision và SHA-256 entrypoint trong catalog; license được giữ/bổ sung. Chưa chạy scientific helper trên dữ liệu thực, chưa cài scientific runtime. Chỉ tạo venv QA tạm ngoài repo với PyYAML 6.0.3 để kiểm skill.
- Kiểm toàn bộ Markdown lần cuối: 237 link tương đối có đích, bốn JSON block parse được, code fences đóng đủ, không có ký tự thay thế UTF-8. `git diff --check` đạt. Mermaid không đổi và chưa render trong lượt này.
- File Field Shift gửi lại khớp nguyên văn đã lưu sau chuẩn hóa khoảng trắng; không thêm bản trùng. Resources đầy đủ và sample vẫn chưa có.
- Đồng bộ trạng thái selected, ghi v4 là căn cứ trước quyết định, index workflow có Field Shift chính và hai fallback. Nội bộ tiếng Việt, nguồn/thuật ngữ và snapshot lịch sử giữ tiếng Anh; bản đối ngoại chuẩn bị riêng.
- Đọc thông báo NASA 2026 và PDF judging 2025. Search local-event 2026 có tên năm tiêu chí nhưng trang trực tiếp trả lỗi; chưa xác minh bộ luật toàn cầu 2026/HCMC. Không áp giới hạn demo hoặc quy định năm cũ như quy định hiện hành.
- Catalog cũ nói sáu skill đã có nhưng checkout không chứa chúng; đã tạo lại theo docs, thêm pitch-review và bỏ `.agents` khỏi ignore. Không tuyên bố khôi phục nguyên bản file cũ.

## Lượt cập nhật workflow, Quang Luật và Việt Technical Lead

Đã kiểm lại sau các yêu cầu bổ sung trong ngày 2026-10-30:

- 211 liên kết nội bộ hợp lệ; 4 ví dụ JSON parse được; phép tính synthetic similarity/harmonization khớp mô tả.
- 14 phần nguyên văn đề còn khớp nguồn; SHA-256 file đầu vào không đổi.
- Tên hiển thị Quang Luật đã thay thống nhất; 14 bảng phân công có Việt — Technical Lead / DATA + AI, và vai trò QA/thống kê của Quang Luật.
- Cả ba workflow cập nhật Việt trực tiếp làm AI cùng Hưng; owner/schema/timeline được rà đồng bộ. Năm sơ đồ Mermaid kiểm cấu trúc cục bộ, chưa render bằng engine.
- Sáu skill kiểm frontmatter cơ bản; không tuyên bố đã chạy validator chuẩn thiếu PyYAML của lượt trước.
- `git diff --check` đạt; toàn bộ 44 file thay đổi hoặc mới trong working tree là Markdown, gồm cả phần việc từ lượt trước. Chưa commit/push, chưa chạy data/model/hardware thực.
- Ngày sự kiện 14–15/11/2026 có nguồn NASA/CSA; địa điểm NOVAWORLD do team cung cấp. HCMC 2025 có nguồn ngày/venue nhưng chưa tìm được agenda theo giờ; giờ trong kế hoạch mới đều là giả định nội bộ hoặc mốc cần xác minh.

## Lượt kiểm trước cập nhật workflow

Phạm vi: docs và skill Markdown trên nhánh local `docs/update-challenges-and-team`. Chưa commit/push; chưa triển khai sản phẩm hay chạy data/model/hardware spike.

| Kiểm tra | Kết quả |
| --- | --- |
| 14 mục trong nguồn → 14 dossier | Đủ, không trùng; mapping Lunar Landing giữ ID 04 |
| Nguyên văn bản đề | 14/14 phần khớp nội dung nguồn sau chuẩn hóa xuống dòng và bỏ khoảng trắng đầu/cuối phần |
| Phân công trong mỗi dossier | Cả 6 thành viên đều có đầu ra riêng |
| Link Markdown nội bộ | 143 liên kết đã kiểm ở lượt kiểm chính, không có đích thiếu |
| Rubric v3 | 14 dòng được tính lại theo trọng số, tổng và thứ tự khớp |
| 6 skill | Kiểm cục bộ tên thư mục/name, description, frontmatter đơn giản và placeholder đạt |
| Validator chuẩn skill-creator | Đã thử; không chạy được do môi trường thiếu PyYAML. Kiểm cấu trúc cục bộ thay thế không phải chứng nhận của validator này |
| Mermaid | 3 sơ đồ đã rà cấu trúc cục bộ: flowchart direction, quote/bracket và subgraph/end; chưa render bằng engine |
| UTF-8 / code fences | Không có ký tự thay thế; fence đóng đủ |
| Git whitespace | `git diff --check` đạt sau sửa |
| Scope repo | Nội dung ngoài `.git` chỉ là `.md`; không thêm code sản phẩm |

Bước render/parse trong trình duyệt có tải thư viện CDN đã bị automatic approval review từ chối vì rủi ro đưa nội dung repo vào môi trường đó. Đã chuyển sang kiểm cục bộ, không thực hiện payload bị từ chối. Việc lấy dependency kiểm tra vào thư mục tạm không hoàn tất và đã dừng; không cài dependency vào repo. Không tuyên bố đã render các sơ đồ hoặc chạy validator chuẩn thành công.

Các giới hạn nghiên cứu còn lại ở [challenge-intake.md](challenge-intake.md); gate quyết định ở [v3](../rankings/v3-full-brief-six-members.md). Tài liệu này ghi kết quả kiểm docs, không xác nhận mô hình hoặc hệ thống đã hoạt động.
