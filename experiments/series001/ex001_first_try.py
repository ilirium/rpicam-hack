import time
from datetime import datetime, timezone
from pathlib import Path

from picamera2 import Picamera2, Preview

from experiments.series001 import PATH_PKG

"""
picam2 = picamera2.Picamera2
picam2.helpers.save

picamera2/request.py/Helpers/save

"""


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
        print(f'snap {i}, {dt}')

        path_file_out_img = path_dir_out / f'DSCPI_{dt}.jpg'
        path_file_out_txt = path_dir_out / f'DSCPI_{dt}.txt'

        (buffer,), metadata = picam2.capture_buffers(["main"])

        img = picam2.helpers.make_image(buffer, picam2.camera_configuration()["main"])
        picam2.helpers.save(img=img, metadata=metadata, file_output=str(path_file_out_img))

        with open(path_file_out_txt, 'w') as fp:
            for key, value in metadata.items():
                fp.write(f'{key}: {value}\n')


if __name__ == "__main__":
    folder_dt_day = datetime.now(timezone.utc).strftime("%Y%m%d")
    folder_dt_full = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    path_dir_out = PATH_PKG / "out" / folder_dt_day / folder_dt_full
    snap2(path_dir_out)
