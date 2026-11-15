# DATA sử dụng và đối chứng đầu ra

**NASA:** POWER Daily API v2.10.3 tại retained coordinate lon106.021621/lat10.479098, label người dùng Mỹ Thành/Đồng Tháp chưa được đo survey/geocode độc lập.1984-01 đến2026-10,514 tháng. PRECTOTCORR mm/day -> monthly sum mm/month; T2M °C và RH2M% -> monthly mean; Tmin/Tmax giữ metadata. Daily UTC khác ranh giới ngày địa phương. SMAP L4 SFMC/RZMC là model context, không phải đầu dò ruộng.

**LOCAL:** tài liệu lịch vụ, tưới–tiêu, nghiên cứu luân canh, SoilGrids và station reference. Khác địa bàn/thời điểm không được join thành nhãn của ruộng. Soil quantiles không phải mẫu đo lặp. Câu hỏi/current crop, EC, pH ruộng còn unknown nếu người dùng chưa cung cấp. Không thêm labels nông học giả hoặc mục tiêu mô phỏng vào feature khí tượng.

Preprocessing: giữ raw; documented fill value thành missing, zero rain là measurement; tổng tháng chỉ khi đủ ngày calendar. Kiểm duplicate key, calendar liên tục, units, physical plausibility, one-to-one monthly joins. Không silently interpolate target. Fit scaler/seasonal feature centering trong train. Tương lai bị mutate không được thay feature/prediction tại origin trước đó.

Đối chứng DATA trước modeling: tính lại độc lập monthly từ raw NASA khớp; max float difference rain5,68e-14mm, temp3,55e-15°C, RH1,42e-14 điểm%. Không phát hiện lỗi preprocessing v2 nghiêm trọng đã xác minh. Manifest380 file, SHA256, schemas/units/source URL/version: Lab reports/v3/evidence/data-manifest.json. Dataset freeze không có nghĩa lịch release vintage đã được chứng minh.

**DATA đối chứng forecast cuối:** target là giá trị tháng POWER thật cùng mẫu/horizon ở2018–2025, không phải labels nông dân đo ruộng. So sánh predicted với actual trong runs/research-v3/<task>/final-diagnostic.csv; tính MAE/RMSE/bias/coverage theo năm/mùa và CI.96 tháng/task; split đã lộ nên không gọi độc lập. So model frozen v2 trên cùng giao thức thay vì lấy historical test2012–2014 trộn với2025 của v1.

**DATA đối chứng RAG cuối:**16 câu có expected evidence ID hoặc abstain do analyst biên soạn, tách development nhưng không expert gold; đối chiếu citation source hash/locator và literal answer. Không có ground truth năng suất, lợi nhuận, tiết kiệm nước, soil health hoặc crop suitability để kiểm chứng các claims đó.

**Đối chứng hệ thống:** deserialize model, chạy inference lại khớp saved output; test units/region/dates/NaN/bounds, missing/extreme forecast, malformed farm input, conflicts/drainage/salinity. Đây là technical QA, không thay Q1/K1 độc lập do reviewer chuyên môn ký.

Gói đã gửi GitHub: data/v2-hung-handoff commit02e3de3 gồm27 file/1,15MB; runtime v2 data/v2-runtime-handoff commitcc67471 gồm40 file/ZIP320KB. Chúng phục vụ **v2**, không được nạp thay selected v4 weights. Selected v4 cần sáu model v3 và ledger/registry v4 tương ứng. Raw giữ tại máy, không đổi tên model v2 thành v4.
