# RAG v4: phương pháp, cẩm nang và bằng chứng

Corpus chính giữ đúng17 bilingual evidence cards v2, không thêm tài liệu để lấy lợi thế so sánh. BM25 + character TF-IDF lấy top3; card top1 đi qua gate từ vựng, chặn câu hỏi số đo/current sensor không có quan trắc và kiểm source bytes SHA256. Threshold refined .4 được chốt bằng development/exposed regression trước final. Lượt đầu từ chối nhầm câu FAO được giữ như failed experiment, không xóa.

## Các cẩm nang/nghiên cứu thực sự được dẫn

| Card / nguồn | Nội dung được sử dụng | Locator và giới hạn |
|---|---|---|
| rice-awd-2024 / MARD2024 | [Sổ tay quy trình lúa ĐBSCL2024](https://khuyennongvn.gov.vn/data/documents/0/2024/03/29/hangweb/so-tay-huong-dan-quy-trinh-1-trieu-ha-dbscl-ngay-27-3-2024.pdf), quản lý nước AWD | PDF35/printed27 section4; cần điều khiển nước và đo mực nước ruộng; mưa tháng không thay phép đo |
| mungbean-water / VN_MUNGBEAN_MEKONG | [Quy trình sản xuất đậu xanh ĐBSCL](https://harc-ias.vn/storage/uploads/files/QTKT%20SX%20dau%20xanh%20DBSCL_%20Final%281%29.pdf) | PDF3 section4.1; tránh úng/mặn/phèn, điều kiện tại ruộng vẫn chưa biết |
| babycorn-water/duration / VN_BABYCORN_GUIDE | [Tài liệu thực hành cây lương thực](https://elib.vnuf.edu.vn/bitstream/123456789/9570/1/Tai%20lieu%20huong%20dan%20thuc%20hanh%20cay%20luong%20thuc.pdf) | PDF52–53; first harvest khác ngày giải phóng đất; tưới–tiêu cần xác nhận |
| rotation-historic / LOCAL_ROT2009 | [Nghiên cứu CTU597 tại Cai Lậy](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/view/597) | Table4/PDF6; các chuỗi là reference, không phải nhãn phương án tốt nhất cho ruộng hiện tại |
| rotation-soil-ctu / CTU605 | [CTU về cơ chế vật lý đất luân canh](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/download/605/3214/3214) | PDF1 abstract/PDF3 design; không chuyển mức cải thiện sang địa bàn hiện tại |

Card khác gồm crop-water-formula (ETc=Kc×ET0), SoilGrids/optical limits, SMAP moisture, POWER variables, phương pháp pH H2O/KCl, salinity-scope và rotation counterexample. Bản source IDs/URL/hash/locator đầy đủ: Lab reports/v3/evidence/corpus-frozen.json. Đây là tổng hợp provenance đã audit trước đó, không tuyên bố vừa có chuyên gia xác nhận lại từng trang. Hash xác minh file, không xác minh semantic interpretation tự động.

## Validation RAG thực tế

Development19 câu:11 answerable +8 unanswerable. V2 trả lời8/8 câu thiếu bằng chứng; gate v4 từ chối8/8 và giữ11/11 câu dương. Bỏ sufficiency gate làm cả8 lỗi quay lại. Kiểm source substitution và sửa file sau lượt trả lời đầu chứng minh integrity gate có tác dụng; bỏ integrity gate không phát hiện fault.

Final tự biên soạn16 câu tách development: positive evidence agreement8/8 và retrieval recall@3=100%; đúng abstention6/8 (75%), v2 chỉ1/8 (12,5%). Literal card support và byte-verified citation share đạt100% trên các câu đã trả. Hai câu sai còn lại liên quan futures/margin gạo và an toàn biến đổi gen bắp non. Vì vậy không gọi groundedness100% theo chuyên gia: câu có thể trích đúng card nhưng card không trả lời đúng câu hỏi.

Original v2 final24 câu đã lộ được dùng regression guard16/16 positive +8/8 abstention; không gọi đó là test mới. Không dùng LLM tự chấm làm bằng chứng duy nhất; không có expert gold, semantic contradiction detector tổng quát, domain sign-off hay farmer study. Conflicts do người dùng nhập vẫn chặn đề xuất áp dụng.

Triển khai: chỉ có metadata/cards chưa đủ. Máy chạy RAG v4 phải có đúng cached source bytes cho citation; file thiếu/sai hash thì abstain. API status báo verified_cards/total_cards và ready/partial. Không bỏ gate để làm demo trông đầy đủ. Corpus cần khoảng76,8MB source bytes được tham chiếu, không phải toàn bộ ảnh/PDF của dự án; quyền chia sẻ source gốc cần xem riêng trước khi phát hành rộng.
