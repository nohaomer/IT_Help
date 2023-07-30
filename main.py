import subprocess
import sqlite3
conn=sqlite3.connect('ping.db')
cursor = conn.cursor()

cursor.execute('''SELECT IP FROM Switches WHERE ''')
c = cursor.fetchone()
# print(c[0])

result = ', '.join(str(field) for field in c)
print(result)
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

output = subprocess.run(['C:\Windows\System32\cmd.exe', '/c', f'ping {result}'], stdout=subprocess.PIPE, text=True)
if 'Lost = 4' in output.stdout:
    print('error')
else:
    print('pingable')

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()