import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Sửa Navbar
old_nav = r'<div class="hidden md:flex space-x-8 text-sm font-medium text-slate-300">.*?</div>'
new_nav = '''<div class="hidden md:flex space-x-8 text-sm font-medium text-slate-300">
                <a href="#video-gallery" class="hover:text-white transition">Thư Viện Video</a>
                <a href="#tong-quan" class="hover:text-white transition">Tổng Quan</a>
                <a href="#vi-tri" class="hover:text-white transition">Vị Trí</a>
                <a href="#san-pham" class="hover:text-white transition">Sản Phẩm</a>
                <a href="#tien-ich" class="hover:text-white transition">Tiện Ích</a>
            </div>'''
html = re.sub(old_nav, new_nav, html, flags=re.DOTALL)

# 2. Tách các sections
hero_match = re.search(r'(<section class="relative h-screen.*?</section>)', html, flags=re.DOTALL)
hero = hero_match.group(1) if hero_match else ''

video_gallery_match = re.search(r'(<!-- Thư Viện Video -->.*?<!-- Video Gallery Modal -->.*?</script>)', html, flags=re.DOTALL)
video_gallery = video_gallery_match.group(1) if video_gallery_match else ''

video_intro_match = re.search(r'(<!-- Video Section -->.*?</section>)', html, flags=re.DOTALL)
video_intro = video_intro_match.group(1) if video_intro_match else ''

project_info_match = re.search(r'(<!-- Project Info Cards -->.*?(?=<!-- Visual Showcase -->))', html, flags=re.DOTALL)
project_info = project_info_match.group(1) if project_info_match else ''

visual_match = re.search(r'(<!-- Visual Showcase -->.*?(?=<!-- Vị Trí Ấn Tượng -->))', html, flags=re.DOTALL)
visual = visual_match.group(1) if visual_match else ''

vi_tri_match = re.search(r'(<!-- Vị Trí Ấn Tượng -->.*?(?=<!-- Floor Plans -->))', html, flags=re.DOTALL)
vi_tri = vi_tri_match.group(1) if vi_tri_match else ''

mat_bang_match = re.search(r'(<!-- Floor Plans -->.*?(?=<!-- Sản Phẩm Mới))', html, flags=re.DOTALL)
mat_bang = mat_bang_match.group(1) if mat_bang_match else ''

san_pham_match = re.search(r'(<!-- Sản Phẩm Mới.*?</section>)', html, flags=re.DOTALL)
san_pham = san_pham_match.group(1) if san_pham_match else ''

thuc_te_match = re.search(r'(<!-- Thực Tế Trung Thực Land -->.*?(?=<!-- Footer CTA -->))', html, flags=re.DOTALL)
thuc_te = thuc_te_match.group(1) if thuc_te_match else ''

footer_cta_match = re.search(r'(<!-- Footer CTA -->.*?(?=<!-- Footer Chuyên Nghiệp -->))', html, flags=re.DOTALL)
footer_cta = footer_cta_match.group(1) if footer_cta_match else ''

footer_match = re.search(r'(<!-- Footer Chuyên Nghiệp -->.*?(?=<!-- Video Modal -->))', html, flags=re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

modals_match = re.search(r'(<!-- Video Modal -->.*$)', html, flags=re.DOTALL)
modals = modals_match.group(1) if modals_match else ''

# 3. Thêm id="tien-ich" cho phần tiện ích trong san_pham
san_pham = san_pham.replace('<!-- TIỆN ÍCH HẤP DẪN -->', '<div id="tien-ich"></div>\n            <!-- TIỆN ÍCH HẤP DẪN -->')

# 4. Rebuild HTML với thứ tự mới
head_end = html.find('</head>')
head = html[:head_end + 7]

body_start = html.find('<body')
body_tag = html[body_start:html.find('>', body_start) + 1]

nav_match = re.search(r'(<nav.*?</nav>)', html, flags=re.DOTALL)
nav = nav_match.group(1) if nav_match else ''

new_body = f'''{body_tag}

    {nav}

    {hero}

    {video_gallery}

    {video_intro}

    {project_info}

    {visual}

    {vi_tri}

    {mat_bang}

    {san_pham}

    {thuc_te}

    {footer_cta}

    {footer}

    {modals}
'''

final_html = head + new_body

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("✅ Đã sắp xếp lại cấu trúc:")
print("1. Navbar: Thư Viện Video → Tổng Quan → Vị Trí → Sản Phẩm → Tiện Ích")
print("2. Sections: Hero → Thư viện Video → Video intro → Tổng quan → Vị trí → Mặt bằng → Sản phẩm → Tiện ích → Thực tế → Footer")
