import os
import argparse
import subprocess

def convert_to_wav(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert each MP3 file to WAV format using ffmpeg
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".wav")
            subprocess.call(["ffmpeg", "-i", input_path, "-acodec", "pcm_s16le", "-ar", "44100", output_path])

if __name__ == "__main__":
    # Define the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder", help="the folder containing the MP3 files")
    parser.add_argument("output_folder", help="the folder to save the WAV files")

    # Parse the arguments
    args = parser.parse_args()

    # Call the conversion function
    convert_to_wav(args.input_folder, args.output_folder)