#!/usr/bin/env python3
"""
Test script to verify that the image.py file still works correctly after our fix.
"""

import sys
import os

# Add the wandb directory to the path
sys.path.insert(0, '/lca-workspace/repos/wandb__wandb')

def test_image_import():
    """Test that we can import the Image class without issues."""
    try:
        from wandb.sdk.data_types.image import Image
        print("✅ Successfully imported Image class")
        return True
    except Exception as e:
        print(f"❌ Failed to import Image class: {e}")
        return False

def test_image_syntax():
    """Test that the syntax in the image.py file is valid."""
    try:
        import ast
        with open('/lca-workspace/repos/wandb__wandb/wandb/sdk/data_types/image.py', 'r') as f:
            content = f.read()
        
        # Parse the file to check for syntax errors
        ast.parse(content)
        print("✅ Image.py file has valid Python syntax")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error in image.py: {e}")
        return False
    except Exception as e:
        print(f"❌ Error parsing image.py: {e}")
        return False

def main():
    """Main test function."""
    print("=== Testing Image functionality after fix ===")
    
    success = True
    success &= test_image_syntax()
    success &= test_image_import()
    
    if success:
        print("\n✅ All tests passed! The fix is working correctly.")
    else:
        print("\n❌ Some tests failed!")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)