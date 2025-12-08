"""
Lightweight JSX validation utilities
"""

def validate_jsx_stub(files_dict):
    """
    Perform basic validation on generated JSX files.

    Checks:
    - Files dict is properly formatted
    - Each file contains valid code structure
    - Export statements are present

    Args:
        files_dict: Dictionary of {filename: code_content}

    Returns:
        bool: True if validation passes
    """
    if not isinstance(files_dict, dict):
        return False

    if not files_dict:
        return False

    for name, content in files_dict.items():
        if not isinstance(content, str):
            return False

        if not content.strip():
            return False

        # Check for export statement (basic validation)
        if "export" not in content.lower():
            return False

    return True

def check_syntax(code):
    """
    Check JavaScript/JSX syntax (basic check).

    For production, integrate with:
    - eslint via subprocess
    - babel parser
    - custom AST validation

    Args:
        code: JavaScript/JSX code string

    Returns:
        tuple: (is_valid, error_message)
    """
    # Basic checks
    if not code.strip():
        return False, "Empty code"

    # Check for common syntax errors
    if code.count("{") != code.count("}"):
        return False, "Mismatched braces"

    if code.count("(") != code.count(")"):
        return False, "Mismatched parentheses"

    if code.count("[") != code.count("]"):
        return False, "Mismatched brackets"

    return True, ""
