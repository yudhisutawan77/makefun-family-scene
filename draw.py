"""Render the family scene illustration (1024x1024 PNG).

Scene: a little girl shows Grandpa her first robot drawing, taped to the
fridge right over his engineering degree. Grandpa studies it, delighted.
The caption band at the bottom carries the entry text itself.
"""
import textwrap

from PIL import Image, ImageDraw, ImageFont

SIDE = 1024
OUTPUT_PATH = "entry.png"
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"

WALL = (251, 243, 228)
FLOORBOARD = (214, 178, 134)
FRIDGE_BODY = (191, 227, 208)
FRIDGE_TRIM = (120, 170, 145)
SHEET = (255, 255, 250)
FRAME_GOLD = (212, 175, 55)
DEEP_BLUE = (38, 54, 84)
BRIGHT_RED = (214, 69, 65)
SKIN_YOUNG = (244, 205, 170)
SKIN_OLD = (232, 190, 155)
GIRL_HAIR = (90, 58, 32)
SILVER = (200, 200, 205)
CARDIGAN = (74, 105, 150)
FROCK = (214, 69, 65)
SNOW = (255, 255, 255)
PENCIL = (40, 40, 40)

ENTRY_TEXT = ("My daughter taped her first robot drawing to Grandpa's fridge, "
              "right over his engineering degree. He studied it for a long "
              "time, then said, 'Mine never had a cape.'")


def load_font(size, bold=False):
    fname = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(FONT_DIR + fname, size)


def paint_wall_dots(canvas):
    for (x, y, r) in [(80, 90, 14), (940, 120, 18), (700, 90, 10),
                      (60, 700, 12), (960, 700, 10)]:
        canvas.ellipse([x - r, y - r, x + r, y + r], fill=(245, 222, 180))


def paint_fridge(canvas):
    canvas.rounded_rectangle([120, 130, 560, 830], radius=36,
                             fill=FRIDGE_BODY, outline=FRIDGE_TRIM, width=6)
    canvas.line([120, 300, 560, 300], fill=FRIDGE_TRIM, width=5)
    canvas.rounded_rectangle([500, 170, 528, 260], radius=10, fill=FRIDGE_TRIM)
    canvas.rounded_rectangle([500, 340, 528, 430], radius=10, fill=FRIDGE_TRIM)
    # plant on top of the fridge
    canvas.ellipse([300, 84, 380, 128], fill=(96, 150, 90))
    canvas.ellipse([330, 60, 400, 118], fill=(120, 175, 110))
    canvas.rectangle([315, 108, 365, 132], fill=(196, 110, 70))


def paint_degree(canvas):
    # framed engineering degree, half hidden behind the robot drawing
    canvas.rectangle([180, 350, 330, 470], fill=(255, 252, 240),
                     outline=FRAME_GOLD, width=8)
    canvas.rectangle([198, 368, 312, 452], outline=FRAME_GOLD, width=2)
    for i, y in enumerate([388, 404, 420, 436]):
        canvas.line([212, y, 298 - i * 8, y], fill=(120, 110, 80), width=3)


def paint_crayon_robot(canvas):
    # crayon robot: box head, antenna, cape
    canvas.rectangle([320, 380, 400, 440], outline=PENCIL, width=5)
    canvas.line([360, 380, 360, 360], fill=PENCIL, width=4)
    canvas.ellipse([352, 348, 368, 364], fill=BRIGHT_RED)
    canvas.ellipse([338, 402, 352, 416], fill=PENCIL)
    canvas.ellipse([368, 402, 382, 416], fill=PENCIL)
    canvas.line([344, 428, 376, 428], fill=PENCIL, width=4)
    canvas.rectangle([330, 445, 390, 505], outline=PENCIL, width=5)
    canvas.polygon([(330, 445), (300, 520), (330, 505)], fill=BRIGHT_RED)
    canvas.polygon([(390, 445), (420, 520), (390, 505)], fill=BRIGHT_RED)
    canvas.line([300, 470, 330, 470], fill=PENCIL, width=4)
    canvas.line([390, 470, 420, 470], fill=PENCIL, width=4)
    canvas.line([345, 505, 345, 530], fill=PENCIL, width=4)
    canvas.line([375, 505, 375, 530], fill=PENCIL, width=4)
    # crayon sun in the corner of the paper
    canvas.ellipse([428, 500, 456, 528], outline=(240, 170, 40), width=4)


