# Ghi chú trình bày nhanh: vì sao nhiều version và chốt v4?

## Bản nói khoảng60–90 giây

“Chúng tôi không giả định model phức tạp sẽ tốt hơn. V2 xây được pipeline NASA + LOCAL và baseline có nguồn. V3 siết validation, thử dự báo anomaly theo mùa và recency nhưng candidate chưa vượt đủ gate, nên giữ climatology. V4 giữ ML đó, cải thiện khâu hỏi đáp bằng kiểm độ đủ bằng chứng và checksum nguồn. Khả năng từ chối khi thiếu bằng chứng tăng từ1/8 lên6/8 câu cuối, giữ8/8 câu có bằng chứng. V5 thử uncertainty theo mùa nhưng chưa ổn định. V6 thử adaptive conformal với delayed labels, có lợi thế development nhưng không giữ khi xác nhận. Vì vậy chúng tôi chốt v4 cho demo theo quyết định người dùng, giữ kết quả âm tính và không đồng nhất version mới nhất với tốt nhất.”

| Bản | Câu hỏi nghiên cứu / thay đổi | Kết luận |
|---|---|---|
| Baseline | Seasonal-naive vs HGB, một holdout | Selection dùng cùng holdout, chưa độc lập |
| v1 /2e810c7 | HGB A8/B10 mưa và local LLM evidence selector | HGB test2025 MAE65,21/63,15 vs naive49,00; LLM không vượt extractive baseline |
| v2 /173bbb8+c6fad2b | Ba target, hai horizon, dữ liệu dài, RAG/rules/API/UI | Sáu kết quả lịch sử tái lập; còn undercoverage và unsupported answers |
| v3 /c6cd2fb | Causal refit, seasonal anomaly Ridge, recency, gate ổn định | Không candidate đủ gate; chọn mean climatology |
| v4 /ac93912, refined attempt | Query support + source-byte integrity; ML giữ v3 | RAG final abstention75% vs v2 12,5%; chọn hệ thống này |
| v5 /9214d35 | Seasonal/scaled residual uncertainty | Không qua score/coverage/width gate; không promote |
| v6 /d0e7269+d9fb7bd | ACI-inspired delayed-feedback calibration | RH outer tốt nhưng confirmation score kém4,49%/7,53%; rolling-no-alpha giải thích phần lớn lợi ích; không thay v4 |

Version là hồ sơ giả thuyết và thực nghiệm, không phải cấp độ thông minh tăng đều. V4 là system gồm ML lineage v3 + RAG lineage v4 + pooled; không phải lấy HGB v2 rồi đổi nhãn. Điểm khác biệt ablation xác nhận là gate bằng chứng/source integrity; chưa chứng minh adaptive alpha v6 tạo lợi ích tăng thêm.

Không nói “AI tối ưu tuyệt đối”, “test hoàn toàn độc lập”, “tiết kiệm X% nước”, “tăng năng suất”, “80% coverage guaranteed” hoặc “đã được chuyên gia nông học duyệt”. ML tổng hợp trên diagnostic cũ kém v2 khoảng4,85%; đó là giới hạn được công bố, không giấu để kể câu chuyện chọn version đẹp hơn.
