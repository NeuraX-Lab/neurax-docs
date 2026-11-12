> Bổ sung sửa AOI 12/11: `build_my_thanh_commune_aoi.py` dựng AOI chính từ geometry nguồn NXB (cached), kiểm so với bản sao tham khảo, xuất GeoJSON/KML/CSV/manifest và ảnh ranh xã. `build_my_thanh_aoi.py` chỉ còn dựng mẫu thủ công 17 ha `illustrative-*`; không là ranh ruộng. `prepare_my_thanh_sources.py` audit dữ liệu query điểm, không tổng hợp toàn xã. Cùng Python Windows 3.12.14/Pillow 13.0.0; không thêm dependency.

# Nghiên cứu dữ liệu công khai cho tài liệu

Bàn giao Bích: `build_my_thanh_study_block.py` số hóa khối canh tác MT-BLOCK-01 theo pixel cạnh đọc được trên ảnh nguồn có extent; xuất ranh/CSV/ảnh/manifest. Kiểm nằm trong xã nguồn bằng các đỉnh và mẫu cạnh. Sample 15 coverage cached tại tâm block mới; không gọi đó là mẫu đất hay xác nhận đồng nhất. Native Windows/Python 3.12/Pillow, không mạng hoặc dependency mới. Xem hồ sơ `bich-site-and-demo-dossier.md` trong case Mỹ Thành.

Bổ sung sau so sánh địa bàn: `audit_long_khanh_power.py` đọc cached POWER Long Khánh–Cai Lậy, kiểm 4.018 ngày/16.072 giá trị rồi xuất daily.csv/manifest; không mạng hoặc dependency mới. [Khuyến nghị case và giới hạn nghiên cứu lịch sử](../../nasa-space-apps-2026/planning/cases/site-choice-2026-11-12.md). Không chuyển dữ liệu đất công bố thành mẫu mới tại điểm NASA.

Lượt khoanh tiểu vùng 12/11: `query_duc_lap_soilgrids.py` tải 18 subset WCS nhỏ và mặc định replay cache/hash, dùng Pillow 13.0.0 đã có ngoài standard library; `screen_duc_lap_rotation_windows.py` kiểm 44 cửa sổ giả định từ raw NASA, standard library, không mạng. Chạy bằng cùng Windows Python 3.12.14. Chưa có ruộng/đất/nước được xác minh; kết quả trong [hồ sơ địa phương](../../nasa-space-apps-2026/planning/cases/duc-lap/local-feasibility-study.md), không cập nhật proposal/PDF. Không cài dependency mới. `--refresh` chỉ áp dụng script SoilGrids khi muốn thay snapshot.

Bổ sung: `crosscheck_duc_lap_rain.py` tải/cached ERA5 event qua Open-Meteo, lưu raw và comparison; `duc_lap_reference_exposure.py` chỉ đọc raw NASA để tính cửa sổ giả định, không gọi mạng. Cả hai là audit phục vụ docs, không là validation nông học hay pipeline sản phẩm. Dùng cùng interpreter standard library; cách chạy tương tự script đầu.

Đây là audit nhỏ phục vụ docs theo yêu cầu người dùng, không là pipeline/as-built của repo sản phẩm. Giữ native Windows hiện có cho download/CSV/JSON bằng standard library; chưa cần WSL/conda/GIS packages. Các nghiên cứu/model Linux lớn sau này theo dependency và runtime của repo sản phẩm.

`audit_duc_lap_power.py` lấy NASA POWER tại điểm địa danh có nhãn, lưu raw/retrieval/manifest/QA và tổng hợp CSV. Mặc định đọc lại raw để tránh gọi lại cùng grid; chỉ `--refresh` khi thực sự muốn thay snapshot. Gói ở `nasa-space-apps-2026/sources/data-audits/duc-lap-2026-11-12/`.

```powershell
& $taskPython scripts/research/audit_duc_lap_power.py
```

Lượt này dùng Python 3.12.14 bundled Codex tại Windows, chỉ import standard library; không có requirements cần cài. `$taskPython` phải trỏ interpreter đã kiểm theo môi trường thực, không mặc định conda base. Script hash và raw SHA-256 trong manifest, query đủ để tái lập request nhưng source API có thể revision.

QA WARN là kết quả hợp lệ của audit: một ngày mưa lớn cần cross-check, không tự sửa/xóa. Assertion lỗi completeness/unit/physical thì xem qa.json trước khi dùng aggregation. Không gọi bản tổng hợp này là mô hình nông học, kiểm định vệ tinh hay baseline dự báo đã thắng.

Kiểm đã làm: duplicate JSON keys; expected daily keys/leap days; fill/nonfinite; units/time; temperature order; precipitation sign; sum tháng so ngày; chạy lại từ raw và so hash output. Không tăng grid resolution hoặc gán precision điểm thành precision ruộng.
