# Bàn giao FieldShift v2 — 15/11/2026

## Nguồn và nhánh dự kiến chia sẻ

| Repository | Branch bàn giao | Nội dung |
| --- | --- | --- |
| [neurax-docs](https://github.com/NeuraX-Lab/neurax-docs) | `docs/data-ai-readiness` | Resources, requirements, workflow, báo cáo v1 và chỉ mục v2 này |
| [neurax-fieldshift-lab](https://github.com/NeuraX-Lab/neurax-fieldshift-lab) | `ai/fieldshift-v2` | DATA/EDA, baseline v1, thực nghiệm v2, API/rules/retrieval, frontend nghiên cứu, báo cáo/metrics/screenshots; commit code v2 `173bbb8`, bàn giao `32cb1bf`, fix UI-origin `c6fad2b` |
| [nasasac26-neurax](https://github.com/NeuraX-Lab/nasasac26-neurax) | `dashboard/fieldshift-v2` | UI demo nối Lab API, commit `027f205`; source UI `handoff/v5-viet` tại `728249b` |

Folder local `references/nasasac26-ui-v5` tương ứng repository **nasasac26-neurax**, không phải repo GitHub có tên nasasac26-ui-v5. Không lấy model/backend/DATA của product làm baseline AI. Không merge hoặc đổi main. Tại lúc soạn chỉ mục, các branch bàn giao chưa được push; trạng thái truy cập cần đối chiếu sau push.

## Đọc ở đâu?

- [Hướng dẫn v2 và cache cần thiết](https://github.com/NeuraX-Lab/neurax-fieldshift-lab/blob/ai/fieldshift-v2/reports/v2/README.md).
- [DATA report](https://github.com/NeuraX-Lab/neurax-fieldshift-lab/blob/ai/fieldshift-v2/reports/v2/DATA_REPORT.md).
- [AI architecture/evaluation](https://github.com/NeuraX-Lab/neurax-fieldshift-lab/blob/ai/fieldshift-v2/reports/v2/AI_ARCHITECTURE_REPORT.md).
- [Dashboard visual report](https://github.com/NeuraX-Lab/neurax-fieldshift-lab/blob/ai/fieldshift-v2/reports/v2/DASHBOARD_VISUAL_REPORT.md).
- [Chạy demo trong repository UI](https://github.com/NeuraX-Lab/nasasac26-neurax/blob/dashboard/fieldshift-v2/docs/fieldshift-v2/README.md).

Demo local: `http://127.0.0.1:5179/fieldshift-v2`, proxy tới Lab API8183. Link localhost chỉ dùng trên máy đang chạy server, không phải một bản deploy public.

## Giới hạn bàn giao

Git chứa code, config, notebooks, báo cáo và các evidence/ảnh được chọn. Raw datasets, processed data caches, PDF nguồn chưa rõ quyền tái phân phối, model weights, môi trường Python/node_modules và secrets không được tự đưa lên. Clone Git chưa đủ để chạy inference nếu chưa có cache/model v2 thật. Hướng dẫn Lab nêu rõ dependencies và prerequisites; không tạo data giả thay cache.

V2 có cải thiện điểm test lịch sử ở mưa3 tháng/nhiệt1 tháng, nhưng CI còn chứa0, RH kém baseline và interval thiếu độ phủ. RAG được đánh giá bằng bộ câu hỏi tự soạn, chưa có expert sign-off. Phương án cây có điều kiện; chưa chứng nhận năng suất/lợi nhuận/cây tối ưu tại ruộng Mỹ Thành.
