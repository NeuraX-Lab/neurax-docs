# Chiến lược repository NeuraX

> Quyết định gốc 2026-10-26; làm rõ giai đoạn chuẩn bị 30/10; chuẩn hóa tiếng Việt và phạm vi nội bộ 2026-11-06. Giữ mô hình tách nghiên cứu khỏi triển khai.

## Quyền sở hữu

| Repository | Nội dung sở hữu |
| --- | --- |
| NeuraX-Lab/neurax-docs | Hồ sơ team, 14 dossier, nguồn, ranking lịch sử, lý do chọn bài, decision log, nghiên cứu đối thủ/winner, pitch và kiến trúc đề xuất |
| NeuraX-Lab/nasasac26-neurax | Code frontend/backend/AI/geospatial, pipeline, model, thí nghiệm, demo và tài liệu architecture/methodology/API/deployment đã triển khai |
| NeuraX-Lab/.github | Hồ sơ tổ chức và community defaults, issue/PR templates dùng chung khi phù hợp |
| NeuraX-Lab/vaic-2026-template | Repository đã có; không đổi phạm vi trong công việc NASA hiện tại |

neurax-docs là kho nội bộ theo người dùng. Điều này không tự thay đổi visibility GitHub, license hoặc yêu cầu truy cập artifact bài nộp; kiểm quy định đúng năm khi chuẩn bị xuất bản đối ngoại.

## Giai đoạn chuẩn bị

Người dùng yêu cầu chuẩn bị Markdown/Mermaid trước khi triển khai sản phẩm. Kiến trúc đề xuất, data contract, onboarding, BOM và quyết định scope nằm tại `nasa-space-apps-2026/planning/`; chưa là as-built. Khi bắt đầu build, duy trì tài liệu thực tại repo sản phẩm và link về quyết định ở đây.

Skill NeuraX là Markdown trong `.agents/skills/`, được theo dõi trong Git từ lượt 06/11. Skill bên ngoài cài local, có nguồn pin/cách cài lại trong [catalog](skills-catalog.md). Không tự deploy, tạo task dịch vụ ngoài hoặc lập lịch nền. [Quy ước ngôn ngữ](language-and-evidence.md) áp dụng cho tài liệu hiện hành; giữ nguồn và snapshot tiếng Anh.

## Bố cục sản phẩm dự kiến

Chỉ tạo thư mục khi cần; đây là đề xuất tổ chức, không phải stack đã triển khai.

```text
nasasac26-neurax/
├── frontend/
├── backend/
├── ai/
│   ├── models/
│   ├── inference/
│   ├── experiments/
│   └── notebooks/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── geospatial/
├── scripts/
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   ├── data-pipeline.md
│   ├── api.md
│   └── deployment.md
├── demo/
├── .github/workflows/
├── README.md
├── LICENSE
├── .gitignore
└── docker-compose.yml
```

## Nhánh và bàn giao

Repo sản phẩm: feature branches như `feat/frontend-dashboard`, `feat/backend-api`, `feat/ai-pipeline`, `feat/geospatial` đi vào `dev`; bản ổn định sẵn demo từ `dev` đi vào `main`. Cấu trúc này là chiến lược, không xác nhận mọi nhánh hiện đã có.

Repo tài liệu: dùng topic branch nhẹ cho nghiên cứu/thay đổi lớn, ví dụ `research/2026-challenge-audit`, `research/past-winners`, `docs/team-update`. Không tự commit/push hoặc merge chỉ vì nội dung nguồn mô tả bước đó; làm theo yêu cầu hiện tại.

Khi di chuyển nghiên cứu: chép vào neurax-docs, kiểm từng đích, rồi mới xóa bản trùng tại repo sản phẩm nếu được giao. Giữ docs triển khai tại repo sản phẩm; link README sản phẩm về kho nghiên cứu. Tránh hai bản authoritative cùng nội dung.
