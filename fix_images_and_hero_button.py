import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix nút "Tải File Trình Chiếu" ở Hero section
old_hero_buttons = r'(<button class="w-full sm:w-auto bg-white text-slate-900 px-8 py-4 rounded-full font-semibold hover:bg-slate-100 transition shadow-xl"[^>]*>.*?Khám Phá Dự Án.*?</button>)\s*(<button class="w-full sm:w-auto glass-panel text-white px-8 py-4 rounded-full font-medium hover:bg-white/10 transition">.*?Tải File Trình Chiếu.*?</button>)'

new_hero_buttons = r'\1\n                <button onclick="document.getElementById(\'contact-modal\').classList.add(\'active\')" class="w-full sm:w-auto glass-panel text-white px-8 py-4 rounded-full font-medium hover:bg-white/10 transition">Đăng Ký Nhận Tài Liệu</button>'

html = re.sub(old_hero_buttons, new_hero_buttons, html, flags=re.DOTALL)

# 2. Đảm bảo TẤT CẢ ảnh trong Visual Showcase có glightbox
# Tìm phần Visual Showcase và đảm bảo tất cả <a> tag có class glightbox
visual_section = re.search(r'(<!-- Visual Showcase -->.*?</section>)', html, flags=re.DOTALL)
if visual_section:
    visual_html = visual_section.group(1)
    # Thêm class glightbox cho mọi <a> có href chứa .jpg/.jpeg/.png
    visual_html = re.sub(r'<a href="([^"]+\.(jpg|jpeg|png|JPG|PNG|webp))"(?![^>]*glightbox)', r'<a href="\1" class="glightbox"', visual_html)
    html = html.replace(visual_section.group(1), visual_html)

# 3. Cải thiện JS GLightbox initialization - đảm bảo bắt mọi ảnh
old_lightbox_js = re.search(r'(// Thêm class glightbox vào TẤT CẢ các link ảnh.*?lightbox\.reload\(\);)', html, flags=re.DOTALL)
if old_lightbox_js:
    new_lightbox_js = '''// Thêm class glightbox vào TẤT CẢ các link ảnh (bao gồm Visual Showcase, bảng giá, chính sách...)
            document.querySelectorAll('a').forEach(link => {
                const href = link.getAttribute('href');
                if (href && href.match(/\\.(jpeg|jpg|gif|png|webp|JPG|PNG)$/i)) {
                    link.classList.add('glightbox');
                    link.removeAttribute('target');
                    // Xóa data-fslightbox nếu có
                    if (link.hasAttribute('data-fslightbox')) {
                        link.removeAttribute('data-fslightbox');
                    }
                }
            });
            
            // Refresh lightbox để nhận ảnh mới
            lightbox.reload();'''
    html = html.replace(old_lightbox_js.group(1), new_lightbox_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Done!")
print("1. Nút 'Tải File Trình Chiếu' ở Hero → mở form đăng ký")
print("2. TẤT CẢ ảnh → click phóng to với GLightbox")
