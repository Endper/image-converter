# Image Converter v100.1.0

A simple image conversion tool made by Endper in Python.

---

NOTE: This project uses the {EPOCH * 100 + MAJOR}.MINOR.PATCH version naming method.

Made to have transparency, offline usage, and be simple in both code and look.

---

# Changelog

## Version 100.1.0

Patches and small tweaks featuring:
- Grammar fixes within the README file.
- Added/Removed comments in the `functions.py` and `image-converter.py` file.
- Resizing of images has been slightly reworked - fixing an image preview size bug.
- Changed the title of the window.
- When hovering over the buttons or the drop down menu, the cursor and background colo (only for the buttons) change.
- Buttons now get added to an object with the self attribute.
- PDF to Image support has been cancelled. This project is aimed to be simple in not only looks but code. Poppler will make the project more complicated for modification.

---

## Version 100.0.0

Includes the base application supporting Bitmaps (.bmp), Window Icons (.ico), Joint Photographic Experts Group (.jpeg, .jpg), Portable Document Format (.pdf), Portable Graymap Format (.pgm) (CURRENT NOT WORKING), Portable Network Graphics (.png), Portable Pixmap Format (.ppm), Tagged Image File Format (.tif, .tiff), and Web Picture Format (.webp) files.

Holds a basic interface.

Things such as more support for different files, better application style, and more features such as image resizing, may be added in the future.

---

# Requirements

If you want to modify the program or run it through Python, you'll need 4 libraries installed: wxPython for the GUI, Pillow for the image processing, img2pdf and pdf2image for handling PDF files.

Install it through `pip install wxPython pillow img2pdf pdf2image`. The program also uses the built-in library `os`.

---

# Pull requests, issues, and modifications

Any pull requests, issues, and/or modifications are welcome. During pull requests, if it improves the program, it'll be accepted. For issues, as long as they're reasonable, it's very likely to be resolved through a fix of some sort. For modifications such as forks or whatnot, as long as visible credit is done to the author of this program.

---

# License

This program is licensed under the [GNU GENERAL PUBLIC LICENSE V3](LICENSE).