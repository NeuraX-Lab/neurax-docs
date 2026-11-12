---
name: neurax-architecture
description: Thiết kế kiến trúc đề xuất DATA–AI–DEPLOY và contract D1/Q1/K1/A1/E1/H1 cho MVP NeuraX; dùng khi đổi luồng dữ liệu hoặc tích hợp.
---

# Kiến trúc NeuraX

Đọc [architecture](../../../nasa-space-apps-2026/planning/architecture.md), workflow đang dùng và team-profile. Giữ code/as-built ở repo sản phẩm; ở đây viết proposal Markdown/Mermaid.

- Bắt đầu từ quyết định người dùng và grain dữ liệu; dùng batch nhỏ + schema ổn định trước API/streaming. UI đọc kết quả, không phụ thuộc notebook hay raster gốc.
- D1 có manifest/dictionary/provenance; Q1 theo feature/entity/period; K1 có nguồn domain; A1 có version/status/warning; E1 gắn đúng split/run; H1 có device/time/unit/quality và live/replay.
- Giữ nodata khác 0, CRS/unit/time/scale rõ. Không tăng độ chính xác bằng resampling. Fit preprocessing chỉ trên train khi đánh giá model.
- Phân biệt analysis/forecast/scenario và observed/synthetic/mixed. Partial/unavailable là trạng thái hợp lệ; UI không tự biến needs_review thành khuyến nghị.
- Thiết bị không chặn pipeline NASA; chọn offline snapshot/replay có nhãn khi cần. CSV/JSON cho R/MATLAB/Python, không buộc deploy MATLAB.
- Thêm trường tùy chọn theo version; đổi grain/unit/ý nghĩa cần cập nhật producer/consumer. Đổi dữ liệu/model tạo version mới, không dùng metric khác version.

Đầu ra: diagram, schema và acceptance cho một lát cắt end-to-end; giải thích trade-off và fallback. Không khóa stack/runtime khi dependencies repo sản phẩm chưa được kiểm.
