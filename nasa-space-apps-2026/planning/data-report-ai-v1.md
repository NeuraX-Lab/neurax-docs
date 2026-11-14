# Báo cáo DATA — đầu vào thí nghiệm AI v1

Ngày 14/11/2026. Owner: Việt/Codex; numeric QA cần Quang Luật review, nghĩa nông học cần Bích review. Đây là báo cáo dữ liệu, tách khỏi [báo cáo AI](ai-report-v1.md).

## Trả lời câu hỏi NASA + LOCAL + FARM

**Có đủ ba thành phần cho thí nghiệm với FARM preferences mô phỏng. Chưa có số đo và lịch canh tác thực của riêng ruộng.** User đã làm rõ FARM INPUT là mong muốn của nông dân, ví dụ tối ưu nước/đất/sản lượng, và cho phép tự xây kịch bản. Không dùng mục tiêu mô phỏng làm nhãn năng suất, giá trị thời tiết hoặc xác nhận điều kiện tại ruộng.

Gói thực: `neurax-fieldshift-lab/data/processed/ai-input-v1/`. Trong đó:

```text
ai-input-v1/
  NASA-LOCAL/                 snapshot nguyên byte của DATA v1
    monthly/environment.csv
    features/core-a.csv
    features/extension-b.csv
    context/                 MODIS và Sentinel-2 theo ngày/QA
    local/                   đất, trạm, rules và reference
    farm-input/              khung đo/quản lý thực địa còn trống
  FARM/preferences.simulated.json
  manifest.json              data_mode=mixed và hashes
```

`config/farm-scenarios.json` trong Lab là nguồn tái tạo ba kịch bản. LOCAL gốc vẫn tập trung ở `data/raw/local/my-thanh-v1/`; các nguồn NASA gốc giữ nơi đã tải và được dẫn bằng manifest. Không có upload hoặc dữ liệu giả trộn vào chuỗi thời tiết.

## Từng nguồn đi đâu trong kiến trúc?

| Nguồn | Dữ liệu đã có | Vai trò thực |
| --- | --- | --- |
| POWER | 4.322 ngày, 01/2015–10/2026; 142 tháng | Lịch sử và target dự báo mưa; nhiệt độ/ẩm không khí làm lag |
| SMAP L4 qua POWER | 31/03/2015–31/12/2025, lớp mặt/vùng rễ | 2 features thử thêm trong ML và context ẩm–khô |
| MODIS MOD13Q1 | 69 composite 2023–2025, vùng 17×17 ô | Map NDVI/EVI, nhịp thảm thực vật theo mùa và QA |
| Sentinel-2 C1 | 8 cảnh 2025, ranh mẫu khoảng 2ha | RGB, NDVI/EVI, coverage trong ranh; chưa phân loại cây |
| SoilGrids/ISRIC | pH/texture từ pack, SOC/N/CEC point subset có độ sâu và phân vị | Context đất mô hình; chưa là mẫu đất đo |
| LOCAL | Mưa Mỹ Tho, nhiệt Cần Thơ, bản tin nước–mặn, nghiên cứu và quy trình canh tác | Reference/context và candidate rules; giữ đúng site/năm/method |
| FARM preferences | 3 kịch bản nước, đất, sản lượng | Mục tiêu, cây quan tâm, mức chấp nhận rủi ro và trọng số mong muốn |

Sentinel-2 thuộc ESA/Copernicus; HLS của NASA chưa tải. IMERG vẫn chưa có pixel mưa thực trong gói, nên không được tính là nguồn fusion/ML. SMAP L3 access audit khác với L4 đã tải. Độ phân giải và cách sinh dữ liệu khác nhau không bị đổi tên thành số đo tại ruộng.

## FARM preferences mô phỏng

| Kịch bản | Nước / đất / sản lượng | Ý nghĩa |
| --- | --- | --- |
| Ưu tiên nước | 0,60 / 0,25 / 0,15 | Muốn xem phương án có thể giảm áp lực nước, cần kiểm tưới–tiêu |
| Ưu tiên đất | 0,20 / 0,65 / 0,15 | Quan tâm đa dạng cây và bằng chứng về đất |
| Ưu tiên sản lượng | 0,15 / 0,15 / 0,70 | Muốn tăng sản lượng, cần reference và điều kiện áp dụng |

Đây là trọng số mong muốn do demo đặt ra, chưa phải trọng số suitability đã được kiểm chứng. Đổi mục tiêu làm đổi đầu việc cần kiểm tiếp; không làm thay lượng mưa dự báo hoặc tự tạo phần trăm tăng năng suất.

