import os
import subprocess
import time
import argparse

def main(output):
  
    directory = './recorded'
 
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ts'):
                input_file = os.path.join(root, file)

                
                relative_path = os.path.relpath(input_file, directory)

             
                output_file = os.path.join(output, f'{os.path.splitext(relative_path)[0]}.mp4')

                
                os.makedirs(os.path.dirname(output_file), exist_ok=True)

               
                if not os.path.exists(output_file) or os.path.getmtime(input_file) > os.path.getmtime(output_file):

                  
                    initial_size = os.path.getsize(input_file)
                    time.sleep(5) 
                    final_size = os.path.getsize(input_file)

                    if final_size == initial_size:
                        
                        command = [
                            'ffmpeg',
                            '-i', input_file,
                            '-c:v', 'copy',
                            '-c:a', 'copy',
                            '-f', 'mp4',
                            output_file
                        ]
                        subprocess.run(command)

                      
                        os.remove(input_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='convert files .')
    parser.add_argument('--output', type=str, help='output directory', required=True)
    args = parser.parse_args()

    main(args.output)
