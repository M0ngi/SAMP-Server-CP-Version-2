from tkinter import *
import ftplib, os

__version__ = '2'
__name__ = 'SA-MP Server CP'
__author__ = 'saidanemongi@gmail.com'
__credits__ = 'Mongi'
__date__ = '26-09-2017'

server = None

def credit():
    credit_root = Tk()
    credit_root.title('Credits')
    credit_root.minsize(700, 200)
    credit_root.maxsize(700, 200)
    credit_root.configure(background='white')
    f = Frame(credit_root, bg='white')
    f.grid()
    Label(f, text="\n\n\n\tThis application developed by Mongi\n\n\tVersion 1 Release Date: 13-08-2017\n\tVersion 2 Release Date: 28-09-2017\n\n\tYou have the right to use, edit, share the software/application as long as you don't remove the credits.", bg='white').grid()
    credit_root.mainloop()
    return 1

def help_():
    help_root = Tk()
    help_root.title('Credits')
    help_root.minsize(450, 200)
    help_root.maxsize(450, 200)
    help_root.configure(background='white')
    f = Frame(help_root, bg='white')
    f.grid()
    Label(f, text="\n\n\n\tThe application will require the FTP Details (User, Password, IP)\n\tMake sure the FTP Path starts in '/scriptfiles/CPfolder'\n\tYou have to install the .pwn file in your server to work.", bg="white").grid()
    help_root.mainloop()
    return 1

def changelog():
    changelog_root = Tk()
    changelog_root.title('Change Log')
    changelog_root.minsize(800, 200)
    changelog_root.maxsize(800, 200)
    changelog_root.configure(background='white')
    f = Frame(changelog_root, bg='white')
    f.grid()
    Label(f, text="\n\n\n\tEdited the application path in FTP to secure the server files (Database, Scripts...). It's safe to share the application with staff team now.\n\tAdded the ability to check the chat log, It will show the player messages and their IDs.\n\tSome edit in the GUI For the Control Panel.", bg='white').grid()
    changelog_root.mainloop()
    return 1

def warning(text):
    warn_root = Tk()
    warn_root.title('Warning!')
    warn_root.minsize(300, 200)
    warn_root.maxsize(300, 200)
    warn_root.configure(background='white')
    f = Frame(warn_root, bg='white')
    f.grid()
    Label(f, text='\n\n\n\tError: '+str(text)+'.', bg='white').grid()
    warn_root.mainloop()
    return 1

def ban(event, playername):
    f = open("ControlPanel.cfg", "w")
    f.write("BanPlayer="+str(playername))
    f.close()
    server.storbinary('STOR ControlPanel.cfg', open('ControlPanel.cfg', 'rb'))
    os.system('del '+str(os.getcwd())+'\ControlPanel.cfg')
    return 1;

def kick(event, playername):
    f = open("ControlPanel.cfg", "w")
    f.write("KickPlayer="+str(playername))
    f.close()
    server.storbinary('STOR ControlPanel.cfg', open('ControlPanel.cfg', 'rb'))
    os.system('del '+str(os.getcwd())+'\ControlPanel.cfg')
    return 1

def BanKick(event):
    ban_root = Tk()
    ban_root.title('Manage Players')
    ban_root.minsize(400, 200)
    ban_root.maxsize(400, 200)
    ban_root.configure(background='white')
    ff = Frame(ban_root, bg='white')
    ff.grid()
    
    #Ban
    Label(ff, text='\n\n', bg='white').grid(column=0, row=1)

    f = Frame(ban_root, bg='white')
    f.grid()
    
    Label(f, text='   Player Name: ', font='Calibri 12 bold', bg='white').grid(column=0, row=1)
    
    Label(f, text='   ', bg='white').grid(column=1, row=1)
    
    ban_entry_playername = Entry(f, bg='white', width=25)
    ban_entry_playername.grid(column=2, row=1)
    
    Label(f, text='   ', bg='white').grid(column=3, row=1)
    
    ban_button = Button(f, text='Ban Player ', bg='white')
    ban_button.bind('<Button-1>', lambda event: ban(event, ban_entry_playername.get()))
    ban_button.grid(column=4, row=1)
    
    #Kick
    Label(f, text='\n', bg='white').grid(column=0, row=2)

    Label(f, text='   Player Name: ', font='Calibri 12 bold', bg='white').grid(column=0, row=2)
    
    Label(f, text='   ', bg='white').grid(column=1, row=2)
    
    kick_entry_playername = Entry(f, bg='white', width=25)
    kick_entry_playername.grid(column=2, row=2)
    
    Label(f, text='   ', bg='white').grid(column=3, row=2)
    
    kick_button = Button(f, text='Kick Player', bg='white')
    kick_button.bind('<Button-1>', lambda event: kick(event, kick_entry_playername.get()))
    kick_button.grid(column=4, row=2)
    
    ban_root.mainloop()

