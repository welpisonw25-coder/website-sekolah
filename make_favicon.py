from PIL import Image

try:
    img = Image.open('images/logo-keerom.png')
    img.save('favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("favicon.ico generated successfully!")
except Exception as e:
    print(f"Error generating favicon.ico: {e}")
