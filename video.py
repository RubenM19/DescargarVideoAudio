from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox

def accion():
    enlace = videos.get()
    if "youtube.com" not in enlace:
        status_label["text"] = "URL no válida"
    try:
        video = YouTube(enlace)
        nombre = video.streams[0].title
        descarga = video.streams.get_highest_resolution()
        descarga.download(filename=f"{nombre}_video.mp4")
        Messagebox.showinfo("Descarga exitosa", f"Se ha descargado el video '{nombre}_video.mp4'")
    except Exception as e:
        Messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def accion2():
    enlace=videos.get()
    if "youtube.com" not in enlace:
        status_label["text"] = "URL no válida"
    try:
        video = YouTube(enlace)
        nombre = video.streams[0].title
        descarga = video.streams.get_audio_only()
        descarga.download(filename=f"{nombre}_audio.mp3")
        Messagebox.showinfo("Descarga exitosa", f"Se ha descargado el video '{nombre}_audio.mp3'")
    except Exception as e:
        Messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

root = Tk()
root.config(bd=15)
root.title('Youtube Download')

menu_bar = Menu(root)

root.config(menu=menu_bar)

instruccion = Label(root, text='Insert Link to download')
instruccion.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton_video = Button(root, text='Download Video', command=accion)
boton_audio = Button(root, text='Download Audio', command=accion2)
boton_video.grid(row=2, column=1)
boton_audio.grid(row=3, column=1)
status_label = Label(menu_bar, text="")

root.mainloop()