def GetChat():
    f = open('ChatLog.txt', 'wb')
    server.retrbinary('RETR ChatLog.txt', f.write)
    f.close()
    f = open("ChatLog.txt", "r")
    msgs = f.read().split("\n")
    f.close()
    return msgs

def Chat(event):
    Chat_Root = Tk()
    Chat_Root.title('Server Chat')
    Chat_Root.minsize(750, 500)
    Chat_Root.maxsize(750, 500)
    Chat_Root.configure(background='white')
    ff = Frame(Chat_Root, bg='white')
    ff.grid()
    
    Label(ff, text='\n', bg='white').grid(column=0, row=1)

    Label(ff, text='Last 500 lines from the chat log:', bg='white').grid(column=0, row=2)
    
    listbox = Listbox(Chat_Root, width=123, height=25)
    listbox.grid()

    for s in GetChat(): #For line in lines
        s = s[:128]
        if len(s) > 100:
            t1 = ''
            t2 = ''
            c = 0
            for x in s:
                if c < 100:
                    t1 += str(x)
                else:
                    t2 += str(x)
                c += 1
            del c
            listbox.insert(0, str(t1))
            listbox.insert(1, "..."+str(t2))
        else:
            s = str(s)
            listbox.insert(0, s)

    Chat_Root.mainloop()
    return 1

def CP_dialog():
    CP_root = Tk()
    CP_root.title('Server Control Panel')
    CP_root.minsize(400, 200)
    CP_root.maxsize(400, 200)
    CP_root.configure(background='white')
    ff = Frame(CP_root, bg='white')
    ff.pack()

    Label(ff, text='\n\n', bg='white').pack()

    f = Frame(CP_root, bg='white')
    f.pack()

    b1 = Button(f, text='Manage Players', bg='white')
    b1.bind('<Button-1>', BanKick)
    b1.pack()
    
    Label(f, text='', bg='white', height=1).pack()
    
    b2 = Button(f, text='View Chat', bg='white', width=12)
    b2.bind('<Button-1>', Chat)
    b2.pack()

    CP_root.mainloop()
    return 1

def connect(event):
    global server
    ip = input_entry_ip.get().replace('\n', '')
    user = input_entry_user.get().replace('\n', '')
    password = input_entry_pass.get().replace('\n', '')
    server = ftplib.FTP()
    server.connect(ip, 21)
    try:
        server.login(user,password)
    except ftplib.error_perm:
        warning("Wrong FTP User or Password")
        root.destroy()
        return 0
    except Exception as e:
        warning("Unexpected Error: "+str(e))
        root.destroy()
        return 0
    root.destroy()

    CP_dialog()
    
    return 1

root = Tk()
root.title('Server CP')
root.maxsize(380, 500)
root.minsize(380, 500)
root.configure(background='white')

#=====================================
menubar = Menu(root)
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label='Help', command=help_)
filemenu.add_separator()
filemenu.add_command(label='Change Log', command=changelog)
filemenu.add_separator()
filemenu.add_command(label='Credits', command=credit)
    
menubar.add_cascade(label='?', menu=filemenu)

# display the menu
root.config(menu=menubar)

#===================================

ff = Frame(root, bg='white')
ff.pack()

Label(ff, text='\n\n', bg='white').grid(column=0, row=1)
Label(ff, text="Make sure that the FTP Path starts in '/scriptfiles/CPFolder'\n", bg='white').grid(row=2)

f = Frame(root, bg='white')
f.pack()

Label(f, text='FTP Host: ', font='Calibri 12 bold', bg='white').grid(column=0, row=4)
input_entry_ip = Entry(f, bg='white', width=25)
input_entry_ip.grid(column=1, row=4)

Label(f, text='', bg='white').grid(column=0, row=5)

Label(f, text='User Name: ', font='Calibri 12 bold', bg='white').grid(column=0, row=6)
input_entry_user = Entry(f, bg='white', width=25)
input_entry_user.grid(column=1, row=6)

Label(f, text='', bg='white').grid(column=0, row=7)

Label(f, text='Password: ', font='Calibri 12 bold', bg='white').grid(column=0, row=8)
input_entry_pass = Entry(f, bg='white', width=25)
input_entry_pass.grid(column=1, row=8)

new_frame = Frame(root, bg='white')
new_frame.pack()

Label(new_frame, text='\n\n', bg='white').grid()

connect_b = Button(new_frame, text='Connect', bg='white')
connect_b.bind('<Button-1>', connect)
connect_b.grid()

root.mainloop()
