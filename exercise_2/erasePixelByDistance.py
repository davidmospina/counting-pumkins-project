import cv2
import numpy as np
import json
from scipy.spatial import distance

def mahalanobis_distance(x, mean, covariance_inv):
    diff = x - mean
    return np.sqrt(np.dot(np.dot(diff, covariance_inv), diff.T))
    #return cv2.Mahalanobis(x,mean,covariance_inv)

def process_image(input_image_path, output_image_path, mean_rgb, covariance_matrix_rgb, distance_threshold):
    # Load the image
    image = cv2.imread(input_image_path)

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Flatten the image to a 1D array per channel
    pixels = image_rgb.reshape((-1, 3))

    # Calculate the Mahalanobis distance for each pixel in RGB space
    covariance_inv_rgb = np.linalg.inv(np.array(covariance_matrix_rgb))
    distances = np.array([mahalanobis_distance(pixel, mean_rgb, covariance_inv_rgb) for pixel in pixels])

    # Threshold the distances and set pixels below the threshold to black
    mask = distances > distance_threshold
    pixels[mask] = [0, 0, 0]

    # Reshape the processed pixels back to the original image shape
    processed_image_rgb = pixels.reshape(image_rgb.shape)

    # Convert RGB back to BGR
    processed_image = cv2.cvtColor(processed_image_rgb, cv2.COLOR_RGB2BGR)

    # Save the processed image
    cv2.imwrite(output_image_path, processed_image)

if __name__ == "__main__":
    # Define the input and output paths
    input_image_path = "/home/david/Documents/SDU/second_term/large_scale_drone_perception/miniproject/Images for first miniproject/EB-02-660_0594_0385.JPG"
    output_image_path = "pumpkingSegmented.jpg"
    json_file_path = "/home/david/Documents/SDU/second_term/large_scale_drone_perception/miniproject/pumpkinsStatistics.json"

    # Read mean and covariance values from the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        mean_rgb = data["mean_rgb"]
        covariance_matrix_rgb = data["covariance_matrix_rgb"]

    # Set the Mahalanobis distance threshold
    distance_threshold = 4.0

    # Process the image
    process_image(input_image_path, output_image_path, mean_rgb, covariance_matrix_rgb, distance_threshold)
