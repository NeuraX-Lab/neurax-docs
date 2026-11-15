# Audit DATA → AI → DEMO và Git

## Đã có bằng chứng

- DATA NASA/LOCAL freeze, checksum, independent reaggregation và causal feature tests; không thêm dataset.
- Selected v4 config khóa ML v3/RAG v4/pooled, model/input checksum, typed forecasts. Server mới không tự chọn v5/v6.
- API phục vụ overview/history/forecasts/analyze/evidence/metrics; OpenAPI và TS adapter cung cấp cho Hưng.
- Kiểm preflight CORS, foreign Origin, malformed inputs, thiếu artifacts và constraints. Full suite hiện82 passes, một Starlette/httpx deprecation warning. HTTP thực status/overview/analyze/preflight đều200 tại máy Việt, source17/17; ghi ở Lab integration/v4-http-validation.json. Không gọi đó là domain approval.
- V2 DATA/runtime đã push và kiểm checkout sạch; vẫn là v2. Không dùng chúng thay model selected v4.

## Còn thiếu / cần tinh chỉnh

| Gap | Tác động | Bước xử lý / acceptance |
|---|---|---|
| Dashboard Hưng chưa có source/branch mới | Chưa thể chạy browser end-to-end hoặc build adapter trong toolchain thật | Hưng cung cấp repo/ref; branch riêng; build + desktop/mobile + error states |
| Selected v4 models/ledger/cache cần có trên máy deploy | Clone source không tự có artifact ignored | Cài bộ selected v4 đúng paths/registry; status ready và6 forecasts |
| Source bytes cho17 cards chưa chắc có ở Hưng | RAG v4 từ chối card có nguồn thiếu/sai hash | Chuyển cache được phép hoặc lấy lại cùng nguồn đúng hash; status17/17; không bỏ gate |
| Cold bundle v2 trước không có ảnh/PDF lớn | Image/plot widgets có thể thiếu; không ảnh hưởng inference core | UI hide/placeholder đúng, hoặc gói assets cần thiết sau |
| Test cuối đã lộ và calibration timing caveat | Không đủ tuyên bố accuracy độc lập/operational | Công bố giới hạn; protocol prospective mới khi được cấp dữ liệu |
| Mưa undercoverage và RH kém v2 | Cần tránh thông điệp “model mới luôn tốt hơn” | Hiển thị nominal và measured coverage riêng; không tự đổi selected theo test |
| Chưa expert K1/Q1 sign-off | Không thể khuyến nghị áp dụng hay claims năng suất/nước | Bích/Quang Luật review; giữ domain_approved=false |
| Không có auth/TLS cho internet | Chỉ demo localhost | Có deployment riêng nếu được yêu cầu |

## Git ổn ở mức nào?

Lab remote `NeuraX-Lab/neurax-fieldshift-lab` khác Docs remote `NeuraX-Lab/neurax-docs`; product UI `NeuraX-Lab/nasasac26-neurax` là repo thứ ba. UI tên V5 không phải model AI v5. Branches version/research giữ riêng; selected branch không merge tự động main và không force-push.

Các ref đã có: data/v2-hung-handoff02e3de3; data/v2-runtime-handoffcc67471; research/ai-v6-delayed-conformald9fb7bd. Phần selected API ở ai/selected-v4-api, docs ở docs/selected-v4. Dùng fetch rồi checkout branch đúng; pin code/config/artifact manifest thay vì copy model trùng tên từ branch khác. Chỉ push hai nhánh task sau kiểm tra; chưa merge hoặc tạo approval thay reviewer.

Docs có thay đổi sẵn ở planning/team-workstreams.md được giữ nguyên, không đưa vào commit báo cáo này. Chưa chứng nhận product Dashboard branch của Hưng đã sync hoặc build, vì chưa được nhận source mới.

Chốt: DATA→AI→API có thể kiểm tại máy Việt; DATA→AI→Dashboard mới **còn bước frontend integration**. Không gọi sự thành công của TestClient/HTTP là browser acceptance hay field validation.
