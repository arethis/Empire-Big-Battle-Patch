A lightweight executable that modifies the hardcoded battle manager heap allocation in Empire: Total War, bypassing the original 32,768 entity limit to allow for massive, stable battles with over 50,000 troops.

**Features**
1. Automated Patching: Safely injects the 4 necessary hex modifications directly into Empire.exe.

2. Automatic Backups: Creates an Empire.exe.backup backup file before making any changes.

**Safety Checks:** 
Verifies existing bytes to prevent double-patching or corrupting incompatible game versions.

**Installation & Usage**

Download EmpirePatch.exe from the Releases tab.

Place the executable directly into your Empire: Total War root directory (the same folder that contains Empire.exe).

Double-click EmpirePatch.exe.

The command prompt will open, create a backup, apply the patches, and display a success message.

Launch the game.

To uninstall, delete the patched Empire.exe and rename Empire.exe.backup back to Empire.exe.
