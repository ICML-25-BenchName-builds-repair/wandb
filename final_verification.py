#!/usr/bin/env python3
"""
Final verification script to ensure our fix is complete and correct.
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

def check_file_content():
    """Check that the file contains the correct fix."""
    file_path = "/lca-workspace/repos/wandb__wandb/wandb/sdk/data_types/image.py"
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check that the fix is applied
    if 'format="png"' in content:
        print("✅ File contains the correct double quotes: format=\"png\"")
        correct_fix = True
    else:
        print("❌ File does not contain the expected double quotes")
        correct_fix = False
    
    # Check that the old single quotes are not present
    if "format='png'" in content:
        print("❌ File still contains single quotes: format='png'")
        correct_fix = False
    else:
        print("✅ File does not contain the old single quotes")
    
    return correct_fix

def main():
    """Main verification function."""
    print("=== Final Verification ===")
    
    repo_dir = "/lca-workspace/repos/wandb__wandb"
    os.chdir(repo_dir)
    
    success = True
    
    # Check file content
    print("\n1. Checking file content...")
    success &= check_file_content()
    
    # Test the specific hook that was failing
    print("\n2. Testing black-jupyter hook...")
    result = run_command("pre-commit run --hook-stage pre-push black-jupyter --all-files")
    if result.returncode == 0:
        print("✅ black-jupyter hook passed!")
    else:
        print("❌ black-jupyter hook failed!")
        success = False
    
    # Test ruff as well (another Python linter)
    print("\n3. Testing ruff hook...")
    result = run_command("pre-commit run --hook-stage pre-push ruff --all-files")
    if result.returncode == 0:
        print("✅ ruff hook passed!")
    else:
        print("❌ ruff hook failed!")
        success = False
    
    # Check git diff to see our changes
    print("\n4. Checking git diff...")
    result = run_command("git diff wandb/sdk/data_types/image.py")
    if "format='png'" in result.stdout and 'format="png"' in result.stdout:
        print("✅ Git diff shows the correct change from single to double quotes")
    else:
        print("❌ Git diff does not show the expected change")
        success = False
    
    if success:
        print("\n🎉 ALL VERIFICATIONS PASSED! The fix is complete and correct.")
    else:
        print("\n❌ Some verifications failed!")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)