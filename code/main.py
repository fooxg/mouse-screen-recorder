from ctypes import windll, Structure, c_long, byref
import mss
import argparse
from time import time
from gif_maker import make_gif


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return (pt.x,pt.y)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Capture screen around cursor.')

    parser.add_argument('-s', dest='size', type=int, default = 400,
                    help='Size of image around mouse')
    
    parser.add_argument('-t', dest='time', type=int, default = 10,
                    help='Time of the recording')

    parser.add_argument('-m', dest='gif_save', type=bool, default = False,
                    help='Whether to save a sequence as gif (True/False)')
    args = parser.parse_args()
        
    sh  = int(args.size/2)
    sct = mss.mss()

    ts = time()
    i   = 0
    while time()<(ts+args.time):
        x, y = queryMousePosition()
        img=sct.grab({"top": y-sh, "left": x-sh, "width": args.size, "height": args.size})
        mss.tools.to_png(img.rgb, img.size, output="..//img//screen_" + "0"*(5-len(str(i))) + str(i) + ".png")
        i+=1
    if args.gif_save:
        make_gif("sample",i)
