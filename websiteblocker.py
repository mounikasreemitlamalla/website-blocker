import datetime
import time
import os

# List of websites to block
site_block = []
n = int(input("Enter the number of websites you want to block: "))
for i in range(n):
    s = input()
    site_block.append(s)

host_path = "C:/Windows/System32/drivers/etc/hosts"  # Update if necessary
redirect = "127.0.0.1"

# Flag to check if blocking is active
is_blocking_active = True

# Calculate end time (5 minutes from now)
end_time = datetime.datetime.now() + datetime.timedelta(minutes=5)

def block_websites():
    with open(host_path, "r+") as host_file:
        content = host_file.read()
        for website in site_block:
            if website not in content:
                host_file.write(redirect + " " + website + "\n")

def unblock_websites():
    with open(host_path, "r+") as host_file:
        content = host_file.readlines()
        host_file.seek(0)
        for line in content:
            if not any(website in line for website in site_block):
                host_file.write(line)
        host_file.truncate()

while True:
    # Check if the current time is less than the end time
    if datetime.datetime.now() < end_time:
        # Check if blocking is active
        if is_blocking_active:
            print("Websites are blocked")
            block_websites()
        else:
            print("Blocking is paused, websites are unblocked")
            unblock_websites()
    else:
        print("End time reached, websites are unblocked")
        unblock_websites()
        break

    # User input to control the blocking
    user_input = input("Enter 'pause' to pause blocking, 'resume' to start blocking again: ").lower()
    
    if user_input == "pause":
        is_blocking_active = False
        print("Blocking is paused.")
    elif user_input == "resume":
        is_blocking_active = True
        print("Blocking resumed.")

    time.sleep(5)  # Adjust the loop interval if needed

