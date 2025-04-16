import wx
import os
from PIL import Image
import img2pdf
from pdf2image import convert_from_path


wildcard_options = (
    "Image files (*.bmp;*.ico;*.jpeg;*.jpg;*.pdf;*.png;*.ppm;*.tif;*.tiff;*.webp)|*.bmp;*.ico;*.jpeg;*.jpg;*.pdf;*.png;*.ppm;*.tif;*.tiff;*.webp|"
    "BMP files (*.bmp)|*.bmp|"
    "ICO files (*.ico)|*.ico|"
    "JPEG files (*.jpeg;*.jpg)|*.jpeg;*.jpg|"
    "PDF files (*.pdf)|*.pdf|"
    # "PGM files (*.pgm)|*.pgm|"
    "PNG files (*.png)|*.png|"
    "PPM files (*.ppm)|*.ppm|"
    "TIFF files (*.tif;*.tiff)|*.tif;*.tiff|"
    "WEBP files (*.webp)|*.webp"
)

SUPPORTED_EXTENSIONS = [
    ".bmp", ".ico", ".jpeg", ".jpg", ".pdf", 
    # ".pgm", 
    ".png", ".ppm", ".tif", ".tiff", ".webp"
]
SUPPORTED_EXTENSIONS_PILLOW = {
    ".bmp": "BMP",
    ".ico": "ICO",
    ".jpeg": "JPEG",
    ".jpg": "JPEG",
    ".pdf": "PDF",
    # ".pgm": "PGM",
    ".png": "PNG",
    ".ppm": "PPM",
    ".tif": "TIFF",
    ".tiff": "TIFF",
    ".webp": "WEBP"
}

image_file = None
image_path = None

def open_image(event):
    global image_file, image_path

    parent = event.GetEventObject().GetParent()

    with wx.FileDialog(parent, message="Choose an image file", 
                       wildcard=wildcard_options,
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:

        if file_dialog.ShowModal() == wx.ID_CANCEL:
            return None, None
    
        image_path = file_dialog.GetPath()

        image_file = wx.Image(image_path, wx.BITMAP_TYPE_ANY)

        image_width, image_height = image_file.GetSize()
        # Resize until it fits within the given window size
        while image_width > 400 and image_height > 200:
            image_file = image_file.Rescale(image_width // 2, image_height // 2)
            image_width, image_height = image_file.GetSize()
        
        image_file = wx.Bitmap(image_file)

        return image_path, image_file
def convert_image_format(event, extension_to_convert):
    # Check if a file has been stored
    if image_path == None:
        return "Error: No image selected/stored"
    image_extension = os.path.splitext(image_path)[1].lower()

    # Check if the file is supported
    if image_file == None and not image_extension in SUPPORTED_EXTENSIONS:
        return "Error: Image format not supported"
    
    # Check if the extension of the file and the desired are not the same
    if image_extension == extension_to_convert:
        return "Error: No extensions can be modified"

    # PDF to image
    if image_extension == ".pdf" and extension_to_convert in [".jpg", ".png", ".webp", ".tiff", ".bmp"]:
        images = convert_from_path(image_path)
        output_path = os.path.splitext(image_path)[0] + extension_to_convert
        format_name = SUPPORTED_EXTENSIONS_PILLOW[extension_to_convert]
        images[0].save(output_path, format=format_name)
        return "Image saved to: " + output_path

    # Image to PDF
    # !!!!! can not convert img2pdf from the image_path provided
    if extension_to_convert == ".pdf" and image_extension != ".pdf":
        new_image_path = image_path.replace(image_extension, ".pdf")
        with open(new_image_path, "wb") as file:
            file.write(img2pdf.convert(image_path))
        return "PDF saved to: " + new_image_path

    # Image to image
    with Image.open(image_path) as img:
        new_image_path = image_path.replace(image_extension, "")
        new_image_path += extension_to_convert
        img.save(new_image_path, format=SUPPORTED_EXTENSIONS_PILLOW[extension_to_convert])
        return "Image saved to: " + new_image_path
    
    return "Error: Conversion failed"