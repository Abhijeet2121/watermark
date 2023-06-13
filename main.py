from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter.font as tkfont
import tkinter.colorchooser as colorchooser

class ImageEditor:
    def __init__(self):
        self.image_path = ""
        self.text_entry = None
        self.font_size = 12
        self.font_style = None
        self.font_type = None 
        self.text_color = None
        self.text_position = None
        self.image_label = None

    def upload_image(self):
        file_type = [('PNG FILE', '*.png'), ('JPG FILE', '*.jpg')]
        self.image_path = filedialog.askopenfilename(filetypes=file_type)

        if self.image_path:
            image = Image.open(self.image_path)
            image = image.resize((500, 500))
            image = ImageTk.PhotoImage(image)

            
            self.image_label = Label(window) 
            self.image_label.grid(row=0, column=3, padx=20, pady=10, rowspan=10)
            self.image_label.image = image
            self.image_label.configure(image=image)
            self.image_label.image = image

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Text Color")
        self.text_color = color[1]

    def update_font_size(self, value):
        self.font_size = int(value)

    def add_text(self):
        if not self.image_path:
            print("Please upload an image first.")
            return

        text = self.text_entry.get()
        # font_size = int(self.font_size.get())
        font_style = self.font_style.get()
        font_type = self.font_type.get()
        text_position = self.text_position.get()

        font = ImageFont.truetype(font_type, self.font_size)

        if font_style == 'bold':
            font = ImageFont.truetype(font_type.replace('.ttf', '-Bold.ttf'), self.font_size)
        elif font_style == 'italic':
            font = ImageFont.truetype(font_type('.ttf', '-Italic.ttf'), self.font_size)

        image = Image.open(self.image_path)
        draw = ImageDraw.Draw(image)

        # Calculate the bounding box of the text

        text_bbox = draw.textbbox((0,0),text, font=font) 
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        if text_position == "Top_Left":
            position = (0, 0)
        elif text_position == "Top_Center":
            position = ((image.width - text_width)// 2 , 0)
        elif text_position == "Top_Right":
            position = (image.width - text_width, 0)
        elif text_position == "Center_Left":
            position = (0, (image.height - text_height)// 2)
        elif text_position == "Center":
            position = ((image.width - text_width)//2, (image.height - text_height)//2)
        elif text_position == "Center_Right":
            position = (image.width - text_width, (image.height - text_height)//2)
        elif text_position == "Bottom_Left":
            position = ( 0 , image.height - text_height)
        elif text_position == "Bottom_Center":
            position = ((image.width - text_width)// 2, image.height - text_height)
        elif text_position == "Bottom_Right":
            position = (image.width - text_width, image.height - text_height)

        draw.text(position, text, font=font, fill=self.text_color)

        image = image.resize((500, 500))
        image = ImageTk.PhotoImage(image)

        self.image_label = Label(window) 
        self.image_label.grid(row=0, column=3, padx=20, pady=10, rowspan=10)
        self.image_label.image = image
        self.image_label.configure(image=image)
        self.image_label.image = image

        # self.save_image(image)

    def save_image(self):
        if not self.image_path:
            print("Please Upload a image frist.")
            return

        image = Image.open(self.image_path)
        file_type = [('PNG FILE', '*.png'), ('JPG FILE', '*.jpg')]
        save_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=file_type)
        if save_path:
            image.save(save_path)

window = tk.Tk()
window.geometry("1400x900")
window.title("WaterMarker")
editor = ImageEditor()

upload_button_label = Label(window, text='Upload Image', width=20, anchor="w", padx=10, pady=10,).grid(row=0, column=0,sticky='w')
upload_button = Button(window, text='Upload Image', width=20, command=editor.upload_image)
upload_button.grid(row=0, column=1, padx=20, pady=10, sticky='w')

text_label = Label(window, text='Enter Text', width=20, anchor='w').grid(row=1, column=0, padx=20, pady=10, sticky='w')
editor.text_entry = Entry(window, width=20)
editor.text_entry.grid(row=1, column=1, padx=20, pady=10, sticky='w')

font_label = Label(window, text='Font Size', width=20, anchor='w').grid(row=2, column=0, padx=20, pady=10, sticky='w')
font_size_slider = Scale(window, from_=8, to=300, orient=HORIZONTAL,length=200, command=editor.update_font_size)
font_size_slider.set(editor.font_size)
font_size_slider.grid(row=2, column=1, padx=20, pady=10, sticky='w')

font_style_label = Label(window, text="Font Style", width=20, anchor='w').grid(row=3, column=0, padx=20, pady=10, sticky='w')
font_styles = ['normal', 'bold', 'italic', 'bold italic']
editor.font_style = tk.StringVar(window)
editor.font_style.set(font_styles[0])
font_style_dropdown = OptionMenu(window, editor.font_style, *font_styles)
font_style_dropdown.grid(row=3, column=1, padx=20, pady=10, sticky='w')

font_type_lable = Label(window, text="Font Type", width=20, anchor='w').grid(row=4, column=0, padx=20, pady=10, sticky='w')
font_types = tkfont.families()
editor.font_type = tk.StringVar(window)
editor.font_type.set(font_types[0])
font_types_dropdown = OptionMenu(window, editor.font_type, *font_types)
font_types_dropdown.grid(row=4, column=1, padx=20, pady=10, sticky='w')

change_color_label = Label(window, text='Text Color', width=20, anchor='w').grid(row=5, column=0, padx=20, pady=10, sticky='w')
color_button = Button(window, text='Color', width=20, command=editor.choose_color).grid(row=5, column=1, padx=20, pady=10, sticky='w')

text_pos = Label(window, text='Text Position', width=20, anchor='w').grid(row=6, column=1, padx=20, pady=10, sticky='w')
text_positions = ['Top_Left', 'Top_Center', 'Top_Right', 'Center_Left', 'Center', 'Center_Right',
                  'Bottom_Left', 'Bottom_Center', 'Bottom_Right']
editor.text_position = tk.StringVar(window)
text_pos_radio = [Radiobutton(window, text=position, variable=editor.text_position, value=position)
                  for position in text_positions]
for i , radio in enumerate(text_pos_radio):
    radio.grid(row= 7 + i //3 , column= i % 3, sticky='w', padx=20, pady=10)

text_button = Button(window, text="Add Text", width=20, command=editor.add_text)
text_button.grid(row=10, column=1, padx=20, pady=10, sticky='w')

save_image = Button(window, text="Save", width=20, command= editor.save_image)
save_image.grid(row=11, column=1, padx=20, pady=10, sticky='w')

window.mainloop()