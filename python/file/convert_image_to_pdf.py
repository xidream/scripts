import sys
from textwrap import dedent

from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def convert_image_to_pdf(input_path, output_path, page_size):
    image = Image.open(input_path)
    image_width, image_height = image.size

    page_width, page_height = page_size

    scale_factor = min(page_width / image_width, page_height / image_height)

    new_width = image_width * scale_factor
    new_height = image_height * scale_factor

    x_position = (page_width - new_width) / 2
    y_position = (page_height - new_height) / 2

    if image.mode == "RGBA":
        image = image.convert("RGB")

    pdf_canvas = canvas.Canvas(output_path, pagesize=page_size)
    pdf_canvas.drawImage(input_path, x_position, y_position, new_width, new_height)
    pdf_canvas.save()
    print(f"Conversion completed: {output_path}")


def get_page_size(size_name: str):
    return {
        "A4": A4,
    }.get(size_name.upper(), A4)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            dedent(
                """\
                Usage: python3 convert_image_to_pdf.py <input_image_path> <output_pdf_path> <page_size>
                - <page_size>: A4
                """
            )
        )
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_pdf_path = sys.argv[2]
    page_size_name = sys.argv[3]

    page_size = get_page_size(page_size_name)

    convert_image_to_pdf(input_image_path, output_pdf_path, page_size)
