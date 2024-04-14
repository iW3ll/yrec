# yrec 

A python aplication for recording youtube lives.

## Requirements

• python 3  
• streamlink  
• pytube  
• ffmpeg or ffmpy  
• rclone

Install packages in requirements.txt using pip.

``pip install -r requirements.txt``  

## Usage

Interface  
• console

## How to use
``Add link in wish.txt``

````
python3 yrec.py

````
``After finishing convert files from .ts to .mp4``
````
python3 merge.py --output 'output_folder'  

````
If you want to send your files to any cloud you can use ``yrclone.py`` (optional)

Visit [rclone](https://rclone.org/) to learn how to create a configuration for yrclone.py before using it