## Features dùng thật trong ML

| Nhóm | Features | Đơn vị/cách hiểu |
| --- | --- | --- |
| Mưa gần | P_lag1, P_lag2, P_lag3 | Tổng mưa của 1/2/3 tháng trước tháng đích, mm/tháng |
| Mùa năm trước | P_lag12 | Mưa cùng tháng năm trước, mm/tháng |
| Khí hậu gần | T2M_lag1, RH2M_lag1 | Nhiệt độ °C và ẩm không khí % tháng trước |
| Lịch | month_sin, month_cos | Mã hóa tháng đích bằng sin/cos |
| SMAP thử thêm | SFMC_lag1, RZMC_lag1 | Mean ẩm thể tích tháng trước, m³/m³ |

A8 có 8 biến đầu; B10 thêm 2 biến SMAP. Sau lag12, 120 tháng đích 2016–2025 có đủ core; 119 có đủ extension. HGB dùng khả năng xử lý NaN của chính thuật toán cho hàng thiếu; không điền target. Ngày khả dụng lịch sử của sản phẩm hồi cứu chưa được chứng minh, nên đây là hindcast research.

## Preprocessing và Data Fusion đã làm

1. Giữ raw và hash; kiểm đơn vị, ngày trùng, fill value, khoảng vật lý và calendar coverage.
2. POWER: mưa cộng tháng; nhiệt/RH lấy mean. Chỉ cấp giá trị tháng khi đủ ngày. SMAP mean cũng cần đủ ngày calendar. Ngày thiếu không thành 0.
3. Ghép trái POWER–SMAP theo region/month, giữ 142 tháng backbone. Tạo lag trên trục lịch liên tục trước chia train/validation/test.
4. Không fit scaler, imputer hoặc PCA. Cực trị hợp lý được giữ; không xóa mưa lớn để làm metrics tốt hơn.
5. Ảnh giữ grain scene/composite với QA và coverage. Không inner join ảnh 2025 làm mất chuỗi khí hậu 2015–2024.
6. LOCAL giữ các bảng theo station/site/depth/method/source. Không đổi pH KCl thành pH nước bằng một hằng số; không đổi mặn g/L thành EC đất; không gán bảng diện tích đất cấp tỉnh vào thửa ruộng.
7. FARM preferences ghép vào context quyết định theo scenario ID, không nối thành covariates thời tiết. Không nhân bản ba kịch bản thành ba mẫu năng suất đã biết.

## Gaps còn lại và ảnh hưởng

- Chưa có EC, pH/phương pháp/độ sâu và khả năng thoát nước riêng ruộng: chưa xác nhận eligibility theo đất/nước.
- Chưa có giống, cây hiện tại, ngày gieo/thu và nguồn tưới thực: chưa chốt lịch luân canh áp dụng.
- Mưa Mỹ Tho là nguồn thứ cấp với 64/72 ô số, chưa đủ chuỗi 2019–2025 và QC/day boundary: chưa chứng minh sai số mưa ngoài đồng.
- SoilGrids và thí nghiệm ở nơi khác chỉ là context/reference; chưa có nhãn “phương án tốt nhất cho ruộng”.
- Ranh khoảng 2ha từ pack là ranh digitised, chưa phải khảo sát độc lập. Nhãn Mỹ Thành theo user, tọa độ cũ được giữ.

Các thiếu hụt này không cản thí nghiệm ML mưa vùng hoặc mô phỏng mục tiêu, nhưng giới hạn kết luận canh tác. File `gap-ledger.csv` và trạng thái `needs_review` vẫn được truyền tới output.

## Kiểm chứng và bàn giao

DATA v1 có kiểm hash, calendar, lag, conversion và notebook14. Gói AI có manifest ghi rõ nguồn thật và preferences mô phỏng; không có synthetic weather/yield labels. Tests mới kiểm preference weights, unknowns, citation giả, prompt injection và contract forecast null. Kết quả chạy cụ thể nằm trong `runs/ai-baseline-v1/validation-record.json` của Lab.

Gói đầu vào hiện đủ để tái tạo **thí nghiệm nghiên cứu đã thực hiện**, chưa phải dữ liệu cho supervised crop recommendation. Khi có input thực địa, bổ sung vào lớp field management/observations và đánh giá applicability; giữ preferences là lớp mong muốn riêng.
