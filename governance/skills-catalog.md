# Bộ skill nghiên cứu và điều phối NeuraX

> 2026-10-30 · Đã tạo repo-local tại `.agents/skills/`, chỉ gồm Markdown.
> Dùng khi làm việc trong thư mục neurax-docs. Không cài thêm plugin, service hoặc workflow chạy nền.

## Bộ skill đã setup

| Skill | Dùng khi | Đầu ra |
| --- | --- | --- |
| [neurax-challenge-research](../.agents/skills/neurax-challenge-research/SKILL.md) | Đọc đề/Resources mới | Dossier có nguồn, core/optional và data gates |
| [neurax-idea-lab](../.agents/skills/neurax-idea-lab/SKILL.md) | Brainstorm và chọn idea | Phương án, trade-off, score và điều kiện chọn |
| [neurax-team-planning](../.agents/skills/neurax-team-planning/SKILL.md) | Onboard, chia task cho sáu thành viên | Owner, dependency, deliverable, acceptance và Mermaid |
| [neurax-docs-maintenance](../.agents/skills/neurax-docs-maintenance/SKILL.md) | Cập nhật nghiên cứu hoặc thành viên | Docs/README/log đồng bộ, giữ lịch sử |
| [neurax-architecture](../.agents/skills/neurax-architecture/SKILL.md) | Chuẩn bị kiến trúc DATA–AI–DEPLOY | Sơ đồ, contract, baseline, fallback và ADR |
| [neurax-system-optimization](../.agents/skills/neurax-system-optimization/SKILL.md) | Tối ưu scope, tài nguyên hoặc bottleneck | So phương án theo bằng chứng, kế hoạch đo và scope cuts |

Đây là các skill **viết riêng cho NeuraX**, không phải bộ NASA hay OpenAI chứng nhận. Tự động ở đây là khả năng chọn workflow phù hợp theo mô tả skill khi có yêu cầu; không có cron, tự gửi tin nhắn hoặc tự giao việc trên dịch vụ bên ngoài.

Có thể gọi trực tiếp, ví dụ: `$neurax-idea-lab so sánh Field Shift với Earth Analog cho đội sáu người`; hoặc `Đọc .agents/skills/neurax-team-planning/SKILL.md và lập kế hoạch chuẩn bị`.

Theo [hướng dẫn OpenAI về repo-local skills](https://developers.openai.com/blog/skills-agents-sdk), `.agents/skills/` là vị trí dành cho workflow trong repo. Skill mới dùng từ lượt tiếp theo khi client khám phá thư mục repo; nếu chat đang ở thư mục cha, mở neurax-docs làm workspace hoặc yêu cầu đọc đường dẫn SKILL.md cụ thể. Không khẳng định đã cài vào mọi tài khoản/giao diện ChatGPT. Tham khảo [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Khảo sát đã làm trước khi chọn

| Nguồn | Kết quả | Quyết định |
| --- | --- | --- |
| [openai/skills curated catalog](https://github.com/openai/skills/tree/main/skills/.curated) | Đã đọc danh mục qua GitHub ngày 2026-10-30; có Notion planning/research, notebook, deploy và các workflow khác | Không cài các integration không cần cho Markdown repo |
| [obra/superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | Đã đọc để đánh giá; nhiều bước hội thoại/approval và phụ thuộc writing-plans | Không cài/bật bộ này; workflow docs của team được viết riêng gọn hơn |
| skill-creator và skill-installer đã có trong môi trường | Dùng hướng dẫn cấu trúc và đánh giá nguồn | Không cài lại system skills |
| OpenAI Docs | Đối chiếu cách đóng gói/discovery | Chọn repo-local, không sửa cấu hình toàn máy |

Không sao chép nội dung skill bên thứ ba vào bộ mới. Nếu nhập skill ngoài trong tương lai: đọc SKILL.md và dependencies, kiểm phạm vi/chất lượng, pin revision, ghi license, rồi chỉ cài phần thật sự dùng được.

## Chu kỳ cập nhật

Dữ kiện mới → research → idea/ranking → team/architecture → docs-maintenance. Chỉ gọi optimization khi có bottleneck hoặc cần cắt scope; không lặp mọi skill cho mọi chỉnh sửa.

Trạng thái decision không tự đổi từ “đề xuất” thành “team đã chốt”. Không gán chuyên môn/availability từ chức danh hoặc năm học; luôn liên kết về team-profile và chứng cứ hiện có.


## Lượt áp dụng tiếp theo — 2026-10-30

Đã dùng cả sáu workflow cho cập nhật Quang Luật và ba idea: nghiên cứu lịch 2025/2026; brainstorm/reassessment shortlist; chia task DATA QA; cập nhật tài liệu; contract-first architecture; tối ưu theo T0/deadline. Team-planning và idea-lab đã bỏ giả định Quang Luật chủ yếu làm gá/vỏ. Xem [workflow index](../nasa-space-apps-2026/planning/workflows/README.md).
