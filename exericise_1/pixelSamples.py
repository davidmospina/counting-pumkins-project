import cv2
import json
import numpy as np
# Function to handle mouse events

def save_to_json(data_array, file_path):
    # Convert the array to JSON format
    json_data = json.dumps(data_array, indent=2)

    # Write the JSON data to a file
    with open(file_path, 'w') as file:
        file.write(json_data)


def click_event(event, x, y, flags, param):
    global click_count, color_samples

    if event == cv2.EVENT_LBUTTONDOWN:
        # Get RGB values
        b, g, r = img[y, x]
        h,s,v = imgHSV[y,x]

        # Save color information to the dictionary
        color_info = {
            'pixel_number': click_count,
            'red': str(r),
            'green': str(g),
            'blue': str(b),
            'hue': str(h),         # Convert hue to string
            'saturation': str(s),  # Convert saturation to string
            'value': str(v)        # Convert value to string
        }

        color_samples.append(color_info)


        # Increment click count
        click_count += 1

        # Display the clicked point
        #print(f"Pixel {click_count}: RGB({r}, {g}, {b}), HSV({h}, {s}, {v})")

        # Draw a small circle at the clicked point
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        # Update the display
        cv2.imshow('Image', img)

# Load the image
img = cv2.imread('/home/david/Documents/SDU/second_term/large_scale_drone_perception/miniproject/Images for first miniproject/EB-02-660_0594_0385.JPG')  # Change the path to your image file
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Initialize variables
click_count = 1
color_samples = []

# Create a window and set the callback function
cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)

# Wait until 30 clicks are made
while click_count <= 30:
    cv2.waitKey(10)



save_to_json(color_samples,'/home/david/Documents/SDU/second_term/large_scale_drone_perception/miniproject/pumpkinsPixels.json')

# Close the window
cv2.destroyAllWindows()
