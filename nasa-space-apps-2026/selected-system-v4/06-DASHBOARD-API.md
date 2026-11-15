# API contract cho Dashboard của Hưng

Code Lab nhánh `ai/selected-v4-api`: `scripts/selected_v4_api.py`; config `config/selected-system.json` pin v4, auto_upgrade=false. TypeScript adapter `integration/dashboard-v4-client.ts`, OpenAPI và output thật `integration/openapi-v4.json`, `integration/v4-overview.example.json`. Chưa sửa Dashboard chưa nhận được.

```powershell
# Repo Lab, môi trường và selected v4 artifacts đã có:
.venv-geo-eda/Scripts/python.exe -m uvicorn scripts.selected_v4_api:app --host 127.0.0.1 --port 8184
```

| Method / endpoint | Dashboard dùng để làm gì |
|---|---|
| GET /api/v4/status | Ready/503, selected_system, run_id, data_through; evidence_sources ready/partial |
| GET /api/v4/overview | Sáu forecasts, lịch sử24 tháng, LOCAL context và decision cần thêm input |
| GET /api/v4/forecasts | Forecast có target/unit/horizon/origin/target_month/value/lower/upper |
| POST /api/v4/analyze | Farm input + question -> options, missing_inputs, warnings, RAG/citations |
| GET /api/v4/evidence |17 cards cùng source IDs/URL/hash/locator |
| GET /api/v4/metrics | Số validation ML/RAG đã pin, independent_test=false |

Response có `api_schema_version=fieldshift-dashboard-1`, `selected_system=v4`. Analysis giữ core shape forecasts/decision/rag của v2, thêm metadata selected; Dashboard phải dùng endpoint v4 thay vì tự đọc snapshot v2. Unknown fields và sai region/unit/date bị422; chưa cài artifacts hoặc hash không khớp ->503, không thay model bằng số giả. Forbidden Origin403, body lớn413. Kiểm RAG source partial qua status và hiển thị abstention nếu thiếu file.

```json
{"region_id":"MT-BLOCK-01","farm":{"current_crop":"rice","goal":"water","drainage":"poor","irrigation":"unknown"},"question":"Đậu xanh có cần thoát nước tốt không?"}
```

Input trên là ví dụ request, không phải quan trắc ruộng. Dashboard không tự xếp hạng hoặc điền score. Hiển thị đầy đủ warnings, missing_inputs, status blocked/needs_information/conditional_reference và citation. Không đổi `nominal_coverage=.8` thành accuracy80%. Kiểm tháng mục tiêu; không gắn forecast tháng vào widget “ngày mai”.

Client: `const api = fieldshiftV4(API_BASE_URL); await api.overview(); await api.analyze(farm, question);`. BaseURL lấy từ cấu hình frontend, không hardcode đường dẫn máy Việt. Adapter hỗ trợ AbortSignal và kiểm selected_system; errors có HTTP status/detail. Đây là client source chưa được build với toolchain Dashboard tương lai.

CORS mặc định cho localhost5173/5180/5179 và localhost3000. Origin mới khai báo env `FIELDSHIFT_DASHBOARD_ORIGINS` (comma-separated full origins), restart API. Không wildcard hoặc tự mở public. Chỉ bind127.0.0.1; nếu deploy public cần auth/TLS/proxy riêng, hiện chưa triển khai.

Khi Hưng gửi repo/branch: fetch, đọc hướng dẫn và status, tạo branch integration riêng, map widget tới contract trên, chạy build và browser desktop/mobile, thử loading/error503/422/abstention/sourcepartial, kiểm không tái xếp hạng. Chưa có source nên không thể chứng nhận bước UI cuối ngay bây giờ.
