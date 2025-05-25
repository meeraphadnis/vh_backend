from pdf2image import convert_from_path

images = convert_from_path("sample_aid.pdf")
for image in images:
    image.save("page_converted.png", "PNG")