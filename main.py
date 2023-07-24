import subprocess

# Run a command in the command prompt
#The /c option tells cmd.exe to execute a single command and then exit. Without this option,
# cmd.exe would start an interactive command prompt session and wait for user input.
result = subprocess.run(['C:\Windows\System32\cmd.exe', '/c', 'ping 10.0.0.100'], stdout=subprocess.PIPE, text=True)
if 'Lost = 4' in result.stdout:
    print('error')
else:
    print('IPv4 address not found.')
# Print the output of the command

