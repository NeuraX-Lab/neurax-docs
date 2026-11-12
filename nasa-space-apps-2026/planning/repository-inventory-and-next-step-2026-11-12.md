# Repo hiện có, phần đã chạy và bước tiếp theo

> 12/11/2026. Người dùng báo đã xác nhận với BTC và chỉ thị tiếp tục làm. Tiến hành các kiểm tra/tích hợp được yêu cầu theo xác nhận đó; không yêu cầu lại cùng quyền. Đây là thông tin người dùng, không giả là đã đọc văn bản thay đổi quy định toàn cầu. Giữ timestamps/lịch sử đúng thực tế.

## 1. Trong thư mục NeuraX trên máy có gì?

Đã kiểm đúng thư mục `C:/Users/ghcoo/Everything/Code/Windows/Organizations/NeuraX`, không quét toàn máy hoặc Windows Registry.

| Repo / thư mục | Thực tế đã kiểm | Quyết định sử dụng |
| --- | --- | --- |
| `neurax-docs` | Markdown nghiên cứu, cached public data/QA, roles, PDF và ZIP bàn giao. Không phải API/dashboard sản phẩm | Nguồn quyết định/scientific evidence, không copy toàn bộ thành app |
| `neurax-fieldshift-lab` | Local ban đầu 77b7197 cũ hơn remote main. Đã fast-forward ddc6512 có AI-first/native review, deterministic tools, report API và 15 tests | Checkout toolkit chính. Cập nhật context/roles và sửa test Windows; tái dùng bộ đọc dữ liệu/QA/normalizer/API thay vì viết lại |
| `neurax-readiness-kit` | Cùng origin `NeuraX-Lab/neurax-fieldshift-lab`, cùng commit 77b7197 trước cập nhật; 86 file giống lab cũ khi bỏ khác CRLF | Bản sao cũ, không phải hệ thống riêng. Giữ nguyên, không chạy hai bản hoặc tự xóa/move |

Không thấy `.sln`, `.csproj` hoặc stack .NET/C# trong ba checkout. Nếu “Microsoft/registry/.NET” là một repo khác ngoài phạm vi này thì chưa có bằng chứng; không tự đoán một framework đang chạy.

## 2. Các repo GitHub khác đã kiểm đọc

