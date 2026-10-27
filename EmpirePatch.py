
""" Copyright (c) 2026 Arethis

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the “Software”),
 to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE."""

import sys
import os
import shutil

PATCHES = {
    0x00CE0D91: b"\x68\x00\x00\x04\x00",  
    0x00CE0DC3: b"\x81\xFF\x00\x00\x04\x00",
    0x00CE0DD8: b"\xB8\x00\x00\x04\x00",
    0x00CE0E17: b"\x05\x00\x00\xB0\x00",   
}

def apply_patches(filename="Empire.exe"):
    if not os.path.exists(filename):
        print(f"[-] Error: {filename} not found in current directory.")
        input("Press Enter to exit...")
        return

    backup_name = filename + ".backup"
    if not os.path.exists(backup_name):
        print("[+] Creating backup of original executable...")
        shutil.copyfile(filename, backup_name)
    else:
        print("[*] Backup already exists. Skipping backup creation.")

    print(f"[+] Verifying and patching {filename}...")
    
    try:
        with open(filename, "r+b") as f:
            for offset, patch_bytes in PATCHES.items():
                f.seek(offset)
                original_bytes = f.read(len(patch_bytes))
                
                if original_bytes == patch_bytes:
                    print(f"[*] Offset 0x{offset:08X} is already patched. Skipping.")
                    continue
                
                f.seek(offset)
                f.write(patch_bytes)
                print(f"[+] Patched offset 0x{offset:08X} successfully.")
                
        print("\n[SUCCESS] All patches applied! You can now launch massive battles.")
    except Exception as e:
        print(f"[-] Critical Error applying patches: {e}")
        
    input("Press Enter to exit...")

if __name__ == "__main__":
    apply_patches()