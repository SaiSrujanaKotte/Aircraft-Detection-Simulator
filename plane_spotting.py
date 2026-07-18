import cv2

# Read the image
Aeroplane_image = cv2.imread("Aeroplane_image.jpg")

# Check if image loaded successfully
if Aeroplane_image is None:
    print("ERROR: Image cannot be found!")
else:
    # Draw the bounding box
    cv2.rectangle(
        Aeroplane_image,
        (320, 200),      # Top-left corner (x1, y1)
        (700, 470),      # Bottom-right corner (x2, y2)
        (0, 255, 0),     # Green color (BGR)
        2                # Thickness
    )

    # Aircraft label
    cv2.putText(
        Aeroplane_image,
        "Unidentified Aircraft",
        (320, 190),                      # Slightly above the rectangle
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    # Detection date
    cv2.putText(
        Aeroplane_image,
        "Detected: 18 Jul 2026",
        (20, 40),                        # Top-left corner of the image
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),                   # Yellow
        2
    )

    # Display the image
    cv2.imshow("Aircraft Detection Simulator", Aeroplane_image)

    # Save the output image
    success = cv2.imwrite("entry_01.jpg", Aeroplane_image)

    if success:
        print("✅ Image saved successfully as entry_01.jpg")
    else:
        print("❌ Failed to save image")

    cv2.waitKey(0)
    cv2.destroyAllWindows()