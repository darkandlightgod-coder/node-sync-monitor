import os
import sys

# 從 GitHub Actions 的環境變數中提取 Secret 內容
logic = os.getenv("CORE_LOGIC")

print("--- [System Initializing] ---")
if not logic:
    print("CRITICAL ERROR: Environment variable 'CORE_LOGIC' is empty.")
    print("Please check GitHub Secrets configuration.")
    sys.exit(1)

try:
    print("Executing CORE_LOGIC...")
    # 執行 Secret 裡面的所有代碼
    exec(logic)
    print("--- [Execution Complete] ---")
except Exception as e:
    print(f"RUNTIME ERROR in CORE_LOGIC: {e}")
    sys.exit(1)
