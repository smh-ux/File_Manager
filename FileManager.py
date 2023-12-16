#import libraries
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil

# create main window
window = Tk()
window.title("File Manager")
window.geometry("600x400")

# function for file select
def select_file():
	# file's path
	global file_path
	
	# open file select window
	file_path = filedialog.askopenfilename()

	# input file name
	file_name = os.path.basename(file_path)

	# write the file name in the label
	file_label.config(text = file_name)

# function for delete file
def delete_file():
	# file's path
	global file_path
	
	# if any file selected
	if file_path:
		# deletion confirmation
		answer = messagebox.askyesno("Deletion Confirmation", "Do you want to delete this file?")

		# if answer is true
		if answer:
			# then delete the file
			os.remove(file_path)
			# update label
			file_label.config(text="File not Selected")
			# format file path
			file_path = None
			# information message
			messagebox.showinfo("Bilgi", "File deleted")
	# if any file not selected	
	else:
		# show error message
		messagebox.showerror("Error", "Please select a file")

# function for copy file	
def copy_file():
	# file's path
	global file_path

	# if any file selected
	if file_path:
		# select the target directory
		target_path = filedialog.askdirectory()
		# if target directory selected
		if target_path:
			# copy the file
			shutil.copy(file_path, target_path)
			# information message
			messagebox.showinfo("Information", "File Copied")
	# if any file not selected
	else:
		# error message
		messagebox.showerror("Error", "Please select a file")				

# function for move file
def move_file():
	# file's path
	global file_path

	#if any file selected
	if file_path:
		# select the target directory
		target_path = filedialog.askdirectory()
		# if target directory selected
		if target_path:
			# move the file
			shutil.move(file_path, target_path)
			# update the label
			file_label.config(text="File not selected")
			# format file path
			file_path = None
			# information message
			messagebox.showinfo("Information", "File Moved")
	# if any file not selected
	else: 
		# error message
		messagebox.showerror("Error", "Please select a file")

def rename_file():
	# file's path
	global file_path
	
	# if any file selected
	if file_path:
		# input rename
		new_name = filedialog.asksaveasfilename()
		# if new name selected
		if new_name:
			# rename the file
			os.rename(file_path, new_name)
			# assign the new file name
			file_name = os.path.basename(new_name)
			# update the label
			file_label.config(text=file_name)
			# update file path
			file_path = new_name
			messagebox.showinfo("Information", "File renamed")
	# if any file not selected
	else:
		# error message
		messagebox.showerror("Error", "Please select a file")
			
			

# create label
file_label = Label(window, text="File not Selected", font=("Arial", 16))
file_label.pack(pady=20)

# create buttons 
select_button = Button(window, text="Select File", command=select_file)
select_button.pack(pady=10) 
	
delete_button = Button(window, text="Delete File", command=delete_file)
delete_button.pack(pady=10)

copy_button = Button(window, text="Copy File", command=copy_file)
copy_button.pack(pady=10)

move_button = Button(window, text="Move File", command=move_file)
move_button.pack(pady=10)

rename_button = Button(window, text="Rename File", command=rename_file)
rename_button.pack(pady=10)
	
# window still open until we want to close it
mainloop()