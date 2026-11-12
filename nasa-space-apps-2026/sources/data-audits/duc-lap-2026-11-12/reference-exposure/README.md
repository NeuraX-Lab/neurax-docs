# Historical exposure cho một cửa sổ tham chiếu

[CSV 11 cửa sổ](exposure.csv) · [Kết quả và hash](summary.json) · [Script](../../../../../scripts/research/duc_lap_reference_exposure.py).

Thiết kế: bắt đầu 15/01 mỗi năm, 75 ngày inclusive; 2015–2025. Ngày là giả định, không lịch ruộng. Độ dài tham khảo cận trên IAS công bố cho candidate ĐH-1, cần review áp dụng. Các năm nhuận tự tính đúng ngày cuối; mỗi cửa sổ có đúng 75 keys từ raw POWER UTC.

| Tổng mưa cửa sổ qua 11 năm | mm |
| --- | ---: |
| Median | 12,0 |
| Mean | 27,42 |
| Minimum | 0,35 |
| Maximum | 112,84 |

T2M trung bình các cửa sổ là 29,295 C. Source grid và raw hash giữ như audit NASA; không có event tháng 6 trong các cửa sổ này, không phải đã sửa/lọc outlier. Overall NASA QA vẫn WARN. Không là climate normal 30 năm hoặc forecast mùa tới.

Phép tính làm cụ thể câu hỏi nước/lịch trong prototype, không chứng minh cây thiếu nước hay phù hợp. Không có ET/crop coefficient/soil storage/irrigation nên không tính water deficit, water savings hoặc yield. Không dùng exposure một cửa sổ để xếp hạng ba chuỗi. Diagnostic Tmax>=35 C trong CSV không là rule hại cây đã review.

Chạy bằng bundled Python native Windows đã xác minh; standard library, không gọi mạng:

```powershell
& $taskPython scripts/research/duc_lap_reference_exposure.py
```

Credit NASA POWER/MERRA2 theo manifest. Nguồn duration: https://iasvn.org/giong-me-dh-1 . Con số giả định và con số từ dữ liệu phải giữ nhãn tách biệt ở UI và pitch.
