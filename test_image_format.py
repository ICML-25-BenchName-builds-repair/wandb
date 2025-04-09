#!/usr/bin/env python
"""
Test script to verify the image format issue in wandb/sdk/data_types/image.py
"""

def test_image_format():
    """Test the format string in the image.py file."""
    with open('wandb/sdk/data_types/image.py', 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if 'savefig(buf, format=' in line:
                print(f"Line {i+1}: {line.strip()}")
                # Check if the line uses single quotes
                if "format='png'" in line:
                    print("Issue found: Using single quotes for 'png' string")
                    return True
                else:
                    print("No issue: Using double quotes for \"png\" string")
                    return False
    
    print("No matching line found")
    return False

if __name__ == "__main__":
    issue_found = test_image_format()
    if issue_found:
        print("Test failed: Issue detected")
        exit(1)
    else:
        print("Test passed: No issue detected")
        exit(0)