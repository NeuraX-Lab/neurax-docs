# ArgoTwin — 7 slide thuyết trình

**Phân công:** Ngọc Bích slide 1–3; Việt slide 4–5; Hưng slide 6–7. Video 30 giây phát riêng. Deck tĩnh, không tab hoặc phần ẩn; PDF có đúng 7 trang 16:9.

## Sửa phần của mình

File nguồn chung: [slides/index.html](slides/index.html). Mỗi slide là một `<section>` có ID cố định:

| Người nói | Phần cần sửa | Nội dung |
|---|---|---|
| Ngọc Bích | `slide-1`, `slide-2`, `slide-3` | Giới thiệu, problem, solution |
| Việt | `slide-4`, `slide-5` | DATA, model, kiến trúc và worked demo |
| Hưng | `slide-6`, `slide-7` | Validation, impact, next steps |

Chỉ sửa section của mình để giảm xung đột. Style chung ở [slides/static.css](slides/static.css); phối hợp trước khi đổi style vì nó có thể ảnh hưởng các trang khác. Assets là logo, research illustration và sơ đồ kiến trúc; không có raw data hoặc source PDF nông học trong thư mục này.

Mở `slides/index.html` để xem ngay. Sau khi sửa, chạy từ thư mục này:

```powershell
python build.py
```

Lệnh chỉ nhúng CSS/ảnh vào `ArgoTwin-Pitch.html`, không ghi đè nội dung nguồn của bất kỳ slide nào. Không cần cài thư viện Python.

Mở HTML đã build, Ctrl+P → Save as PDF, bật background graphics và tắt browser headers/footers. CSS đã đặt khổ 16:9 và ngắt đúng 7 trang. Kiểm print preview rồi lưu đè `ArgoTwin-Pitch.pdf` khi hoàn tất chỉnh sửa; build.py không tự tạo PDF.

## Kịch bản Việt

[Lời thoại Anh–Việt cho slide 4–5](06-VIET-SLIDES-4-5-EN-VI.md), mục tiêu khoảng 75 giây. Bích và Hưng tự chỉnh lời thoại phần mình theo phân công.

## Giữ các claim đúng

NASA POWER là dữ liệu lưới vùng; selected climate model là seasonal mean climatology. RAG dùng BM25 + character TF-IDF, kiểm hỗ trợ câu hỏi và source hash, trả extractive answer có citation hoặc từ chối. UI screenshot vẫn là placeholder chờ Hưng. Ba reference rotations không phải ranking đã kiểm chứng.

Bản được kiểm trước push: 7 slide hiển thị đầy đủ, không JS/control/hidden panel, không overflow ở screen/print; PDF đã render kiểm slide 3 sau khi bỏ các dòng phụ và căn giữa R0/R1/R2. Cần kiểm lại sau mỗi thay đổi nội dung.
