"""Generate cover image for Apple × Gemini article."""
import struct, zlib, os

def create_png(width, height, r, g, b):
    def chunk(chunk_type, data):
        c = chunk_type + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    header = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    raw = b''
    for y in range(height):
        raw += b'\x00'
        for x in range(width):
            raw += bytes([r, g, b])
    idat = chunk(b'IDAT', zlib.compress(raw))
    iend = chunk(b'IEND', b'')
    return header + ihdr + idat + iend

# Try to use PIL for a better image
try:
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new('RGB', (900, 500), '#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Try to load fonts
    font_dir = "/System/Library/Fonts"
    try:
        title_font = ImageFont.truetype(os.path.join(font_dir, "Helvetica.ttc"), 52)
        sub_font = ImageFont.truetype(os.path.join(font_dir, "Helvetica.ttc"), 26)
        label_font = ImageFont.truetype(os.path.join(font_dir, "Helvetica.ttc"), 18)
    except:
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 52)
            sub_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 26)
            label_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 18)
        except:
            title_font = ImageFont.load_default()
            sub_font = title_font
            label_font = title_font
    
    # Draw background gradient (simulated)
    for y in range(500):
        blend = y / 500
        r = int(26 * (1 - blend) + 22 * blend)
        g = int(26 * (1 - blend) + 33 * blend)
        b = int(46 * (1 - blend) + 62 * blend)
        for x in range(900):
            img.putpixel((x, y), (r, g, b))
    
    # Draw decorative line
    draw.rectangle([60, 80, 120, 83], fill='#ff8c42')
    
    # Draw Apple logo (simple)
    draw.ellipse([50, 130, 130, 210], outline='#ff8c42', width=3)
    # actually just draw a circle for simplicity
    
    # Title
    draw.text((60, 130), "Apple × Gemini", fill='#ffffff', font=title_font)
    draw.text((60, 200), "是投降，还是聪明？", fill='#ff8c42', font=sub_font)
    
    # Label
    draw.text((60, 260), "猿来AI · WWDC 2026 深度解读", fill='#888888', font=label_font)
    
    # Small decorative
    draw.rectangle([60, 320, 200, 322], fill='#ff8c42')
    
    img.save('/tmp/cover-apple-gemini.png')
    print("Cover image created with PIL at /tmp/cover-apple-gemini.png")
    
except ImportError:
    png_data = create_png(900, 500, 26, 26, 46)
    with open('/tmp/cover-apple-gemini.png', 'wb') as f:
        f.write(png_data)
    print("Cover image created (simple) at /tmp/cover-apple-gemini.png")
