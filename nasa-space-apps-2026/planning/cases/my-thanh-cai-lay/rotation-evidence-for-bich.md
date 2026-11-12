# Bảng đất - nước - cây - mùa để Bích review

> 12/11/2026, bản 1.1. Mỹ Thành được giữ làm địa bàn nghiên cứu. Ba phương án dưới đây là reference scenarios, chưa là lịch canh tác xác minh của MT-BLOCK-01. Không mở rộng địa bàn hoặc giao khảo sát thực địa. Bích review bằng nguồn và ghi giới hạn; không được coi là xác nhận chuyên môn nông học ngoài phạm vi năng lực.

## 7. Bằng chứng chung và cách đọc bảng

**Mục đích:** xác định điều gì có thể đưa vào prototype so sánh và điều gì phải giữ unknown. Không dùng bảng này làm lịch gieo, công thức bón/tưới hoặc kết luận phương án tối ưu cho một ruộng.

| Nhãn | Ý nghĩa | Cách dùng |
| --- | --- | --- |
| HISTORICAL | Có trong nghiên cứu lịch sử tại Cai Lậy/Long Khánh | Dùng làm tham chiếu, giữ địa danh/năm; chưa chuyển sang Mỹ Thành |
| MODEL | Được mô hình dự đoán tại ô chứa tâm block | Hiển thị nguồn và bất định; không thay mẫu đất đo |
| UNKNOWN | Chưa có bằng chứng đủ cho block hoặc rule cụ thể | Hỏi người dùng/ghi thiếu; không chấm là phù hợp |
| SCENARIO | Giả định do team/người dùng chọn | Gắn nhãn, không gọi là hiện trạng hoặc dự báo |

**Nguồn đã kiểm để bắt đầu review:**

- **[S4] CTU 2009, 11:194-199:** methods PDF trang 2 liệt kê ba chuỗi tại Long Khánh; bảng 1 trang 3 mô tả phẫu diện và vật lý đất; bảng 4 trang 5 có kết quả độ bền đoàn lạp. Khác biệt giữa nghiệm thức tại Long Khánh không có ý nghĩa thống kê ở outcome này; không mượn kết quả Vĩnh Mỹ để khẳng định lợi ích chắc chắn. [PDF](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/download/605/3214/3214).
- **[S5] CTU 2009, 11:262-269:** methods PDF trang 2 mô tả đất phù sa Mollic Endoaquept, trong vùng bao đê, thí nghiệm tiếp nối từ 2001; bảng 1 trang 3 cho chuỗi theo vụ. Đánh giá mẫu năm 2005, bảng đất đầu kỳ là năm 2001. Không chứng minh cùng thửa với S4. [PDF](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/download/597/3222/3222).
- **[S2] SoilGrids tại tâm block:** pH H2O mean 6,3 ở ba tầng tới 30 cm, Q05-Q95 4,5-8,3; cát/sét tầng 0-5 cm có khoảng rộng. Đây là MODEL, không xác nhận nhóm đất, EC, tầng đế cày hoặc đồng nhất toàn block. [JSON](study-block-soil-model.json), [CSV](study-block-soil-model.csv).
- **[S6] NASA POWER:** chuỗi điểm vùng 2015-2025 đã có QA/WARN; chưa tính cân bằng nước hay cửa sổ mùa tối ưu cho ba phương án. Mưa không thay lưu lượng tưới, thoát nước hoặc nguồn nước mặn/ngọt.

Giữ riêng đất nghiên cứu lịch sử, đất mô hình tại Mỹ Thành và giá thể demo HCM. Không ghép số đo thành một record hoặc lấy bảng tổng hợp làm raw training samples. Bảng này không thêm ngưỡng pH/EC, thời gian giống hoặc nhu cầu nước khi chưa có tài liệu đúng cây, phương pháp và phạm vi áp dụng.

## 8. R0 - lúa / lúa / lúa

**Vai trò:** đối chứng tham khảo, không mặc định là hiện trạng MT-BLOCK-01. Lịch HISTORICAL [S5, bảng 1]: lúa Đông Xuân -> lúa Hè Thu -> lúa Thu Đông. Chưa có ngày gieo/thu hoặc giống cụ thể để áp năm 2026.

