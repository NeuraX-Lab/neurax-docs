# Xuất paper và proposal PDF

**Bàn giao Bích:** `build_bich_site_dossier.py` đọc `planning/cases/my-thanh-cai-lay/bich-site-and-demo-dossier.md`, xuất PDF 13 trang riêng (bản 1.3 có bìa, bảng đất-nước-cây-mùa và roles), không ghi đè proposal/hardware snapshot cũ. Dùng logo có sẵn và ảnh địa lý thật có attribution; sơ đồ lab là luồng đề xuất. Metadata PDF chứa SHA Markdown; `.build.json` ghi hash input và output. Theo PDF skill, gọi authoring marker trước khi tạo/edit PDF. Chạy `build_my_thanh_study_block.py` trước nếu thay ranh/coverage cached, sau đó build PDF và render bằng Poppler để review.

Tooling tài liệu, không phải code sản phẩm. Chạy native Windows bằng Python bundled Codex đã có ReportLab, Pillow, pypdf; font Arial trong `C:/Windows/Fonts`. Không dùng conda AI hoặc cài package vào system Python. Không chia sẻ environment với WSL.

Nguồn: `nasa-space-apps-2026/planning/project-brief.md` và `hardware-design-paper.md`. Script tìm repo từ vị trí file; không phụ thuộc đường dẫn checkout cá nhân. `agrotwin_visuals.py` vẽ sơ đồ logic bằng vector; không gọi đây là đã chạy Mermaid engine. Các sơ đồ/wireframe là đề xuất, không phải screenshot thực nghiệm. Ảnh logo/linh kiện dùng assets có sẵn; hình ESP32 là cấu hình dự phòng có nhãn trong hardware paper.

Từ root repo, dùng Python của workspace dependencies:

```powershell
& $taskPython scripts/pdf/build_project_proposal.py
& $taskPython scripts/pdf/build_technical_paper.py
& $taskPython scripts/pdf/build_team_decision_brief.py
```

`$taskPython` là interpreter đã xác minh từ `load_workspace_dependencies`, không là đường dẫn mặc định của mọi laptop. Cần `reportlab`, `Pillow`, `pypdf`; môi trường dùng lần này có sẵn, không cài thêm. Ghi version thực trong review-record khi xuất. PDF metadata có SHA-256 Markdown để kiểm đồng bộ. Source đề xuất và PDF đều phải đổi cùng revision/date khi nội dung thay đổi.

Render mọi trang bằng Poppler `pdftoppm -png -r 85 INPUT OUTPUT_PREFIX`, xem contact sheet và trang quan trọng ở độ phân giải lớn. Kiểm heading/text/links/hash bằng pypdf, `git diff --check`, links Markdown và trạng thái facts. Preview nằm `output/pdf/preview/` được ignore; không thay visual QA bằng chỉ trích text.

Thay source thì build lại cả artifact bị ảnh hưởng. Codex dùng PDF skill marker đúng một lần trước lượt authoring PDF như skill yêu cầu; script không tự gọi marker. Không chạy generator rồi coi data/model/hardware đã được thử.

`build_team_decision_brief.py` đọc planning/team-proposal-2026-11-12.md, tạo PDF riêng phục vụ buổi quyết định sau desk research; không ghi đè proposal tổng thể/hardware. Reference mode trong wireframe giữ nhãn tham chiếu thay hiện trạng thật.

## Nhãn PDF snapshot

`label_snapshot_pdfs.py` thêm một trang cảnh báo vào ba PDF proposal tổng thể/team/hardware, giữ bản trước nhãn trong `output/pdf/archive/pre-current-state-label-2026-11-12/` và ghi hash/page count ở `snapshot-label-manifest.json`. Nội dung gốc không được viết lại hoặc coi là đã đồng bộ. Nếu chạy lại generator cũ sẽ làm mất nhãn, nên sau mọi lần build lại snapshot phải gọi marker và bước label theo PDF skill. Lặp label từ bản archive không cộng thêm nhiều trang. Bản hiện hành để team đọc là PDF Bích 1.3 và `planning/START-HERE.md`.
