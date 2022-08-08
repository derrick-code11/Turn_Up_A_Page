import os
from tkinter import *
from PIL import ImageTk, Image

image_files = [element for element in os.listdir('../Turn_Up_A_Page') if
               element.endswith('.png') and element != 'pic.png']

text_files = [element for element in os.listdir('../Turn_Up_A_Page') if element.endswith('.txt')]

colors = ['#72faf1', 'ghost white', '#72fa9d', 'ghost white', '#d07ac8',
          'hot pink', 'ghost white', 'yellow',
          'ghost white', 'tomato']


class App(Tk):
    def __init__(self):
        super().__init__()

        self.homepage_button = None
        self.previous_button = None
        self.flashcard_label = None
        self.flashcard_window = None
        self.story_window = None
        self.new_window = None
        self.next_button = None

        self.image_number = IntVar()
        self.image_list = [ImageTk.PhotoImage(Image.open(image).resize((800, 500))) for image in image_files]

        self.geometry('600x720')
        self.title('TURN UP A PAGE')
        self.resizable(False, False)
        self.app_image = ImageTk.PhotoImage(Image.open('pic.png').resize((400, 400)))

        self.my_label = Label(self, image=self.app_image)
        self.my_label.grid(row=0, column=0, columnspan=4, padx=100, pady=30)

        self.home_button1 = Button(self, text='EXPLORE AVAILABLE SHORT STORIES ', width=37, height=3, font='arial',
                                   relief=GROOVE,
                                   bg='#72fa9d', command=self.stories_section)
        self.home_button1.grid(row=1, column=0, columnspan=4, padx=15, pady=5)

        self.home_button2 = Button(self, text='EXPLORE AVAILABLE FLASHCARDS', width=37, height=3, font='arial',
                                   relief=GROOVE,
                                   bg='#a193a0', command=self.flashcards_section)
        self.home_button2.grid(row=2, column=0, columnspan=4, padx=15, pady=20)

    def stories_section(self):
        self.new_window = Toplevel(self)
        self.new_window.geometry('880x570')
        self.new_window.title("SHORT STORIES")
        self.new_window.resizable(False, False)

        for num, file in enumerate(text_files):
            if num < 5:
                story_button = Button(self.new_window, text=text_files[num].replace('.txt', ''), width=30, height=2,
                                      font='Tahoma', relief=GROOVE,
                                      bg=colors[num], command=lambda m=num: self.get_story(text_files[m]))
                story_button.grid(row=num, column=0, columnspan=3, padx=40, pady=20)
            elif num >= 5:
                story_button = Button(self.new_window, text=text_files[num].replace('.txt', ''), width=30, height=2,
                                      font='Tahoma', relief=GROOVE,
                                      bg=colors[num], command=lambda m=num: self.get_story(text_files[m]))
                story_button.grid(row=num - 5, column=4, columnspan=3, padx=40, pady=20)

    def get_story(self, file_name):
        self.story_window = Toplevel(self)
        story = Text(self.story_window, wrap=WORD, width=100, height=30, spacing1=5, relief=GROOVE, bg='ghost white',
                     font=('Tahoma', 12), padx=30, pady=30)
        story.grid(row=0, column=0, columnspan=4, padx=100, pady=5)

        with open(file_name, 'r', encoding='utf-8') as filename:
            story.insert(INSERT, filename.read())
            story['state'] = DISABLED

    def flashcards_section(self):
        self.flashcard_window = Toplevel(self)
        self.flashcard_window.geometry('1000x700')
        self.flashcard_window.title('FLASHCARDS')
        self.flashcard_label = Label(
            self.flashcard_window, image=self.image_list[0])
        self.previous_button = Button(
            self.flashcard_window, text="PREV", font="Tahoma", bg="#00a8a8",
            width=8, height=2, state=DISABLED, command=self.back)
        self.homepage_button = Button(
            self.flashcard_window, text="GO TO HOMEPAGE", font="Tahoma",
            bg="ghost white", width=50, height=2,
            command=self.flashcard_window.destroy)
        self.next_button = Button(
            self.flashcard_window, text="NEXT", font="Tahoma", bg="#00a8a8",
            width=8, height=2, command=self.forward)
        self.flashcard_label.grid(
            row=0, column=0, columnspan=4, padx=100, pady=50)
        self.previous_button.grid(row=1, column=0)
        self.homepage_button.grid(row=1, column=1, columnspan=2)
        self.next_button.grid(row=1, column=3)

    def forward(self):
        try:
            self.image_number.set(self.image_number.get() + 1)
            img_num = self.image_number.get()
            if img_num >= 0:
                self.previous_button.config(state=NORMAL)
            self.next_button.config(state=NORMAL)
            if img_num >= len(self.image_list) - 1:
                self.next_button.config(state=DISABLED)
                self.update()
            self.flashcard_label.config(image=self.image_list[img_num])
        except IndexError:
            pass

    def back(self):
        try:
            self.image_number.set(self.image_number.get() - 1)
            img_num = self.image_number.get()
            self.next_button.config(state=NORMAL)
            if img_num <= 0:
                self.previous_button.config(state=DISABLED)
                self.update()
            self.flashcard_label.config(image=self.image_list[img_num])
        except IndexError:
            pass


app = App()
app.mainloop()
