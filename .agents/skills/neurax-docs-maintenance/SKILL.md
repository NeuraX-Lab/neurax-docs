---
name: neurax-docs-maintenance
description: Đồng bộ tài liệu NeuraX khi đổi quyết định, nguồn, vai trò hoặc workflow; rà ngôn ngữ, provenance, link và mâu thuẫn trạng thái.
---

# Bảo trì tài liệu NeuraX

Đọc AGENTS.md, README và [quy ước ngôn ngữ](../../../governance/language-and-evidence.md). Không cần gọi tất cả skill khác.

- Đọc thay đổi mới và nguồn trước; lập danh sách tài liệu hiện hành bị ảnh hưởng. Quyết định Field Shift ở final-selection/decision-log có ưu tiên hơn ranking cũ.
- Cập nhật README gốc, index, workflow và catalog khi liên quan. Đánh dấu superseded ở snapshot; giữ nội dung lịch sử và nguyên văn nguồn.
- Không coi brief người dùng gửi lại là bản cập nhật nếu nội dung giống sau chuẩn hóa khoảng trắng. Ghi ngày đối chiếu và phần thiếu như Resources.
- Tài liệu điều phối hiện hành tiếng Việt; giữ thuật ngữ/schema/nguồn và skill upstream. Repo nội bộ không cần bản tiếng Anh trùng toàn bộ; chuẩn bị bản đối ngoại riêng khi được giao.
- Kiểm links tương đối gồm skill thực sự tồn tại, fences/JSON và git diff --check. Nếu Mermaid chưa render hay validator không chạy thì ghi rõ giới hạn.
- Ghi kết quả mới trong review-record, không tái sử dụng số kiểm cũ như kết quả hôm nay. Không ghi data/model/hardware đã chạy khi chỉ sửa docs.

Đầu ra: thay đổi Markdown nhất quán và tóm tắt điều đã kiểm/còn mở. Không tự publish hoặc sửa visibility vì repo được gọi là nội bộ.