def paint_robot_sheet(canvas):
    canvas.rectangle([250, 330, 470, 560], fill=SHEET,
                     outline=(200, 200, 190), width=3)
    # tape corners
    canvas.rectangle([250, 330, 292, 352], fill=(255, 235, 150))
    canvas.rectangle([428, 330, 470, 352], fill=(255, 235, 150))
    paint_crayon_robot(canvas)


def paint_grandpa(canvas):
    # head
    canvas.ellipse([640, 300, 780, 430], fill=SKIN_OLD)
    canvas.arc([640, 300, 780, 430], start=180, end=360, fill=SILVER, width=22)
    canvas.ellipse([668, 352, 700, 380], outline=PENCIL, width=3)
    canvas.ellipse([716, 352, 748, 380], outline=PENCIL, width=3)
    canvas.line([700, 366, 716, 366], fill=PENCIL, width=3)
    canvas.arc([680, 380, 740, 420], start=15, end=165, fill=PENCIL, width=4)
    # body: navy sweater
    canvas.rounded_rectangle([620, 430, 800, 700], radius=40, fill=CARDIGAN)
    canvas.rounded_rectangle([620, 700, 800, 830], radius=20, fill=DEEP_BLUE)
    # arm pointing at the drawing
    canvas.line([640, 480, 560, 420], fill=CARDIGAN, width=34)
    canvas.ellipse([540, 400, 580, 440], fill=SKIN_OLD)


def paint_girl(canvas):
    # pigtails + head
    canvas.ellipse([830, 520, 870, 560], fill=GIRL_HAIR)
    canvas.ellipse([930, 520, 970, 560], fill=GIRL_HAIR)
    canvas.ellipse([845, 500, 955, 610], fill=SKIN_YOUNG)
    canvas.ellipse([845, 500, 955, 545], fill=GIRL_HAIR)
    canvas.ellipse([868, 548, 886, 566], fill=PENCIL)
    canvas.ellipse([914, 548, 932, 566], fill=PENCIL)
    canvas.arc([880, 568, 920, 596], start=15, end=165, fill=PENCIL, width=4)
    # red dress
    canvas.polygon([(860, 610), (940, 610), (975, 760), (825, 760)], fill=FROCK)
    canvas.polygon([(860, 610), (940, 610), (940, 660), (860, 660)], fill=FROCK)
    # pointing arm
    canvas.line([860, 640, 700, 560], fill=FROCK, width=22)
    canvas.ellipse([684, 544, 716, 576], fill=SKIN_YOUNG)
    # legs + shoes
    canvas.line([875, 760, 875, 820], fill=SKIN_YOUNG, width=16)
    canvas.line([925, 760, 925, 820], fill=SKIN_YOUNG, width=16)
    canvas.ellipse([858, 812, 892, 836], fill=DEEP_BLUE)
    canvas.ellipse([908, 812, 942, 836], fill=DEEP_BLUE)


def caption_lines():
    return textwrap.wrap(ENTRY_TEXT, width=58)


def paint_caption(canvas):
    canvas.rectangle([0, 850, 1024, 1024], fill=DEEP_BLUE)
    face = load_font(30)
    y = 878
    for line in caption_lines():
        canvas.text((512, y), line, font=face, fill=SNOW, anchor="ma")
        y += 44


def build_scene():
    img = Image.new("RGB", (SIDE, SIDE), WALL)
    canvas = ImageDraw.Draw(img)
    paint_wall_dots(canvas)
    canvas.rectangle([0, 830, 1024, 850], fill=FLOORBOARD)
    canvas.rectangle([0, 850, 1024, 1024], fill=DEEP_BLUE)
    paint_fridge(canvas)
    paint_degree(canvas)
    paint_robot_sheet(canvas)
    paint_grandpa(canvas)
    paint_girl(canvas)
    paint_caption(canvas)
    return img


def main():
    build_scene().save(OUTPUT_PATH, "PNG")


if __name__ == "__main__":
    main()
