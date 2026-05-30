# AWS Image Resizer Automation

## Overview

AWS Image Resizer Automation is a serverless image processing application built using AWS S3, AWS Lambda, and Python.

The application automatically resizes images uploaded by users to an input S3 bucket and stores the processed images in a separate output S3 bucket. This eliminates manual image processing and demonstrates event-driven automation using AWS services.

---

## Architecture

1. User uploads an image to the Input S3 Bucket.
2. The upload event triggers an AWS Lambda function.
3. The Lambda function retrieves the uploaded image from the Input Bucket.
4. The image is resized to 300x300 pixels using the Pillow library.
5. The processed image is stored in the Output S3 Bucket with the prefix `resized-`.
6. The process completes automatically without any manual intervention.

### Workflow

User Upload → Input S3 Bucket → Lambda Trigger → Image Processing (Python + Pillow) → Output S3 Bucket

---

## AWS Services Used

### Amazon S3

* Stores original images uploaded by users.
* Stores resized images after processing.
* Generates events that trigger the Lambda function.

### AWS Lambda

* Executes image resizing logic.
* Processes images automatically upon upload.
* Eliminates the need to manage servers.

---

## Technologies Used

* Python
* AWS Lambda
* Amazon S3


* Fully automated image resizing.
* Serverless implementation.
* Scalable and cost-efficient solution.
* No manual image processing required.

---



├── lambda_function.py


└── README.md

## How It Works

2. Create an Output S3 Bucket.
3. Configure an S3 Event Notification on the Input Bucket.
4. Trigger the Lambda function whenever a new image is uploaded.
5. Set the OUTPUT_BUCKET environment variable in Lambda.
6. Upload an image to the Input Bucket.
7. The Lambda function automatically resizes the image and stores it in the Output Bucket.

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Amazon S3
* Python automation
* Serverless computing
* AWS IAM permissions
* Boto3 SDK integration

