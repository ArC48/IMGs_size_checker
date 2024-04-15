import customtkinter
from tkinter import filedialog
import os

##########################################
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry("500x450")
# root.eval('tk::PlaceWindow . center')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='Image Size Checker', font=('font1',20))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Folder Path", width=300, height=30)
entry.pack(pady=42, padx=10)


def check_images_sizes(counter_num=1000):
    # count files so we don't end up in an hour long loop
    path = entry.get()
    counter = counter_num
    files_count = 0
    # when the path is empty
    if len(path) == 0:
        print('---------------------------------------------------------')
        print('Enter a path or click Open!')
        print('---------------------------------------------------------')
        return

    # loop through files in the folder
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        # checking file types
        if os.path.isfile(file_path) and file_name.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
            file_size = os.path.getsize(file_path)
            # convert to kbs
            file_size_kb = file_size // 1024
            # Change what min size pictures you're looking for
            if file_size_kb >= 200:
                files_count += 1
                print(f"{file_name} ==> ({file_size_kb:.1f} kb)")

        counter -= 1
        if counter <= 0:
            print('Limit reached')
            return
    print('---------------------------------------------------------')
    print('Task Ended successfully! ', files_count, ' images Found!')
    print('---------------------------------------------------------')


def browse_folder():
    folder_path = filedialog.askdirectory()  # Open a folder selection dialog
    if folder_path:
        entry.delete(0, customtkinter.END)  # Clear the entry field
        entry.insert(0, folder_path)  # Set the selected folder path


button_browse = customtkinter.CTkButton(master=frame, text="Open", height=30, width=30,fg_color='green' , command=browse_folder)
button_browse.pack(pady=1, padx=40)

button = customtkinter.CTkButton(master=frame, text="Search", height=50, command=check_images_sizes)
button.pack(pady=52, padx=10)

root.mainloop()