- [`nasasac26-neurax`](https://github.com/NeuraX-Lab/nasasac26-neurax): repo sản phẩm public, chưa có checkout tại thư mục trên. Đã đọc cây file **main 3ca3000** và **dev e05a30b**: đều mới có README/docs/contribution scaffolding; chưa có frontend/backend executable. Không gọi kế hoạch folder frontend/backend/ai là code đã triển khai. README main vẫn ghi chưa chọn challenge, nên đó là trạng thái cũ cần đồng bộ khi bắt đầu app.
- [`.github/profile`](https://github.com/NeuraX-Lab/.github/blob/main/profile/README.md): trang giới thiệu tổ chức GitHub, không phải Microsoft/.NET. Đang còn shortlist cũ và thiếu Quang Luật; là phần giới thiệu cần sửa sau, không chặn intake/core. Không sửa org profile hoặc repo sản phẩm trong lượt này để tránh mở thêm đường phát triển.
- Connector chỉ báo read cho một số repo, nhưng GitHub CLI account local có ADMIN. Dùng Git CLI cho commit/push local, không đổi quyền/visibility. `neurax-docs` vẫn public theo lựa chọn trước của người dùng; lab private giữ nguyên.

## 3. Đã có dữ liệu chưa?

**Đã có snapshot công khai để kiểm pipeline:** POWER 2015-2025, SoilGrids và imagery có provenance trong docs. **Chưa có gói Resources/data bổ sung mà người dùng đang chờ ngày 13/11**; chưa đọc/ingest gói tương lai đó. Không thể nói hiện “không có dữ liệu gì”, cũng không nói dataset cuộc thi đã đầy đủ.

Thực thi mới trên lab:

| Kiểm tra | Kết quả thật | Chưa chứng minh |
| --- | --- | --- |
| Native Windows Python project `.venv` | Python 3.12.14, dependencies riêng; snapshot phiên bản trong lab | Chưa là môi trường training GPU, không dùng WSL env chung |
| Unit/integration tests | 15 passed sau sửa test SQLite đóng handle đúng trên Windows | Không phải accuracy model hoặc rule nông học đã kiểm |
| POWER cached -> monthly D1 | 4.018 ngày -> 132 tháng; SHA input khớp; tổng mưa từng tháng khớp tính độc lập | Chưa forecast, cân bằng nước hoặc ranking cây |
| QA và provenance | Giữ raw/WARN 488,17 mm ngày 14/06/2020 trong source_metadata/manifest; qa_status=pass chỉ completeness | Không biến WARN thành dữ liệu đã được domain QA phê duyệt |
| API | FastAPI TestClient trong tiến trình: status/fit/inventory 200; forecast không model 404 | Không phải server chạy nền, browser dashboard hoặc public deployment |
| AI/native workflow mô phỏng | Scripted fake model, partial, crop ranking và training bị chặn khi thiếu evidence/K1 | Không gọi LLM thứ hai, không train NASA model hoặc chứng minh AI nghiên cứu tự chủ |

Lỗi sửa: test dùng SQLite transaction context nhưng không đóng connection, Windows cleanup lỗi; scanner thực tế đã đóng connection. Sửa test bằng `contextlib.closing`, bỏ build `*.egg-info` khỏi Git. CI mở thêm Windows/Ubuntu. Còn một Starlette/httpx TestClient deprecation warning, tests pass; không đổi thư viện chỉ để giấu warning.

## 4. Kết hợp toolkit vào dự án thế nào?

Một luồng, không ghép ba repo thành một app khổng lồ:

**docs (quyết định/nguồn/K1) -> fieldshift-lab (intake/QA/D1 và review có gate) -> output/versioned contract -> backend Hiếu + core/UI Hưng-Việt trong repo sản phẩm khi triển khai.** An giữ H1 lab riêng, Luật kiểm từng block. Không copy duplicate readiness-kit, không ép forecast thành bài toán chính, không lấy fake-model simulation làm ranking luân canh.

Lab hiện **chưa tiêu thụ independent Q1/K1 approval để mở crop-ranking** và chưa có crop-ranking implementation. Finalizer chủ động hạ GO. Bước tiếp theo phải chốt rule/approval flow và schema từ bằng chứng Bích review, không bypass gate hoặc mặc định thêm một neural model. Dashboard và ESP thật vẫn là việc triển khai/kiểm riêng, chưa được tạo bởi tool intake.

## 5. Việc làm ngay, không đợi gói mới

1. **Hưng-Việt:** dùng fieldshift-lab chính, giữ môi trường/run reproducible; thống nhất lát cắt Data -> feature -> comparison -> output. Dùng kết quả POWER check làm chứng minh đường kỹ thuật, chưa là crop decision.
2. **Bích:** review [bảng 12 hàng](cases/my-thanh-cai-lay/rotation-evidence-review.csv), đúng cây/nguồn/vùng/năm; ưu tiên nước/thoát nước, lịch giống/chuyển vụ và rule NASA-feature-to-comparison có thể dùng. Ô reviewer/decision còn trống, không ghi đã được Bích phê duyệt.
3. **Luật:** nắm output thật ở mỗi block, kiểm đơn vị/coverage/flags và hỏi owner về blocker. Không lấy 132 tháng đầy đủ làm đồng nghĩa suitability pass.
4. **Hiếu:** chốt slot remote và backend handoff; Hưng-Việt hỗ trợ UI/UX và backend khi Hiếu offline.
5. **An:** kiểm model board/probe, interface, log/backup; không chờ chip để làm phần core khác.

Khi gói mới thực sự đến: giữ raw/hash -> inventory định dạng/schema/metadata/license -> chọn phần liên quan -> review nguồn/coverage/đơn vị/support -> ánh xạ D1/K1 -> Luật QA -> mới quyết định có cần thêm phương pháp/model. Không giả gói đó là dataset train sạch sẵn hoặc mở auto-train mặc định.

## 6. Gửi Bích cái gì và đã nghiên cứu tới đâu?

Đã nghiên cứu cấu trúc ba chuỗi từ hai bài CTU và tách SoilGrids model/ảnh/khí tượng khỏi dữ liệu ruộng; có bảng nguồn, trang/method và unknown trong PDF 1.3. **Chưa nghiên cứu được gói data ngày mai, chưa xác minh đất/nước tại ruộng và chưa có quyết định review của Bích.** Gửi hồ sơ để Bích review/đào sâu, không giao nhiệm vụ làm lại từ đầu hoặc tìm tỉnh mới.

- [ZIP hiện hành](../../output/handoff/NeuraX-MyThanh-Bich-Research-Pack-2026-11-12.zip): PDF 1.3 + CSV 12 hàng + bản đồ + GIS/tọa độ. Người nhận tải về và giải nén, đọc PDF trước, mở CSV UTF-8 trong Excel rồi điền cột review có nguồn.
- Hoặc gửi [PDF](../../output/pdf/NeuraX-AgroTwin-Site-and-Demo-Dossier-Bich.pdf) cùng [CSV](cases/my-thanh-cai-lay/rotation-evidence-review.csv), thay vì gửi riêng hình polygon.
- [Lời nhắn/email có thể copy](bich-review-message.md). Chưa có địa chỉ email/người nhận xác định và chưa thực hiện gửi email hoặc nhắn thay người dùng.

## 7. Lệnh kiểm đã dùng

Từ lab, native Windows project-local Python:

```powershell
$env:OMP_NUM_THREADS='1'
$env:OPENBLAS_NUM_THREADS='1'
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe scripts/simulate_ai_workflow.py
.venv/Scripts/python.exe scripts/check_cached_power.py --docs ../neurax-docs --out runs/cached-power-check-2026-11-12
```

Raw/derived run files và venv của lab giữ ignored. Chỉ commit tooling/docs/tests/dependency snapshot; không đẩy run artifacts hoặc secrets. Không có server nào được để chạy nền sau kiểm này.
