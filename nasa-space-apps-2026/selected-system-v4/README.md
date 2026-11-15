# FieldShift — selected system v4

Ngày15/11/2026. **Người dùng chốt v4 cho kết nối Dashboard.** Cấu hình: ML v3 frozen climatology + RAG v4 refined evidence gate + pooled residual intervals. Không tự nâng lên v5/v6 khi thấy artifacts mới. Đây là lựa chọn hệ thống nghiên cứu để demo, không phải tuyên bố ML thắng v2 hoặc khuyến nghị canh tác đã kiểm chứng.

| Cần đọc | Báo cáo |
|---|---|
| Kiến trúc giải thích cho người không chuyên | [01-AI-ARCHITECTURE.md](01-AI-ARCHITECTURE.md) |
| ML, training và kết quả validation thực | [02-ML-VALIDATION.md](02-ML-VALIDATION.md) |
| RAG, cẩm nang, citation và giới hạn | [03-RAG-EVIDENCE.md](03-RAG-EVIDENCE.md) |
| DATA đầu vào và DATA đối chứng đầu ra | [04-DATA-VALIDATION.md](04-DATA-VALIDATION.md) |
| Ghi chú trình bày các version | [05-VERSION-STORY.md](05-VERSION-STORY.md) |
| API và cách nối Dashboard | [06-DASHBOARD-API.md](06-DASHBOARD-API.md) |
| DATA → AI → DEMO và Git còn thiếu gì | [07-WORKFLOW-AUDIT.md](07-WORKFLOW-AUDIT.md) |

Code nguồn và artifacts trong repo `NeuraX-Lab/neurax-fieldshift-lab`, nhánh `ai/selected-v4-api`. Docs trong `NeuraX-Lab/neurax-docs`, nhánh `docs/selected-v4`. Không đồng nhất hai repo hoặc tên UI V5 với version AI. Dashboard mới của Hưng **chưa được cung cấp**, nên chưa tuyên bố end-to-end UI mới đã tích hợp.

Bằng chứng gốc: ML `reports/v3/evidence/selection-frozen.json`, `final-diagnostic.json`; RAG `reports/v4/evidence/refined/selection-frozen.json`, `final.json`; registry `runs/research-selected/artifact-manifest.json` và bản aggregate tracked `reports/research-final/evidence/artifact-manifest.json`. Runtime weights nằm ngoài Git thông thường. Các con số dưới đây được tổng hợp từ artifacts thực đã chạy, không train lại trong lượt tích hợp API.

Skill dùng: neurax-api-contract (Lab), neurax-docs-maintenance và neurax-architecture (Docs). Người dùng yêu cầu ghi kiến trúc đã triển khai tại neurax-docs, nên đây là as-built report, không ghi như proposal chưa thực hiện. Không có xác nhận mới của Bích/Quang Luật hoặc farmer trial.
