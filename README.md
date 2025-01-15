# **TrollShop SA-MP Cheats Scanner & Webhook Notifier**

TrollShop's Samp Cheats file scanning tool, designed to efficiently search for specific file types across your system and send the results directly to a Discord webhook. Built with high-performance multithreading and asynchronous operations, this tool is designed to minimize system load while performing extensive file searches.

---

## **Features:**
- 🔍 **Efficient File Scanning**: Scans directories for file types like `.lua`, `.luac`, `.asi`, and `.cs`.
- 📂 **Asynchronous Logging**: Logs found files asynchronously to avoid performance bottlenecks.
- 🌐 **Webhook Integration**: Automatically sends the log file to a Discord webhook once scanning is complete.
- ⚙️ **Multithreaded Performance**: Uses threading to ensure faster file discovery, even in large directory trees.
- 🖥️ **Excludes System Folders**: Automatically skips critical system directories like `System32` and `Program Files`.

---

## **Installation:**

To get started with the TrollShop Sa-mp Cheats Scanner, you'll need Python and a few dependencies:

1. **Clone the repository** or copy the script to your local machine.

2. **Install required dependencies**:

   ```bash
   pip install aiofiles aiohttp pystyle
   ```

---

## **Usage:**

Follow these steps to run the file scanner:

1. **Run the script using Python 3**:

   ```bash
   python3 main-tshop.py
   ```

2. **Input the Discord Webhook URL**: When prompted, provide your Discord webhook URL.

3. **Choose file types to scan**:

   The script provides you with four options for file scanning:
   - `1` → Scan for `.luac` files
   - `2` → Scan for `.cs` files
   - `3` → Scan for all file types (`.lua`, `.luac`,  `.cs`)

4. **Results & Logging**:
   - The results are saved to a log file named `TrollShop-Checker-Kotaro1337.txt`.
   - Once scanning is complete, the log file is automatically sent to the Discord webhook you provided.

---

## **Example Run:**
```bash
Discord Webhook: https://discord.com/api/webhooks/xxxxxxxxx
1. .luac
2. .cs
3. All (.lua, .luac, .cs)
Choose an option (1-3): 3
```
## SAMPLE LOGS:
```bash
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\moonloader\kotaro ddos samp.lua
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\moonloader\nds.luac
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\moonloader\neega slapper.lua
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\moonloader\sampballas.lua
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\cleo\roleplay_guns.cs
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\moonloader\patayka.lua
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\cleo\Switz_Hot.cs
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\moonlfoader\suntok-antiskid.luac
Found: C:\Users\Kotaro1337\Downloads\R.gta Modified\cleo\Use_any_car.cs
Scanning complete. Total files found: 9
File successfully sent to the webhook.
```

---

## **Customization:**

- **Excluding Directories**: The script is configured to exclude certain directories by default (e.g., `System32`, `Program Files`, `AppData`). You can customize the `excluded_dirs` variable in the code if you want to adjust which directories are skipped.
- **File Extensions**: You can modify or expand the extensions in the `extensions_mapping` dictionary to fit your specific needs.

---

## **System Requirements:**

- **Operating System**: Windows or Linux (ensure you have sufficient permissions to scan directories).
- **Python**: 3.6 or higher.
- **Permissions**: Administrator/root permissions may be required to scan certain directories.

---

## **Disclaimer:**

This tool is designed for legitimate use cases. Ensure you comply with all applicable laws and regulations when using this script.

---

## **Contributing:**

If you discover any bugs, or would like to request a feature or improvement, feel free to submit an issue or a pull request.

-                   Made with ❤️ by Kotaro1337.
[![Discord Presence](https://lanyard.cnrad.dev/api/871257848804442202)](https://discord.com/users/871257848804442202)
