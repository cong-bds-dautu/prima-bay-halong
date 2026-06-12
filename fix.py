import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the old #san-pham section completely
html = re.sub(r'<!-- Sản phẩm & Tiềm năng từ 2 website tham khảo -->.*?<!-- Hình ảnh tham khảo từ 2 website -->', '<!-- Hình ảnh tham khảo từ 2 website -->', html, flags=re.DOTALL)

# Find the end of #mat-bang section
mat_bang_end = html.find('<!-- Thực Tế Trung Thực Land -->')

# Insert the new product sections right before "Thực Tế Trung Thực Land"
new_sections = """
    <!-- Sản Phẩm Mới (Theo primahalong.com) -->
    <section id="san-pham" class="py-24 bg-slate-900/60">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-bold mb-4">SẢN PHẨM</h2>
                <p class="text-slate-400 max-w-3xl mx-auto">Dự án phát triển đa dạng loại hình căn hộ từ Studio, Studio Plus đến 2PN, 3PN và Duplex với diện tích linh hoạt từ 29m² – 107m², đáp ứng nhu cầu an cư, nghỉ dưỡng và đầu tư khai thác lưu trú cao cấp.</p>
            </div>

            <!-- Boutique Hotel & Shoplot -->
            <div class="mb-16">
                <h3 class="text-2xl font-bold text-sky-400 mb-6">Boutique Hotel & Shoplot Prima Bay Hạ Long</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div>
                        <p class="text-slate-300 leading-relaxed mb-4">Prima Bay Hạ Long sở hữu dòng sản phẩm Boutique Hotel và Shoplot khối đế cao cấp, kết nối trực tiếp hệ tiện ích nghỉ dưỡng – thương mại – giải trí sôi động tại Halong Marina.</p>
                        <p class="text-slate-300 leading-relaxed">Mặt bằng Prima Bay Hạ Long được thiết kế khoa học theo mô hình căn hộ nghỉ dưỡng cao cấp, tối ưu khả năng đón sáng, thông gió và tầm nhìn về cảnh quan nội khu. Thiết kế hành lang, lõi thang máy và khu tiện ích được sắp xếp hợp lý, giúp cư dân di chuyển thuận tiện.</p>
                    </div>
                    <div class="rounded-4xl overflow-hidden glass-panel">
                        <a href="assets/external/shoplot-prima-bay.jpg" class="glightbox">
                            <img src="assets/external/shoplot-prima-bay.jpg" class="w-full h-auto object-cover img-hover" alt="Shoplot Boutique Hotel">
                        </a>
                    </div>
                </div>
            </div>

            <!-- Căn hộ Studio -->
            <div class="mb-16">
                <h3 class="text-2xl font-bold text-sky-400 mb-6 uppercase">CĂN HỘ STUDIO</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="order-2 md:order-1 rounded-4xl overflow-hidden glass-panel">
                        <a href="assets/external/studio-prima-bay.jpeg" class="glightbox">
                            <img src="assets/external/studio-prima-bay.jpeg" class="w-full h-auto object-cover img-hover" alt="Căn hộ Studio">
                        </a>
                    </div>
                    <div class="order-1 md:order-2">
                        <p class="text-slate-300 leading-relaxed mb-4">Căn hộ Studio tại Prima Bay Hạ Long được phát triển theo xu hướng nghỉ dưỡng hiện đại với thiết kế thông minh, tối ưu không gian sử dụng. Diện tích nhỏ gọn nhưng vẫn đảm bảo sự tiện nghi.</p>
                        <ul class="space-y-3 text-slate-300 list-disc list-inside ml-4">
                            <li>Diện tích linh hoạt từ khoảng 29,2 – 35,5m².</li>
                            <li>Thiết kế không gian mở kết hợp khu bếp, phòng khách và khu nghỉ ngơi.</li>
                            <li>Sở hữu logia riêng giúp đón gió và ánh sáng tự nhiên.</li>
                            <li>Hệ cửa kính lớn tạo cảm giác thoáng đãng và mở rộng tầm nhìn.</li>
                            <li>Phù hợp với người độc thân, cặp đôi trẻ...</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Căn hộ 1 Phòng Ngủ -->
            <div class="mb-16">
                <h3 class="text-2xl font-bold text-sky-400 mb-6 uppercase">CĂN HỘ 1 Phòng Ngủ</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div>
                        <p class="text-slate-300 leading-relaxed mb-4">Căn hộ 1 phòng ngủ tại Prima Bay được thiết kế theo phong cách hiện đại với không gian sống sang trọng, tối ưu công năng và đề cao trải nghiệm nghỉ dưỡng ven biển.</p>
                        <ul class="space-y-3 text-slate-300 list-disc list-inside ml-4">
                            <li>Diện tích đa dạng từ khoảng 47,3 – 72,1m².</li>
                            <li>Thiết kế tối ưu gồm phòng khách, khu bếp và phòng ngủ riêng biệt.</li>
                            <li>Sở hữu logia riêng giúp đón ánh sáng và gió tự nhiên.</li>
                            <li>Hệ cửa kính lớn mở rộng tầm nhìn và tăng độ thông thoáng cho căn hộ.</li>
                            <li>Phù hợp cho khách hàng an cư, nghỉ dưỡng hoặc cho thuê tại Hạ Long.</li>
                        </ul>
                    </div>
                    <div class="rounded-4xl overflow-hidden glass-panel">
                        <a href="assets/external/can-ho-2pn-prima-bay.jpg" class="glightbox">
                            <img src="assets/external/can-ho-2pn-prima-bay.jpg" class="w-full h-auto object-cover img-hover" alt="Căn hộ 1 Phòng Ngủ">
                        </a>
                    </div>
                </div>
            </div>

            <!-- Căn hộ 2 Phòng Ngủ -->
            <div class="mb-16">
                <h3 class="text-2xl font-bold text-sky-400 mb-6 uppercase">CĂN HỘ 2 Phòng Ngủ</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="order-2 md:order-1 rounded-4xl overflow-hidden glass-panel">
                        <a href="assets/external/noi-that-can-ho-prima-bay.jpeg" class="glightbox">
                            <img src="assets/external/noi-that-can-ho-prima-bay.jpeg" class="w-full h-auto object-cover img-hover" alt="Căn hộ 2 Phòng Ngủ">
                        </a>
                    </div>
                    <div class="order-1 md:order-2">
                        <p class="text-slate-300 leading-relaxed mb-4">Căn hộ 2 phòng ngủ tại Dự Án Prima Bay theo phong cách sống hiện đại với không gian rộng rãi, bố trí khoa học và sử dụng vật liệu hoàn thiện cao cấp. Thiết kế chú trọng sự riêng tư, tối ưu ánh sáng tự nhiên.</p>
                        <ul class="space-y-3 text-slate-300 list-disc list-inside ml-4">
                            <li>Diện tích đa dạng từ khoảng 70,6 – 89m².</li>
                            <li>Công năng gồm 2 phòng ngủ, phòng khách, khu bếp và 1–2 WC tiện nghi.</li>
                            <li>Sở hữu logia riêng, không gian sinh hoạt rộng và khu bếp bố trí hợp lý.</li>
                            <li>Các phòng đều có cửa sổ hoặc mặt thoáng giúp đón gió và ánh sáng tự nhiên.</li>
                            <li>Phù hợp với gia đình trẻ, khách hàng nghỉ dưỡng dài ngày hoặc cho thuê.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Bàn Giao & Tiện Ích -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-12">
                <div class="glass-panel p-8 rounded-4xl">
                    <h3 class="text-2xl font-bold mb-4 uppercase">BÀN GIAO NỘI THẤT CĂN HỘ</h3>
                    <p class="text-slate-300 leading-relaxed mb-4">Căn hộ Prima Bay Hạ Long được bàn giao theo tiêu chuẩn hoàn thiện cao cấp với phong cách hiện đại. Mỗi căn hộ được bố trí khoa học với hệ cửa kính lớn đón ánh sáng tự nhiên, vật liệu hoàn thiện tinh tế cùng tông màu thanh lịch.</p>
                </div>
                <div class="glass-panel p-8 rounded-4xl">
                    <h3 class="text-2xl font-bold mb-4 uppercase">MẢNH GHÉP MỚI CHO HALONG MARINA</h3>
                    <ul class="space-y-2 text-slate-300 list-disc list-inside">
                        <li>Cách bãi biển chỉ vài bước chân</li>
                        <li>Gần quảng trường biển, phố đi bộ</li>
                        <li>Kết nối nhanh Tuần Châu – Hòn Gai</li>
                        <li>View trực diện vịnh Hạ long</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

"""

final_html = html[:mat_bang_end] + new_sections + html[mat_bang_end:]

# Xoá luôn phần hình ảnh tham khảo dư thừa (nếu còn)
final_html = re.sub(r'<!-- Hình ảnh tham khảo từ 2 website -->.*?<!-- Floor Plans -->', '<!-- Floor Plans -->', final_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Done updating index.html")
