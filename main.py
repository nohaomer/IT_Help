import subprocess
import sqlite3
import tkinter as tk
from tkinter import messagebox
conn=sqlite3.connect('ping.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM Switches')

# Fetch the result of the query
count = cursor.fetchone()[0]

# Print the number of rows
print(count)
co=1
ping=""
error=""
while co <= 4:

    cursor.execute(f'''SELECT IP FROM Switches WHERE ID={co}''')
    # convert tuple to srting must use fetchone
    c = cursor.fetchone()
    result = ', '.join(str(field) for field in c)
    # The /c option tells cmd.exe to execute a single command and then exit. Without this option,
    # cmd.exe would start an interactive command prompt session and wait for user input.
    output = subprocess.run(['C:\Windows\System32\cmd.exe', '/c', f'ping {result}'], stdout=subprocess.PIPE, text=True)

    if 'Lost = 4' in output.stdout:
        print(" not replay")
        ping=ping+result+" "
    else:
        print(" replay")
        error=error+result+" "

    co+=1
    # print(c[0])





# Create a root window
root = tk.Tk()
root.withdraw()

# Show a message box with an OK button
messagebox.showinfo("outputs", f"Pingable IPs are :   {ping}"+"\n" f"Error IPs are : {error}")

# Main loop
root.mainloop()

#################################without DB ###################################
# result = subprocess.run(['C:\Windows\System32\cmd.exe', '/c', 'ping 10.0.0.100'], stdout=subprocess.PIPE, text=True)
# if 'Lost = 4' in result.stdout:
#     print('error')
# else:
#     print('IPv4 address not found.')
# # Print the output of the command

################################# with DB ###################################

# output = subprocess.run(['C:\Windows\System32\cmd.exe', '/c', f'ping {result}'], stdout=subprocess.PIPE, text=True)
# if 'Lost = 4' in output.stdout:
#     print('error')
# else:
#     print('pingable')

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()