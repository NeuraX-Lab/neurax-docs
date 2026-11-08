# Kiểm tra tài liệu — 2026-10-30

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