| Yếu tố | Đã có và phạm vi bằng chứng | Chưa đủ tại Mỹ Thành / Bích cần review |
| --- | --- | --- |
| Đất | HISTORICAL: S4 có phẫu diện đất lúa Long Khánh và tầng nén dẽ; S5 mô tả đất phù sa của thí nghiệm Cai Lậy. MODEL: SoilGrids tại tâm block | UNKNOWN nhóm đất thực, đế cày, phèn/mặn, điều kiện rễ. Cần nguồn đất có tỷ lệ bản đồ/vị trí/năm; chưa được chuyển tên đất S5 sang block |
| Nước | S5 là vùng bao đê; đã có khí tượng NASA vùng. Đây chưa là bằng chứng đủ nước cho ba vụ ở block | UNKNOWN nguồn tưới, lịch cấp, độ mặn nước, thoát nước và rủi ro ngập. Không suy “không ngập lũ” thành không úng; chưa tính được tổng nước tưới |
| Cây | HISTORICAL: lúa là cây trong cả ba vụ của đối chứng S4/S5 | UNKNOWN giống, thời gian giống, yêu cầu pH/EC theo phương pháp, sâu bệnh và mục tiêu hộ. Không lấy soil mean làm chứng nhận cây phù hợp |
| Mùa | HISTORICAL: Đông Xuân - Hè Thu - Thu Đông theo bảng S5 | UNKNOWN ngày gieo/thu, khoảng nghỉ và lịch địa phương hiện thời; khung tên vụ chưa bảo đảm ba vụ nối được |

**Kết luận hiện hành:** đủ để đặt R0 cạnh hai lựa chọn trong reference comparison. **Chưa đủ để gọi là baseline nông hộ hiện tại, phù hợp hoặc bền vững ở Mỹ Thành.**

**Bích chốt bằng desk review:** (1) nguồn nào chứng minh lịch lúa hiện tại ở phạm vi xã/block; (2) điều kiện nước/đất nào được biết; (3) thiếu gì phải hỏi người dùng. Nếu không tìm được baseline block, giữ nhãn “đối chứng nghiên cứu”, không điền “đang trồng” vào giao diện.

**Gate đề xuất:** nếu người dùng chưa xác nhận baseline hoặc nước tưới, kết quả = UNKNOWN_FOR_FIELD. Không gán R0 điểm thua mặc định chỉ để làm nổi phương án thay thế.

## 9. R1 - lúa / bắp non / lúa

**Vai trò:** phương án tham khảo thay vụ Hè Thu bằng bắp non/bắp rau. Lịch HISTORICAL [S5, bảng 1]: lúa Đông Xuân -> bắp rau Hè Thu -> lúa Thu Đông. Giữ đúng sản phẩm bắp non; không thay bằng bắp hạt CP888 hoặc bắp nếp.

| Yếu tố | Đã có và phạm vi bằng chứng | Chưa đủ tại Mỹ Thành / Bích cần review |
| --- | --- | --- |
| Đất | HISTORICAL: S4 có chuỗi lúa-bắp non-lúa và mô tả vật lý đất vùng. Đây là lý do phải kiểm điều kiện chuyển lúa sang cây cạn | UNKNOWN khả năng làm đất, tầng nén dẽ, thông khí và thoát nước của block. Cần tài liệu đúng bắp non, nhóm đất và phương pháp; chưa có ngưỡng loại trừ số hóa được |
| Nước | Có chuỗi thí nghiệm tham khảo, chưa có lượng tưới so sánh đủ để chuyển sang block; NASA chỉ cho bối cảnh khí tượng | UNKNOWN cách thoát nước sau lúa, nguồn tưới lúc cần và mặn/phèn. Bích cần xác định điều kiện tưới/tiêu trong mùa bắp; không kết luận “ít nước hơn” theo tên cây |
| Cây | HISTORICAL: bắp non S4 / bắp rau S5 là cây được thử, không phải dữ liệu crop rule đầy đủ | UNKNOWN giống, số ngày đến thu sản phẩm non, yêu cầu đất/nước và đầu ra thị trường. Không dùng ngày thu bắp hạt; không đưa liều phân trong thí nghiệm thành khuyến cáo |
| Mùa | HISTORICAL: thay đúng vụ Hè Thu trong S5, sau đó trở lại lúa Thu Đông | UNKNOWN ngày giải phóng ruộng, chuẩn bị đất, thu bắp và chuẩn bị vụ lúa sau. Phải kiểm cửa sổ giống + thời gian chuyển vụ; chưa chứng minh không xung đột |

