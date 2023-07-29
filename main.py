import subprocess
import sqlite3
conn=sqlite3.connect('ping.db')
cursor = conn.cursor()
cursor.execute('''SELECT IP FROM Switches''')
c = cursor.fetchmany(2)
print(c[0])
v=''+c[0]
print(v)
# Run a command in the command prompt
#The /c option tells cmd.exe to execute a single command and then exit. Without this option,
# cmd.exe would start an interactive command prompt session and wait for user input.


#################################without DB ###################################
# result = subprocess.run(['C:\Windows\System32\cmd.exe', '/c', 'ping 10.0.0.100'], stdout=subprocess.PIPE, text=True)
# if 'Lost = 4' in result.stdout:
#     print('error')
# else:
#     print('IPv4 address not found.')
# # Print the output of the command

################################# with DB ###################################
for res in c:
    print(c)
    # result = subprocess.run(['C:\Windows\System32\cmd.exe', '/c', f'ping {c}'], stdout=subprocess.PIPE, text=True)
    # if 'Lost = 4' in result.stdout:
    #     print('error')
    # else:
    #     print('IPv4 address not found.')

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()