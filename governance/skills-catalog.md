# Skill cho NeuraX và Field Shift

> 2026-11-06 · Đã search, đọc entrypoint, cài bốn skill ngoài bằng skill-installer và tạo lại các workflow nội bộ bị thiếu. Skill tăng chất lượng bài thi, không đảm bảo giải thưởng.

## Bảy skill riêng — theo dõi trong repo

| Skill | Khi dùng | Đầu ra |
| --- | --- | --- |
| [neurax-challenge-research](../.agents/skills/neurax-challenge-research/SKILL.md) | Brief/Resources mới, NASA và nguồn nông học | So nguồn, data/K1 gates |
| [neurax-idea-lab](../.agents/skills/neurax-idea-lab/SKILL.md) | Chọn scope/điểm khác biệt | Trade-off, demo moment |
| [neurax-team-planning](../.agents/skills/neurax-team-planning/SKILL.md) | Chia việc/onboard/dependency | Owner, deliverable, acceptance |
| [neurax-architecture](../.agents/skills/neurax-architecture/SKILL.md) | Định nghĩa/đổi DATA–AI–DEPLOY | Contract, Mermaid, fallback |
| [neurax-system-optimization](../.agents/skills/neurax-system-optimization/SKILL.md) | Bottleneck/cắt scope | Bằng chứng, phần cắt, cách kiểm |
| [neurax-pitch-review](../.agents/skills/neurax-pitch-review/SKILL.md) | Demo/pitch/project page | Script, claim–evidence, phản biện |
| [neurax-docs-maintenance](../.agents/skills/neurax-docs-maintenance/SKILL.md) | Đổi nguồn/quyết định/vai trò | Docs/link/ngôn ngữ nhất quán |

Ví dụ: `$neurax-challenge-research kiểm Resources Field Shift và nguồn cây–đất–mùa`; `$neurax-pitch-review rà storyboard theo evidence hiện có`.

Theo [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills), skill chia sẻ theo repo nằm ở `.agents/skills/`. Mở neurax-docs làm workspace để khám phá theo repo; chat ở thư mục cha NeuraX có thể yêu cầu đọc đường dẫn SKILL.md cụ thể. Skill mới khả dụng từ lượt tiếp theo khi client khám phá chúng.

## Bốn skill ngoài — đã cài cho người dùng trên máy này

Vị trí `C:/Users/ghcoo/.codex/skills/{name}`. Không đồng nghĩa đã cài trên máy team hoặc runtime WSL. Không cài lại documents/pdf/presentations/visualize đã có qua plugin.

| Skill | Giá trị cho Field Shift | Nguồn pin | License |
| --- | --- | --- | --- |
| jupyter-notebook | Notebook thí nghiệm có cấu trúc, dễ chạy lại | [openai/skills](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook) | LICENSE.txt đi kèm |
| geomaster | CRS, grid, nodata và remote sensing | [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills/tree/a25cf9ec00e2745d03f8704acf6f6919694ccd9a/skills/geomaster) | MIT |
| statistical-analysis | Phương pháp, dependence, uncertainty và báo cáo thống kê | [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills/tree/a25cf9ec00e2745d03f8704acf6f6919694ccd9a/skills/statistical-analysis) | MIT |
| scientific-critical-thinking | Rà claim, confounding và evidence | [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills/tree/a25cf9ec00e2745d03f8704acf6f6919694ccd9a/skills/scientific-critical-thinking) | MIT |

Đã đọc SKILL.md, giữ upstream và license; bổ sung bản MIT gốc vào ba thư mục K-Dense. Chỉ cài skill/helper, chưa cài scientific runtime hay chạy pipeline. Dependency/version ví dụ phải đối chiếu project lock khi build. Script upstream chưa được chứng minh trên dữ liệu NeuraX.

scientific-critical-thinking có nhánh sơ đồ OpenRouter tùy chọn; chưa cấu hình/chạy nhánh đó. Không cài paid service. K-Dense yêu cầu attribution khi đóng góp đáng kể vào bản phát hành/báo cáo; kiểm metadata nguồn và ghi attribution khi thực sự dùng.

### Cài lại

Nhờ `$skill-installer` cài URL đã pin ở bảng, hoặc dùng helper `scripts/install-skill-from-github.py` của skill-installer với các tham số:

```text
--repo openai/skills --ref 49f948faa9258a0c61caceaf225e179651397431 --path skills/.curated/jupyter-notebook
--repo K-Dense-AI/scientific-agent-skills --ref a25cf9ec00e2745d03f8704acf6f6919694ccd9a --path skills/geomaster skills/statistical-analysis skills/scientific-critical-thinking
```

Installer dừng nếu đích tồn tại; không ghi đè chỉnh sửa local. Giữ thêm LICENSE.md gốc từ root K-Dense ở từng bản cài. Đây là cài skill, không cài scientific runtime.

### SHA-256 SKILL.md đã cài

| Skill | SHA-256 |
| --- | --- |
| jupyter-notebook | 62F102E8554B25716DCCEF0FFAB4572D4E3EAF05CCC76562D33A065BC9C521FB |
| geomaster | 7B3B88F13F0094285372DFCC25A000FB7E74E5FC4B67C1B6999543FFF3CADDE8 |
| statistical-analysis | E112848726B3713267CAC65E4E2C15491A0A26EE1ED628DB01195F7E43F97997 |
| scientific-critical-thinking | 563AF70571B7DCD6A96BF2E303BEDFDCBA623B4E9F082D58F04AACBC961FDAE4 |

## Cách chọn và giới hạn

Nguồn mới → challenge-research; idea → idea-lab; interface → architecture; phân công → team-planning; EO → geomaster; thống kê → statistical-analysis; rà claim → scientific-critical-thinking; notebook → jupyter-notebook; demo/pitch → pitch-review; cập nhật docs → docs-maintenance. Chỉ gọi optimization khi có bottleneck. Không nạp mọi skill cùng lúc.

Skill sản phẩm dùng ở nasasac26-neurax khi bắt đầu build và được giao; neurax-docs vẫn Markdown/Mermaid. Chưa cài cả bộ frontend/deploy vì stack chưa chốt. [Playbook](../nasa-space-apps-2026/planning/competition-playbook.md) ghi nguồn rubric và giới hạn kiểm năm 2026.

## Lịch sử và sửa sai

Catalog 30/10 ghi sáu skill tại `.agents/skills/`, nhưng checkout 06/11 không có thư mục này; PR #2 đã loại `.agents` khỏi Git. Lượt này tạo lại sáu workflow theo tài liệu hiện hành, thêm pitch-review và bỏ ignore. Không khẳng định khôi phục nguyên bản skill cũ.

Khảo sát hiện tại dùng catalog openai/skills và source K-Dense, chọn bốn tác vụ cụ thể. Không cài cả thư viện, bộ brainstorming bắt buộc nhiều vòng approval hoặc integration tài khoản chưa cần. Bộ skill NeuraX do team/trợ lý viết, không phải NASA chứng nhận.
