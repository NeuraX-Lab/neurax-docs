# Hai candidate: kiểm cửa sổ lịch và exposure lịch sử

Phục vụ [nghiên cứu địa phương](../../../../planning/cases/duc-lap/local-feasibility-study.md), không là crop model, dự báo mùa tới hoặc quyết định chọn cây. [windows.csv](windows.csv) lưu 44 cửa sổ, [summary.json](summary.json) lưu nguồn duration, giả định và hash raw/script.

Nguồn duration: GV10 95 ngày trong thử Đông Xuân 2011–2012 ở Đức Hòa Thượng ([TTKN Long An](https://khuyennongvn.gov.vn/hoat-dong-khuyen-nong/chuyen-giao-tbkt/long-an-mot-so-giong-lac-tren-vong-tren-vung-dat-xam-duc-hoa-6086.html)); CP888 102–110 ngày trong bảng khảo nghiệm ĐNB/ĐBSCL ([VAAS 7/2018, bảng 2, trang in 5](https://tapchi.vaas.vn/sites/tapchi.vaas.vn/files/tapchi/2021-08/tc1-2018_0.pdf)). Hai nguồn khác năm/vùng, chưa là giống đã chọn ở thửa; 110 không là trần thời gian trong mọi điều kiện.

Giả định: bắt đầu 1/1 hoặc 15/1 mỗi năm 2015–2025; dài 110 hoặc 95 ngày, inclusive; lúa vụ sau gieo 15/5; cần 14 ngày chuyển vụ. **Các ngày và 14 ngày đều do nghiên cứu đặt**, không từ nhật ký hộ. Ngày trống = khoảng cách tới 15/5 trừ ngày kết thúc cây trước và ngày gieo cây sau. Lúa chưa có giống/duration, nên không dùng kết quả để duyệt cả năm.

Kết quả số học: bắp 110 ngày từ 15/1 thiếu 3–4 ngày chuyển vụ; từ 1/1 dư 10–11 ngày. Đậu phộng 95 ngày dư 25–26 ngày từ 1/1, 11–12 ngày từ 15/1. Chênh một ngày do năm nhuận. Đây là độ nhạy lịch dưới giả định; không phải tỷ lệ thất bại mùa vụ hoặc cây nào tốt hơn.

Tổng mưa median các cửa sổ tương ứng 47,37 / 72,10 / 29,62 / 46,29 mm; cửa sổ khác độ dài không thể dùng để so nhu cầu tưới. Không có ET, Kc, root zone, đất/nước ruộng hoặc mô hình yield. Nguồn khí tượng là raw POWER tại điểm GeoNames đã audit; chưa kiểm chuyển vị trí sang tiểu vùng chọn. QA POWER vẫn WARN do event tháng 6/2020 ngoài các cửa sổ này, raw không sửa.

Chạy lại từ root repo bằng Windows Python 3.12.14, standard library, **không gọi mạng**:

```powershell
& $taskPython scripts/research/screen_duc_lap_rotation_windows.py
```

Credit: NASA POWER, nguồn/URL/version và raw hash ở [manifest cha](../manifest.json). Source IDs D7/D8 đối chiếu ledger của hồ sơ địa phương, không là mã contract sản phẩm.
