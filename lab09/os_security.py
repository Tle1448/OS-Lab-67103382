import os
import stat


def check_file_permissions(filename):
    print(f"--- OS File Permission Check: {filename} ---")

    file_stats = os.stat(filename)

    permissions = stat.filemode(file_stats.st_mode)

    print(f"Current Permissions: {permissions}")

    if os.access(filename, os.R_OK):
        print("Read Permission: YES")
    else:
        print("Read Permission: NO")

    if os.access(filename, os.W_OK):
        print("Write Permission: YES")
    else:
        print("Write Permission: NO")

    if os.access(filename, os.X_OK):
        print("Execute Permission: YES")
    else:
        print("Execute Permission: NO")


def main():
    test_file = "secure_data.txt"

    with open(test_file, "w") as f:
        f.write("Sensitive AI dataset information.")

    check_file_permissions(test_file)


if __name__ == "__main__":
    main()