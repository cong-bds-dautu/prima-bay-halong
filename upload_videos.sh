#!/bin/bash
FOLDER_ID="1i0kgZRvq46e9HedM0LIMn_dxR4EuVNp2"
VIDEOS=(
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/05. Social posts/6. HÀ NỘI - PRIMA BAY: CHẠM NHỊP SIÊU KẾT NỐI/Siêu kết nối HN - Prima Bay.mp4"
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/05. Social posts/8. Tầm nhìn đa lớp/BIM_PrimaBay_Tầm nhìn đa lớp_1.mp4"
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/05. Social posts/1. Post 1 - Video giới thiệu Logo/Prima logo.mp4"
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/04. Phim/Phim_ Clip Prima Bay/Nhịp sống Prima Bay.mp4"
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/04. Phim/Phim_ Clip Prima Bay/Clip ra mắt logo Prima Bay.mp4"
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/04. Phim/Phim_ Clip Prima Bay/Prima Bay_Nơi mọi trải nghiệm bắt đầu.mp4"
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/04. Phim/Phim_ Clip Prima Bay/Prima Bay_Tầm nhìn đa lớp.mp4"
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/04. Phim/Phim_ Clip Halong Marina/Giá trị bền vững của Halong Marina.mp4"
  "../chu-dau-tu/PRIMA BAY_THÔNG TIN DỰ ÁN/05. Marketing/04. Phim/Phim_ Clip Halong Marina/Dư địa phát triển Halong Marina.mp4"
  "../trung-thuc-land/TTL- PRIMA BAY/4. Tài liệu Marketing/video/0517.mp4"
  "../trung-thuc-land/TTL- PRIMA BAY/4. Tài liệu Marketing/video/0515.mp4"
  "../trung-thuc-land/TTL- PRIMA BAY/4. Tài liệu Marketing/video/0516.mp4"
)

echo "[" > uploaded_videos.json
for file in "${VIDEOS[@]}"; do
  echo "Uploading: $file"
  NAME=$(basename "$file" .mp4)
  RES=$(gog drive upload "$file" --parent "$FOLDER_ID" --json)
  ID=$(echo "$RES" | grep -o '"id": *"[^"]*"' | cut -d'"' -f4)
  if [ ! -z "$ID" ]; then
    gog drive share "$ID" --to anyone --role reader --discoverable --force
    echo "  {\"name\": \"$NAME\", \"id\": \"$ID\"}," >> uploaded_videos.json
  fi
done
echo "]" >> uploaded_videos.json
