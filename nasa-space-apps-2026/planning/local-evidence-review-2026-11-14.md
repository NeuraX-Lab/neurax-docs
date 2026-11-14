# Bích bản có nguồn, local EDA và workflow ML/RAG

> 14/11/2026 chiều. Cập nhật nghiên cứu; chưa chọn features/kiến trúc cuối, train ML hay build RAG index.

Người dùng gửi `Data_fn.xlsx`, yêu cầu đọc nguồn, tự bổ sung dữ liệu địa phương và giải thích các dataset cùng workflow AI trong chat. Bản raw được sao vào Lab với tên `data/raw/bich-final-2026-11-14/bich-vietnam-agronomy-with-sources-2026-11-14.xlsx`; bản Downloads giữ nguyên, SHA-256 `844af355cd4068231815af6527a061eb5f8da389e46a0f52301ecca3369edb37`.

## Kết quả và giới hạn

- Workbook có 4 sheets, 11 URL nguồn, 9 cửa sổ vụ. Đã audit claim/source; homepage, nguyên tắc FAO hoặc văn bản vận hành thủy lợi không tự chứng minh mọi số trong bảng.
- Giữ tọa độ pack 10.4790980766,106.0216210397 và nhãn Mỹ Thành, Đồng Tháp theo xác nhận người dùng. Scope các nghiên cứu/tỉnh lịch sử kiểm riêng, chưa tự gán dữ liệu ở nơi khác thành đo tại block.
- SOC/N/CEC tải actual SoilGrids, 3 properties × 3 depths × mean/Q05/Q95 = 27 statistics tại một vị trí model. Có đơn vị/uncertainty, không phải 27 mẫu đất độc lập.
- NOAA GSOD Cần Thơ 2015–2025 có 3.794 temperature records/4.018 calendar days, 114 tháng nhiệt độ đủ ngày. Không có PRCP đủ strict full-day QA trong subset; flag I=0 không phải ngày khô quan trắc. Trạm cách AOI ~55km, không field ground truth.
- Đã tải/đọc CTU 2009/2017, VJST 2025 và nghiên cứu tiếng Anh 2024; trích bảng soil profile, provincial areas/ranges và 12 treatment means. Study Vĩnh Long dùng mè/đậu nành, không gán sang bắp non/đậu xanh. Các kết quả khác điều kiện không tự là nhãn best rotation.
- Corpus có bytes 11 tài liệu Anh/Việt (6 en/5 vi), 6 candidate rules chưa domain sign-off. Chưa embedding hoặc inference LLM.

## Đề xuất cần cùng chốt với người dùng

1. English cho hồ sơ/demo giám khảo, Vietnamese cho farmer explanation; corpus giữ nguyên ngôn ngữ nguồn và hỗ trợ retrieval song ngữ.
2. ML mưa monthly: seasonal-naive và một ứng viên HGB. Bộ A 8 biến (rain lags1/2/3/12, T/RH lag1, sin/cos tháng); bộ B thêm SMAP surface/rootzone lag1. Chọn bằng validation, không vì có thêm nguồn là mặc định tốt hơn.
3. MODIS/Sentinel trước mắt là map/context có QA và acquisition date, không crop classifier hoặc soil chemistry map.
4. So sánh luân canh dùng K1 + quản lý ruộng; unknown không tự thành pass. RAG giải thích numeric JSON và tài liệu có scope/citations, không tự sửa số hoặc tạo ngưỡng.
5. Workflow dự kiến build/QA → causal features → rolling tuning development → validation2024 → freeze → test2025 → visual/ablation → versioned inference. Trainer code cũ chỉ 5 features + single holdout; chưa là workflow mới đã chạy. Cần tách model selection khỏi final-test reporting trước benchmark mới.

Mốc 17h vẫn là mục tiêu người dùng từ trao đổi trước. Lượt hiện tại hoàn thành gói dữ liệu/EDA/thiết kế để chọn features, không khẳng định đã có baseline ML/RAG hoặc metrics. Thiếu rainfall observations, field drainage/irrigation, EC/current crop/cultivar calendar và K1 review được ghi rõ.

## Đọc trong Lab

Nhánh `research/bich-final-local-evidence-2026-11-14`:

- `docs/local-evidence-2026-11-14/README.md` — inputs, source audit, bổ sung thực tế và unknown.
- `dataset-guide.md` — POWER/MODIS/SMAP/Sentinel/SoilGrids/local/reference: units, visual và vai trò.
- `ml-rag-workflow.md` — method, features, input/output, metrics/splits, bilingual RAG và evaluation.
- `notebooks/resources/12-bich-final-source-review.ipynb`, `13-local-reference-eda.ipynb`.
- `runs/local-evidence-2026-11-14/` — source audit, các CSV chuẩn hóa có provenance, corpus register, rule candidates, seed summaries, figures và summary. Raw/runs local, chưa publish/upload.

Owner Việt; domain Bích; QA/E1 Quang Luật; scope/dashboard cùng Hưng. Không gửi tin cho thành viên trong lượt này.
