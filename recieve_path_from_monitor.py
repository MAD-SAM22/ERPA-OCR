import sys

def main():
    if len(sys.argv) > 1:
        src_path = sys.argv[1]
        print(f'Source path received: {src_path}')
        # Add your processing code here

if __name__ == "__main__":
    main()
