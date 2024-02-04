import subprocess

def run_rclone_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    rclone_move_copy = input("rclone move or rclone copy: ").lower()

    if rclone_move_copy not in ['move', 'copy']:
        print("Invalid choice. Please enter 'move' or 'copy'.")
    else:
        source_path = input("Enter source path: ")
        destination_path = input("Enter destination path: ")

        rclone_command = ['rclone', rclone_move_copy, source_path, destination_path]

        output = run_rclone_command(rclone_command)

        if output:
            print("Rclone command executed successfully.")
            print("Output:")
            print(output)