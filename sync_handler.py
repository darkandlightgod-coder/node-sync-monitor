import os, sys

def main():
    print("--- [System Initializing] ---")

    logic = os.getenv("CORE_LOGIC")
    if not logic:
        print("CRITICAL ERROR: Environment variable 'CORE_LOGIC' is empty.")
        sys.exit(1)
    
    print("Executing CORE_LOGIC...")
    try:

        exec(logic)
    except Exception as e:
        print(f"RUNTIME ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
