import time
from datetime import datetime, timezone
from pathlib import Path

from picamera2 import Picamera2, Preview

from experiments.series001 import PATH_PKG


def print_metadata(metadata):
    for key, value in metadata.items():
        print(f'{key}: {value}')


def snap1(path_dir_out: Path):
    # Step: Init
    path_dir_out.mkdir(exist_ok=True, parents=True)

    # Step: Init Camera
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration(main={'size': (4608, 2592)}, lores={'size': (640, 480)}, encode='lores')
    picam2.configure(camera_config)
    # picam2.start_preview(Preview.QTGL)
    picam2.start_preview(Preview.DRM)
    picam2.start()
    time.sleep(5)

    # Step: Save
    for i in range(3):
        dt = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S%f")
        filename = path_dir_out / f'DSCPI_{dt}.jpg'
        picam2.capture_file(filename)


def snap2(path_dir_out: Path):
    # Step: Init
    path_dir_out.mkdir(exist_ok=True, parents=True)

    # Step: Init Camera
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration(main={'size': (4608, 2592)}, lores={'size': (640, 480)}, encode='lores')
    picam2.configure(camera_config)
    # picam2.start_preview(Preview.QTGL)
    picam2.start_preview(Preview.DRM)
    picam2.start()
    time.sleep(5)

    # Step: Save
    for i in range(3):
        dt = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S%f")
        path_file_out = path_dir_out / f'DSCPI_{dt}.jpg'

        (buffer,), metadata = picam2.capture_buffers(["main"])
        print(dt)
        print_metadata(metadata)
        print()
        img = picam2.helpers.make_image(buffer, picam2.camera_configuration()["main"])
        picam2.helpers.save(img, metadata, path_file_out)


if __name__ == "__main__":
    path_dir_out = PATH_PKG / "out"
    snap2(path_dir_out)
