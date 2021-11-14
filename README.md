# Mask R-CNN
Instance segmentation with Mask [R-CNN](https://arxiv.org/pdf/1703.06870v3.pdf)
<p align="center">
<img width="700"  src="framework.png"/> 
</p>




## Requirements

<table>
<tr>
  <td>OpenCV</td>
  <td>
    <a href="https://pypi.org/project/opencv-python/">
    <img src="https://img.shields.io/badge/OpenCV-4.5.4.58-red" alt="OpenCV" />
    </a>
  </td>
</tr>
<tr>
  <td>PixelLib</td>
  <td>
    <a href="https://pixellib.readthedocs.io/en/stable/">
    <img src="https://img.shields.io/badge/PixelLib-3.5--3.7-green" alt="PixelLib" />
    </a>
  </td>
</tr>
  <tr>
  <td>Mask R-CNN</td>
  <td>
    <a href="https://github.com/matterport/Mask_RCNN/releases/tag/v2.0">
    <img src="https://img.shields.io/badge/Mask%20R--CNN-2.0-yellow" alt="Mask R-CNN" />
    </a>
  </td>
</tr>
</table>

This code  works on Python 3.5 or later.

* * *
# Usage

For real-time video segmentation run the `realtime.sh` script from a terminal, like this:
```
$ bash Run.sh
```
For local video segmentation replace the path to your video file in the `Instance_segment_from path.py` and run the `from_path.sh` script from a terminal, like this:
```
$ bash from_path.sh
```
