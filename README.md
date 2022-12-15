[comment]: <> (This readme was created by Nodinq Readme Generator)
![alt text](https://img.shields.io/badge/License-MIT-brightgreen)
![alt text](https://img.shields.io/badge/Ver.-1.0.0-blue)

# TV Decibel Keeper


## Description

This code is setting up a python program to check the volume of a TV connected to a local network. It is initializing the PyAudio library, setting up the format of the audio, channels, and rate, and then creating a stream that reads in the data from the TV. It then processes the audio data to calculate the decibel level, and checks that against a threshold to determine whether the volume should be increased or decreased. Finally, it closes the stream and terminates the program.
My motivation for controlling the noise levels at home is to ensure a peaceful and comfortable living environment. With this program, I can easily keep track of the sound levels in my home and adjust the TV volume accordingly. This will allow me to maintain a quiet and relaxing home environment without having to constantly adjust the volume manually. I also want to include my kids in this effort. They often like to turn up the volume on the TV, so this program will help me keep the noise levels in check and ensure that they don't get too loud. By setting up this program, I can be sure that my kids can enjoy their favorite shows and movies while keeping the noise levels in check.
What I learned from this program is that maintaining the volume level of a device is more complex than simply using decibels and responding to it. It requires knowledge of the audio format, channels, and rate, as well as an understanding of how to process the audio data to accurately calculate the decibel level. Additionally, it requires careful consideration of the threshold levels to ensure that the volume is neither too loud nor too quiet. This program has taught me the importance of using the right tools and understanding the complexities of sound and audio processing.

## Usage

For MacOS Monterrey install PyAudio using the following command:
`LDFLAGS="-L/opt/homebrew/Cellar/portaudio/19.7.0/lib" CFLAGS="-I/opt/homebrew/Cellar/portaudio/19.7.0/include" pip3 install pyaudio`


## Questions

Please send your questions [here](mailto:cristobal@barberis.com?subject=[GitHub]%20TV%20Decibel%20Keeper) or visit [github/brberis](https://github.com/brberis).

## Credits

* Cristobal A Barberis%   