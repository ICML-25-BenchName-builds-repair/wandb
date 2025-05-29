#!/usr/bin/env python3
"""
Reproduction script to test the pre-commit black-jupyter hook issue.
This script runs the specific hook that was failing and checks if it passes.
"""

import subprocess
import sys
import os

def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")
    return result

def main():
    """Main function to reproduce the issue."""
    repo_dir = "/lca-workspace/repos/wandb__wandb"
    
    print("=== Testing pre-commit black-jupyter hook ===")
    
    # Change to repo directory
    os.chdir(repo_dir)
    
    # Run the specific hook that was failing
    result = run_command("pre-commit run --hook-stage pre-push black-jupyter --all-files")
    
    if result.returncode == 0:
        print("\n✅ SUCCESS: black-jupyter hook passed!")
        return True
    else:
        print("\n❌ FAILURE: black-jupyter hook failed!")
        print("This indicates the formatting issue still exists.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)