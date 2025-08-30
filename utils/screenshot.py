import Quartz
import numpy as np
from AppKit import NSWorkspace
from PIL import Image

# regions for Google Play Games
crk_value_region = (1354, 774, 180, 483)
crk_roll_region = (544, 774, 593, 483)

# screenshot crk window to locate reset all button.
def screenshotWindow(bounds, pid, alterX=0, alterY=0, alterWidth=None, alterHeight=None):
    x = float(bounds["X"] + alterX)
    y = float(bounds["Y"] + alterY)
    w = alterWidth or float(bounds["Width"])
    h = alterHeight or float(bounds["Height"])
    rect = Quartz.CGRectMake(x, y, w, h)

    cgimg = Quartz.CGWindowListCreateImage(rect, Quartz.kCGWindowListOptionIncludingWindow,
                                           int(pid), Quartz.kCGWindowImageDefault)

    if not cgimg:
        raise RuntimeError("CGWindowListCreateImage returned None. Check Screen Recording permission or the window ID.")

    width = Quartz.CGImageGetWidth(cgimg)
    height = Quartz.CGImageGetHeight(cgimg)
    bytes_per_row = Quartz.CGImageGetBytesPerRow(cgimg)

    provider = Quartz.CGImageGetDataProvider(cgimg)
    data = Quartz.CGDataProviderCopyData(provider)
    buf = np.frombuffer(data, dtype=np.uint8)

    # Reshape with padding taken into account
    buf = buf.reshape((height, bytes_per_row))
    buf = buf[:, :width * 4]  # drop padding bytes
    buf = buf.reshape((height, width, 4))

    # macOS CGImage data is usually BGRA
    buf = buf.reshape((height, width, 4))
    # Convert BGRA → RGBA
    buf = buf[:, :, [2, 1, 0, 3]]

    img = Image.fromarray(buf, 'RGBA')
    return img

# get crk window and resize. prep for screenshot.
def findAndResize():
    workspace = NSWorkspace.sharedWorkspace()
    apps = workspace.runningApplications()
    for app in apps:
        if app.localizedName() == "Cookie Run: Kingdom":
            pid = app.processIdentifier()
            print(pid)
            windows = Quartz.CGWindowListCopyWindowInfo(
                Quartz.kCGWindowListOptionOnScreenOnly,
                Quartz.kCGNullWindowID
            )
            for w in windows:
                if w['kCGWindowOwnerPID'] == pid:
                    print(w['kCGWindowBounds'])
                    return w['kCGWindowBounds'], w['kCGWindowNumber']  # x, y, width, height
    return None

# type of roll. CD, ATK, etc.
# makes use of the emu counts to determine, since future would further support more
def screenshotRoll(win, pid, scale_x, scale_y):
    x, y, width, height = crk_roll_region
    x = x // scale_x
    y = y // scale_y
    width = width // scale_x
    height = height // scale_y
    img = screenshotWindow(win, pid, x, y, width, height)
    # img.save("images/roll.png")
    return img


# cropped size is 275 x 335.
def screenshotValues(win, pid, scale_x, scale_y):
    x, y, width, height = crk_value_region
    x = x // scale_x
    y = y // scale_y
    width = width // scale_x
    height = height // scale_y
    img = screenshotWindow(win, pid, x, y, width, height)
    # img.save("images/value.png")
    return img
    





