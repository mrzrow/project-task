from PIL import Image, ImageFont, ImageDraw
from typing import Tuple

def generate_sub(name: str, pos: str, font: ImageFont,
                 bg: Tuple[int, int, int], color: Tuple[int, int, int],
                 save_to: str) -> None:
    w, h = 1920, 512

    fname = ImageFont.truetype(font=font, size=64)
    fpos = ImageFont.truetype(font=font, size=50)

    _, _, *fname_size = fname.getbbox(name)
    _, _, *fpos_size = fpos.getbbox(pos)
    w_name, h_name = fname_size
    w_pos, h_pos = fpos_size

    image = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(image)

    point_name = ((w - w_name) // 2, (h - h_name - h_pos) // 2)
    point_pos = ((w - w_pos) // 2, (h + h_name + h_pos) // 2)

    draw.multiline_text(point_name, name, font=fname, fill=color)
    draw.multiline_text(point_pos, pos, font=fpos, fill=color)

    image.save(save_to)


if __name__ == "__main__":
    name = input("Full name: ")
    pos = input("Position at work: ")
    font = input("Path to font: ")
    bg = tuple(map(int, input("Background color: ").split()))
    color = tuple(map(int, input("Text color: ").split()))
    save_to = input("Save image to: ")
    
    generate_sub(name, pos, font, bg, color, save_to)