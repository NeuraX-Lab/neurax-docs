# Ngôn ngữ, nguồn và tài liệu nội bộ

> 2026-11-06 · Người dùng xác nhận neurax-docs là repo nội bộ. Đây là quy ước nội dung; chưa thay đổi visibility trên GitHub.

- Kế hoạch, phân công và quyết định hiện hành viết tiếng Việt, dùng tên thành viên thống nhất với team-profile.
- Giữ tên challenge/dataset, DOI/URL, đơn vị, schema và field code đúng nguồn. DATA, AI, DEPLOY, QA, baseline, forecast và scenario có thể giữ nguyên; giải thích khi cần cho người đọc.
- Giữ nguyên văn đề và snapshot nghiên cứu cũ. Thêm ghi chú superseded thay vì dịch/sửa ngược lịch sử.
- Bản nộp, pitch và demo hướng tới giám khảo quốc tế cần bản tiếng Anh rõ ràng. Đây là lựa chọn chuẩn bị nội bộ; quy định ngôn ngữ, thời lượng và hình thức nộp năm 2026 phải xác nhận riêng. Không mặc định luật 2025 là luật 2026.
- Nội dung nội bộ có thể chứa phân công, giới hạn và giả thuyết làm việc. Tách phần xuất ra ngoài khi cần; không tự đăng repo hay thay quyền truy cập.

## Thứ tự nguồn hiện hành

1. Quyết định người dùng/team được ghi ngày trong decision-log và final-selection.
2. Brief nguyên văn và Resources có provenance, năm và ngày truy cập.
3. Workflow/kiến trúc/phân công đề xuất; chưa là artifact đã chạy.
4. Ranking cũ, ghi nhận đối thủ và winner chưa có nguồn là lịch sử hoặc giả thuyết.

Mỗi claim kỹ thuật gắn với nguồn hoặc artifact/metric có version. Phân biệt analysis, forecast và scenario. Không chuyển 'may/could' thành yêu cầu bắt buộc, không gọi synthetic là quan sát NASA.

## Runtime và bàn giao

Repo này chỉ chứa Markdown/Mermaid; chưa chọn stack sản phẩm. Lượt cài skill ngày 06/11 chạy helper trên Windows bằng Python 3.12 tại `C:/Users/ghcoo/AppData/Local/Programs/Python/Python312/python.exe`; không cài scientific runtime vào repo. Khi bắt đầu code, đọc dependencies của repo sản phẩm và hei-dev-workflow; ưu tiên WSL cho xử lý EO/AI và ghi môi trường/lock/run commands tại đó. Không chia sẻ env giữa Windows và Linux.
