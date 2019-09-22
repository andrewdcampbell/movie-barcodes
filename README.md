# movie-barcodes

Python program to generate a movie "barcode", or a visualization of the colour palette used in a film. It is generated by compressing each frame into a single column of pixels that are stacked sequentially to form a barcode-like image. Makes for a neat wallpaper.

There are many implementations available, and I don't claim this is the best, but it's clean, simple, efficient, and easily-customizable. Automatically adjusts sample rate according to the length of the video. Runs in under 2 minutes for a typical 2 hour movie.

Supported on Python 3 and OpenCV 3+. Tested on macOS.

## Requirements
* OpenCV
* numpy

## Example Results

<img src="https://github.com/andrewdcampbell/movie-barcodes/blob/master/compressed_barcode_examples/Dunkirk_barcode.jpg" width="100%"> 
Dunkirk

<img src="https://github.com/andrewdcampbell/movie-barcodes/blob/master/compressed_barcode_examples/Blade_Runner_2049_barcode.jpg" width="100%">
Blade Runner 2049

<img src="https://github.com/andrewdcampbell/movie-barcodes/blob/master/compressed_barcode_examples/Ratatouille_barcode.jpg" width="100%"> 
Ratatouille

<img src="https://github.com/andrewdcampbell/movie-barcodes/blob/master/compressed_barcode_examples/Tangled_barcode.jpg" width="100%">
Tangled

<img src="https://github.com/andrewdcampbell/movie-barcodes/blob/master/compressed_barcode_examples/Frozen_barcode.jpg" width="100%"> 
Frozen

<img src="https://github.com/andrewdcampbell/movie-barcodes/blob/master/compressed_barcode_examples/LOTR_FOTR_barcode.jpg" width="100%">
The Lord of the Rings: The Fellowship of the Ring


#### Uniform column mode

<img src="https://github.com/andrewdcampbell/movie-barcodes/blob/master/uniform_barcode_examples/Wall-E_barcode.jpg" width="100%"> 
WALL-E

<img src="https://github.com/andrewdcampbell/movie-barcodes/blob/master/uniform_barcode_examples/The_Handmaiden_barcode.jpg" width="100%">
The Handmaiden

## Usage
```
python barcode.py -video <PATH_TO_VIDEO> [-u]
```
* `-video`: The path to the movie to be processed. Only tested on `.mp4` files, but should work with any format supported by OpenCV.
* `-u`: Optional flag to compress all frames into a single color, thus producing uniform columns. 


#### Additional Notes
There are some constants defined in the code that can be changed if desired.
* Set `OUT_WIDTH` and `OUT_HEIGHT` to the desired output dimensions.
* Set `SAMPLE_HEIGHT` to change the granularity of the columns. `SAMPLE_HEIGHT` should be at most the input video height and at least 1 (which is equivalent to using the `-u` flag). This is a matter of personal preference; larger values preserve more detail while smaller values yield smoother results.
* Tip: use low-resolution videos. It won't effect the result at all and it will run much faster.
