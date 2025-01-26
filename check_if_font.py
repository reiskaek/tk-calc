import os
import shutil
import winreg
import ctypes
import sys
def prog():
    def is_font_installed(font_name):
        """Check if a font is installed by querying the Windows registry."""
        try:
            reg_key = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key) as key:
                num_values = winreg.QueryInfoKey(key)[1]
                for i in range(num_values):
                    name, value, _ = winreg.EnumValue(key, i)
                    if font_name.lower() in name.lower():
                        return True
        except FileNotFoundError:
            pass
        return False

    def install_font(font_name, font_file):
        """Install the font by copying it to the Fonts directory and updating the registry."""
        fonts_dir = r"C:\Windows\Fonts"
        destination = os.path.join(fonts_dir, font_file)

        # Copy the font file to the Fonts directory
        if not os.path.exists(destination):
            shutil.copy(font_file, destination)
        
        # Add the font to the registry
        reg_key = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key, access=winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, f"{font_name} (TrueType)", 0, winreg.REG_SZ, font_file)

    def main():
        font_name = "SF UI Text Heavy"  # Replace with the actual font name
        font_file = "SFUIText-Heavy.ttf"  # Replace with the actual font file name

        # Get the full path to the font file in the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(script_dir, font_file)
        
        # Check if the font is already installed
        if not is_font_installed(font_name):
            print(f"Font '{font_name}' not found. Installing...")
            install_font(font_name, font_path)
            print(f"Font '{font_name}' installed successfully.")
        else:
            print(f"Font '{font_name}' is already installed.")
        
        # Delete the font installer
        if os.path.exists(font_path):
            os.remove(font_path)
            print(f"Font installer '{font_file}' deleted.")

    # Ensure the script runs with administrator privileges
    if __name__ == "__main__":
        if ctypes.windll.shell32.IsUserAnAdmin():
            main()
        else:
            # Restart the script with admin privileges
            print("Requesting admin privileges...")
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
