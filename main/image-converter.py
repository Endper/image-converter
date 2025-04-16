import wx
from functions import *

app = wx.App()

# Create the base window and the element objects within arrays
frame = wx.Frame(None)
# text = []
# buttons = []

# Set the window properties
frame.SetBackgroundColour("#777777")
frame.SetMinSize((400, 600))
frame.SetSize((800, 600))
frame.SetMaxSize((1000, 600))
frame.SetTitle("Image Converter")

# Configure the window panel
class WindowPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        text = []
        buttons = []
        # Set the panel properties
        vertical_layout = wx.BoxSizer(wx.VERTICAL)

        # Initialize objects
        self.changeFontSize(30)
        text.append(wx.StaticText(self, label="Image Converter"))
        self.changeFontSize(10)
        text.append(wx.StaticText(self, label="version 100.0.0"))
        # Add a placeholder image
        empty_bitmap = wx.Bitmap(1, 1)
        dc = wx.MemoryDC(empty_bitmap)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        self.image_preview = wx.StaticBitmap(self, bitmap=empty_bitmap, size=(400, 200))
        # Continue with the rest of the initialization
        self.changeFontSize()
        buttons.append(wx.Button(self, label="Select Image"))
        self.image_page = wx.StaticText(self, label="[path/to/image]")
        text.append(wx.StaticText(self, label="Conversion Type"))
        self.conversion_options = wx.ComboBox(self, choices=[
            ".bmp", ".ico", ".jpeg", ".jpg", ".pdf",
            ".png", ".ppm", ".tif", ".tiff", ".webp", 
        ])
        buttons.append(wx.Button(self, label="Convert Image"))
        self.result_text = wx.StaticText(self, label="[result message]")

        # Change object properties
        for each_text in text:
            each_text.SetForegroundColour("#ffffff")
        self.image_page.SetForegroundColour("#ffffff")
        self.result_text.SetForegroundColour("#ffffff")

        for each_button in buttons:
            each_button.SetBackgroundColour("#333333")
            each_button.SetForegroundColour("#ffffff")
        
        self.conversion_options.SetSelection(0)
        self.conversion_options.SetBackgroundColour("#333333")
        self.conversion_options.SetForegroundColour("#ffffff")
        self.conversion_options.SetEditable(False)

        # Align objects
        vertical_layout.Add(text[0], flag=wx.ALIGN_CENTER)
        vertical_layout.Add(text[1], flag=wx.ALIGN_CENTER)
        vertical_layout.Add(self.image_preview, flag=wx.ALIGN_CENTER)
        vertical_layout.AddSpacer(30)
        vertical_layout.Add(buttons[0], flag=wx.ALIGN_CENTER)
        vertical_layout.Add(self.image_page , flag=wx.ALIGN_CENTER)
        vertical_layout.AddSpacer(30)
        vertical_layout.Add(text[2], flag=wx.ALIGN_CENTER)
        vertical_layout.Add(self.conversion_options, flag=wx.ALIGN_CENTER)
        vertical_layout.AddSpacer(30)
        vertical_layout.Add(buttons[1], flag=wx.ALIGN_CENTER)
        vertical_layout.Add(self.result_text, flag=wx.ALIGN_CENTER)

        # Key bindings
        self.Bind(wx.EVT_BUTTON, handler=self.select_image, source=buttons[0])
        self.Bind(wx.EVT_BUTTON, handler=self.convert_image, source=buttons[1])

        # Finish panel
        self.SetSizer(vertical_layout)

    # Changes the font size
    def changeFontSize(self, fontSize : int = 15):
        current_font = self.GetFont()
        current_font.SetPointSize(fontSize)
        self.SetFont(current_font)

    # Opens the file dialog, display the image, and it's path
    def select_image(self, event):
        image_path, image_file = open_image(event)
        if image_path != None:
            self.image_page.SetLabel(image_path)
            self.image_preview.size = image_file.GetSize()
            self.image_preview.SetBitmap(image_file)
            # Realign the text and image
            self.Layout()

    def convert_image(self, event):
        conversion_type = self.conversion_options.GetValue()
        result_message = convert_image_format(event, conversion_type)
        self.result_text.SetLabel(result_message)
        # Realign the text and image
        self.Layout()

# Finish the window
panel = WindowPanel(frame)
frame.Center()
frame.Show()

app.MainLoop()