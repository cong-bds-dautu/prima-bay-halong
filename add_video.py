import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Tìm Hero Section và thêm video section ngay sau nó
hero_end = html.find('    <!-- Project Info Cards -->')

video_section = """
    <!-- Video Section -->
    <section class="py-24 bg-slate-900/80 relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-900 via-slate-900/50 to-slate-900"></div>
        <div class="max-w-7xl mx-auto px-6 relative z-10">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-5xl font-bold mb-4">Video Giới Thiệu Dự Án</h2>
                <p class="text-slate-400">Khám phá Prima Bay Hạ Long qua video</p>
            </div>
            <div class="max-w-5xl mx-auto">
                <div class="rounded-4xl overflow-hidden shadow-2xl glass-panel p-2">
                    <div class="relative" style="padding-bottom: 56.25%; height: 0;">
                        <iframe 
                            src="https://drive.google.com/file/d/1w_J7bAKNKWut7FYFGlFRV13GpHj1LNCX/preview" 
                            class="absolute top-0 left-0 w-full h-full rounded-3xl"
                            allow="autoplay; fullscreen"
                            allowfullscreen
                            style="border: none;">
                        </iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""

html = html[:hero_end] + video_section + html[hero_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Video section added!")
