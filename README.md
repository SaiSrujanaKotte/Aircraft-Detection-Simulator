# Aircraft Detection Simulator (Manual Bounding Box)
A simple tool that takes a real plane-spotting photo and overlays a manually 
calibrated bounding box, label, and detection timestamp — simulating the 
output format of an object detection system.

## What it demonstrates?
- Image I/O and coordinate systems in OpenCV
- Manual bounding box calibration from percentage estimates to pixel coordinates
- Text/shape overlay rendering

## Example
I have taken by me while plane-spotting, Teisnach, Germany — 18 Jul 2026.

## Why this matters?
This is the manual, hand-calculated version of what automated object detection 
models (e.g. YOLO) do in Phase 5 of my CV learning roadmap. Understanding 
bounding box coordinates by hand first builds the intuition needed to debug 
and validate automated detections later.