**Kết luận hiện hành:** có tiền lệ nghiên cứu cho cấu trúc R1, **chưa đủ khuyến nghị áp dụng tại block**. Không khẳng định chắc cải thiện cấu trúc đất, tiết kiệm nước hoặc tăng lợi nhuận; kết quả phụ thuộc outcome và điều kiện nghiên cứu.

**Bích ưu tiên:** nguồn về (1) bắp non đúng loại sản phẩm; (2) tưới/thoát nước khi chuyển từ ruộng lúa; (3) thời gian giống và khả năng trở lại vụ lúa sau. Ghi rõ địa bàn, mùa, phương pháp và bằng chứng có chuyển giao được không.

**Gate đề xuất:** chưa biết tưới/tiêu hoặc cửa sổ chuyển vụ -> UNKNOWN_FOR_FIELD. Chỉ đánh CONSTRAINT_VIOLATED khi có rule có nguồn và giá trị đầu vào đủ để đối chiếu; không tự đặt threshold.

## 10. R2 - lúa / đậu xanh / lúa

**Vai trò:** phương án tham khảo thay vụ Hè Thu bằng đậu xanh. Lịch HISTORICAL [S5, bảng 1]: lúa Đông Xuân -> đậu xanh Hè Thu -> lúa Thu Đông. Không thay bằng đậu phộng GV10, đậu nành hoặc suy rằng mọi cây họ đậu có cùng yêu cầu.

| Yếu tố | Đã có và phạm vi bằng chứng | Chưa đủ tại Mỹ Thành / Bích cần review |
| --- | --- | --- |
| Đất | HISTORICAL: chuỗi lúa-đậu xanh-lúa có trong S4/S5; S5 có thí nghiệm dinh dưỡng/chất hữu cơ của hệ luân canh | UNKNOWN ngưỡng pH/EC theo phương pháp, điều kiện rễ/thoát nước tại block. Không suy cố định N hoặc lợi ích đất tại Mỹ Thành chỉ vì có cây họ đậu |
| Nước | Có tiền lệ luân canh trong nghiên cứu, chưa có lượng tưới/tiêu của block; mưa NASA chưa phản ánh nước khả dụng vùng rễ | UNKNOWN rủi ro úng, thời điểm tưới và nguồn nước. Cần tài liệu yêu cầu nước đúng đậu xanh và giai đoạn; chưa tính được % tiết kiệm nước |
| Cây | HISTORICAL: đậu xanh là cây thử ở vụ giữa | UNKNOWN giống, thời gian thu, yêu cầu dinh dưỡng/bệnh và cách xử lý tàn dư. Không gán lượng N bổ sung hoặc lợi nhuận khi chưa có số đúng bối cảnh |
| Mùa | HISTORICAL: thay Hè Thu rồi trở về lúa Thu Đông theo S5 | UNKNOWN ngày gieo/thu, mưa lúc thu, thời gian làm đất và lịch vụ sau. Cần kiểm lịch giống cụ thể với cửa sổ địa phương; tên vụ chưa đủ |

**Kết luận hiện hành:** đủ làm reference scenario cùng R0/R1, **chưa đủ gọi R2 tốt nhất hoặc phù hợp cho ruộng**. Không mặc định xếp trên R1 vì là cây họ đậu.

**Bích ưu tiên:** tài liệu đúng đậu xanh về đất/úng/tưới, thời gian giống và thời điểm thu; bằng chứng nào hỗ trợ mục tiêu người dùng, bằng chứng nào chỉ là kỳ vọng. Kết quả cần so với R0 trên cùng outcome có nguồn, không gộp thành một điểm soil health tùy ý.

**Gate và cách review chung:** UNKNOWN_FOR_FIELD = thiếu điều kiện quan trọng; REFERENCE_ONLY = đủ giải thích lịch sử, chưa chuyển giao; CONSTRAINT_VIOLATED = có rule + input chứng minh xung đột. Đây là nhãn thiết kế đề xuất, chưa là model đã triển khai. CSV có 12 hàng đất/nước/cây/mùa để Bích ghi nguồn mới, reviewer_decision, reviewer_note và review_date. Để trống các ô review tới khi Bích thật sự review.
