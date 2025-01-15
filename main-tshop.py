import os
import asyncio
import aiofiles
import aiohttp
from pystyle import Colors, Colorate
from concurrent.futures import ThreadPoolExecutor

purple = Colors.purple
red = Colors.red


async def log_found_file(file_path, log_file):
    """Log each found file asynchronously."""
    try:
        async with aiofiles.open(log_file, 'a') as f:
            await f.write(file_path + "\n")
        print(f"Found: {file_path}")
    except Exception as e:
        print(f"Error logging file {file_path}: {e}")


def find_files_thread(root_directory, extensions, log_file, loop, stats):
    """Find files in /moonloader/ and /cleo/ folders only."""
    included_dirs = {"moonloader", "cleo"}
    excluded_dirs = {"vscode", "System Cache", "System32"}

    for dirpath, _, filenames in os.walk(root_directory):
        if any(excluded in dirpath for excluded in excluded_dirs):
            continue
        if not any(included in dirpath for included in included_dirs):
            continue

        for filename in filenames:
            if filename.lower().endswith(extensions):
                full_path = os.path.join(dirpath, filename)
                asyncio.run_coroutine_threadsafe(log_found_file(full_path, log_file), loop)
                stats['count'] += 1  


async def find_files(root_directories, extensions, log_file):
    """Start the file search in multiple directories using threads."""
    loop = asyncio.get_event_loop()
    stats = {'count': 0}
    with ThreadPoolExecutor() as executor:
        tasks = [
            loop.run_in_executor(executor, find_files_thread, root_directory, extensions, log_file, loop, stats)
            for root_directory in root_directories
        ]
        await asyncio.gather(*tasks)

    return stats['count']


async def send_to_webhook(webhook_url, file_path):
    """Send the log file to the webhook."""
    try:
        async with aiohttp.ClientSession() as session:
            async with aiofiles.open(file_path, 'rb') as f:
                file_data = await f.read()

            data = aiohttp.FormData()
            data.add_field('file', file_data, filename=file_path, content_type='text/plain')

            async with session.post(webhook_url, data=data) as response:
                if response.status == 204:
                    print("File successfully sent to the webhook.")
                else:
                    print(f"Failed to send the file. Status code: {response.status}")
    except Exception as e:
        print(f"Error sending file to webhook: {e}")


async def main():
    root_directories = [f"{chr(i)}:\\" for i in range(ord('A'), ord('Z') + 1) if os.path.exists(f"{chr(i)}:\\")]

    ascii_art = '''
                           ██╗  ██╗ ██████╗ ████████╗ █████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
                           ██║ ██╔╝██╔═══██╗╚══██╔══╝██╔══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
                           █████╔╝ ██║   ██║   ██║   ███████║██║     ███████║█████╗  ██║     █████╔╝ 
                           ██╔═██╗ ██║   ██║   ██║   ██╔══██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
                           ██║  ██╗╚██████╔╝   ██║   ██║  ██║╚██████╗██║  ██║███████╗╚██████╗██║  ██╗ V2
                           ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
                              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                     Work hard in silence, let your success be your noise
                                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    '''
    os.system('cls' if os.name == "nt" else 'clear')
    print(Colorate.Vertical(Colors.red_to_purple, ascii_art, 2))
    webhook_url = input(f"{purple}Discord Webhook: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.red_to_purple, ascii_art, 2))
    print(f"{purple}1. .lua and .luac")
    print(f"{purple}2. .cs")
    print(f"{purple}3. All (.lua, .luac, .cs)")

    choice = input(f""" {purple}
┌──{red}(kotaro@T$HOP){purple} ~ [{red}Ϟ{purple}]
└─> """)
    os.system('cls' if os.name == 'nt' else 'clear')

    extensions_mapping = {
        '1': ('.lua', '.luac'),
        '2': ('.cs',),
        '3': ('.lua', '.luac', '.cs'),
    }

    extensions = extensions_mapping.get(choice)

    if not extensions:
        print("Invalid choice. Exiting.")
        return

    log_file = "TrollShop-Checker-Kotaro1337.txt"

    async with aiofiles.open(log_file, 'w') as f:
        await f.write('')

    found_count = await find_files(root_directories, extensions, log_file)

    async with aiofiles.open(log_file, 'a') as f:
        await f.write(f"\nScanning complete. Total files found: {found_count}\n")
    print(f"\nScanning complete. Total files found: {found_count}")

    await send_to_webhook(webhook_url, log_file)


if __name__ == "__main__":
    asyncio.run(main())
