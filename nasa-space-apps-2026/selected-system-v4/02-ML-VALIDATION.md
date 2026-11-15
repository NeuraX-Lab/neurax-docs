# ML, training và validation đã thực hiện

Selected v4 dùng **mean climatology** từ v3 cho precipitation, air temperature và relative humidity, mỗi target có horizon1/3. Fit là ước lượng thống kê train và lưu model.joblib. Không có neural training hoặc weight fine-tuning ở bản được chọn. Các phương án đã thử gồm recent10/20-year climatology, seasonal-anomaly Ridge alpha20/200/2000, frozen v2 specs và fixed v1-style HGB reference. Reference v1-style không được gọi là exact v1; tái lập lịch sử v1 được lưu riêng.

Search gồm60 tổ hợp method/task, 1.320 build/fit calls gồm cả baseline/composite statistics, khoảng61 giây lượt đầu trên CPU một luồng. Full replay60 cấu hình khớp predictions đến1e-12. Máy đo khoảng15,7GB RAM, MX5702GB; không dùng GPU/cloud hoặc trả phí. Python3.12.7, sklearn1.5.1, numpy1.26.4, pandas2.2.2. Các seed stochastic comparator đã pin; climatology/Ridge deterministic không cần giả vờ nhiều seed tạo thêm độc lập.

**Walk-forward / rolling-origin:** refit theo quý với train mở rộng; cập nhật feature theo tháng. Development2004/2006/2008/2010/2011; fit seasonal centering/scaling trong train. Gate chọn candidate: MAE giảm>=3%, thắng>=3/5 năm, không mùa nào kém>10%, lower paired year-block CI95>0. Các candidate chưa vượt đủ gate nên giữ baseline. CI mang tính mô tả, nhỏ mẫu và selection optimism vẫn tồn tại.

**Calibration** riêng2015–2017,36 tháng. **Final diagnostic**2018–2025,96 tháng/task, chỉ mở sau commit9214d35 đã chốt v3–v5. Nhãn đã lộ trong dự án trước đó; không gọi đây là independent/blind test. Có một caveat: cuối calibration2017 chưa hoàn toàn khả dụng tại origin đầu2018 theo buffer; v6 có đối chứng timing đã sửa. Vì người dùng chốt v4, không âm thầm thay band thành v6; giới hạn timing phải được giữ trong tuyên bố khoa học.

| Target / h | V4 MAE | Frozen v2 cùng giao thức MAE | Coverage nominal80% |
|---|---:|---:|---:|
| Mưa h1, mm/tháng |62,7357|66,2414|67,71%|
| Mưa h3, mm/tháng |62,7357|62,1183|67,71%|
| Nhiệt h1, °C |0,5373|0,5435|85,42%|
| Nhiệt h3, °C |0,5373|0,5376|85,42%|
| RH h1, điểm % |3,6331|2,9983|82,29%|
| RH h3, điểm % |3,6331|3,2034|82,29%|

MAE càng thấp càng tốt. Tỷ số MAE ngang trọng số sáu task so với v2 là1,04851, tức kém4,85% trên diagnostic này. Không khẳng định ML v4 tốt nhất về mọi metric. Lựa chọn v4 là cấu hình thận trọng đã chốt development và có RAG cải thiện, hiện được người dùng chọn cho demo.

Seasonal failure: mưa mùa ướt MAE khoảng90,706mm vs mùa khô23,578mm ở h1; bias mưa toàn kỳ khoảng−49,640mm. Có distribution shift/outlier theo năm; không bỏ cực trị để làm đẹp điểm. Chưa có geographic generalization do một AOI, chưa có ground-truth mưa ruộng.

Output forecast hiện tại dùng dữ liệu đến2026-10, target h1=2026-12, h3=2027-02 do buffer; không phải dự báo ngày mai. Artifacts có sáu file runs/research-v3/<target>-h<h>/model.joblib và radius metadata. Registry giữ checksum weights và data. Báo cáo này ghi kết quả sau fit đã có; lượt API không train lại hoặc nhìn final để tune thêm.
