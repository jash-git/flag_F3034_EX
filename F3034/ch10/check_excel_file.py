import os

def check_excel_file(file_path):
    """
    檢查.xlsx檔案是否存在

    Args:
        file_path (str): 檔案路徑

    Returns:
        bool: 檔案是否存在
    """
    if os.path.isfile(file_path) and file_path.endswith('.xlsx'):
        return True
    else:
        return False
