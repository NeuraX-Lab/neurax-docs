---
name: neurax-system-optimization
description: Giảm scope hoặc xử lý bottleneck dữ liệu, mô hình, tích hợp và hardware của NeuraX theo bằng chứng và deadline hackathon.
---

# Tối ưu MVP và công suất

Đọc [timeline](../../../nasa-space-apps-2026/planning/event-timeline.md), workflow đang dùng và trạng thái artifact thực. Chỉ áp dụng khi có bottleneck hoặc yêu cầu cắt scope.

1. Xác định metric liên quan: thời gian có D1/A1, lỗi tích hợp, coverage, latency hoặc công suất owner. Phân biệt số đo, ước lượng và mục tiêu.
2. Tìm dependency đang chặn demo; so cách giảm volume/số nguồn, cache, batch, baseline đơn giản hoặc đổi cách chia việc trước khi thêm hạ tầng.
3. Giữ correctness: không bỏ QA/unit/source để làm chart đẹp, không gọi scenario là forecast. Đừng tối ưu model khi chưa có baseline/evaluation.
4. Theo T+2 data gate, T+6 D1/baseline, T+12 demo; dùng D=min(deadline local, global) khi đã xác nhận. Mốc nội bộ không phải agenda BTC.
5. Ưu tiên một vùng, 1–2 nguồn, ít cây; bỏ model nâng cao, nguồn/layer phụ, actuator và animation trước đường DATA → baseline → demo → evidence.

Đầu ra: bottleneck có bằng chứng, phương án chọn, phần cắt, owner, cách đo lại và rollback nếu đổi kỹ thuật. Giữ nghỉ và buffer; không tính sáu người nhân 48 giờ như công suất thực.
