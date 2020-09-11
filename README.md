# Screen recorder
This script captures area around mouse cursor using mss library and saves captured frames ads images. Code is able to capture smooth framerate on desktop and fullscreen applications. Right now it is only tested on Windows. 

## Requirements
mss (ver 5.1 was used originally)
## To do
- [ ] Add script to render gifs and movies from image frames
- [ ] Ensure multiplatform support
- [ ] Add shortkeys support

## Uses
Script was written with `argparse` library, so you can always type `python main.py -h` for help with arguments. In default mode screen capture is set to record square part of the screen **400x400** for **10 seconds**. To set record mode for *2 seconds* with *500x500* resolution use:

```console
python main.py -s 500 -t 2
```
