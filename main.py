#!/usr/bin/env python3
"""
main.py - lightweight launcher for the Web_App_AT project.

Usage:
    python main.py streamlit  # runs "streamlit run ui_streamlit/app.py" (dev)
    python main.py tk         # runs the tkinter UI directly
    python main.py help       # prints this help
"""

import sys
import os
import subprocess

# Ensure project root is on path so "engine" package is importable
ROOT = os.path.abspath(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

def run_streamlit():
    """Run the Streamlit app using subprocess so logs appear in terminal."""
    streamlit_path = os.path.join(ROOT, "ui_streamlit", "app.py")
    if not os.path.exists(streamlit_path):
        print(f"ERROR: {streamlit_path} not found.")
        return 1

    # Use the same Python executable running this script to call streamlit
    cmd = [sys.executable, "-m", "streamlit", "run", streamlit_path]
    print("Launching Streamlit with:", " ".join(cmd))
    # This will block until Streamlit exits; logs printed to console
    return subprocess.call(cmd)

def run_tk():
    """Import and run the Tkinter app directly (useful for packaging as EXE)."""
    tk_path = os.path.join(ROOT, "ui_tkinter", "app.py")
    if not os.path.exists(tk_path):
        print(f"ERROR: {tk_path} not found.")
        return 1

    # Import the tkinter app as a module and run its main() if defined,
    # otherwise execute the file as a script.
    try:
        # Preferred: treat ui_tkinter as package and import app
        from ui_tkinter import app as tk_app_module
        # If module defines a main() function call it, else assume running import starts it.
        if hasattr(tk_app_module, "main"):
            return tk_app_module.main()
        else:
            # If app.py runs the UI on import, then importing above already executed it.
            return 0
    except Exception as e:
        # Fallback: run the file as script
        print("Import failed, falling back to executing file as script. Error:", e)
        return subprocess.call([sys.executable, tk_path])

def print_help():
    print(__doc__)

def main():
    if len(sys.argv) < 2:
        print("No command provided. Use 'help' to see usage.")
        print_help()
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd in ("help", "-h", "--help"):
        print_help()
        sys.exit(0)
    elif cmd == "streamlit":
        code = run_streamlit()
        sys.exit(code)
    elif cmd in ("tk", "tkinter"):
        code = run_tk()
        sys.exit(code)
    else:
        print(f"Unknown command: {cmd}")
        print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
