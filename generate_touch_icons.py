from PIL import Image
import os

img = Image.open('images/logo-keerom.png').convert('RGBA')
w, h = img.size
print(f"Original logo size: {w}x{h}")

def make_square_icon(src_img, target_size, bg_color=(255, 255, 255, 255)):
    # Create target square canvas
    canvas = Image.new('RGBA', (target_size, target_size), bg_color)
    
    # Calculate scale to fit inside target_size with nice padding (e.g. 85% of canvas)
    pad = int(target_size * 0.08)
    avail_w = target_size - (pad * 2)
    avail_h = target_size - (pad * 2)
    
    scale = min(avail_w / src_img.width, avail_h / src_img.height)
    new_w = int(src_img.width * scale)
    new_h = int(src_img.height * scale)
    
    resized = src_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    offset_x = (target_size - new_w) // 2
    offset_y = (target_size - new_h) // 2
    
    canvas.paste(resized, (offset_x, offset_y), resized if resized.mode == 'RGBA' else None)
    return canvas

# 192x192
icon_192 = make_square_icon(img, 192)
icon_192.save('images/logo-keerom-192.png', 'PNG')
icon_192.save('apple-touch-icon.png', 'PNG')
icon_192.save('apple-touch-icon-precomposed.png', 'PNG')
icon_192.save('images/apple-touch-icon.png', 'PNG')

# 512x512
icon_512 = make_square_icon(img, 512)
icon_512.save('images/logo-keerom-512.png', 'PNG')

# 180x180 for Apple
icon_180 = make_square_icon(img, 180)
icon_180.save('images/apple-touch-icon-180.png', 'PNG')

# 32x32 and 16x16
icon_32 = make_square_icon(img, 32)
icon_32.save('images/favicon-32x32.png', 'PNG')

# Multi-size ICO for root
icon_512.save('favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)])

print("Generated all touch icons and favicons successfully!")
