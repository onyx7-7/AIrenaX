# AIrenaX
# AIrenaX

AIrenaX is a smart stadium management system designed to enhance the fan experience. The app leverages AI technologies to improve crowd management, provide personalized navigation, and offer virtual queueing for stadium services.

## MVP Features

### 1. **AI-powered Crowd Detection**
   - The app uses AI models like YOLO to monitor and assess crowd density in the stadium.
   - Helps identify areas of high congestion and optimize crowd movement, improving overall stadium safety and comfort.

### 2. **Virtual Queueing**
   - Fans can join virtual queues for services like food, beverages, or merchandise from their seats.
   - The app sends notifications to users when it’s their turn, minimizing wait times and preventing long lines.

### 3. **Personalized Seat Navigation**
   - The app uses AR/VR technology to guide fans to their seats and around the stadium.
   - Makes use of computer vision models like Mask R-CNN for seat detection and SLAM for navigation to provide real-time directions.

## Tech Stack

- **Frontend**: Flutter for cross-platform mobile development (iOS and Android)
- **Backend**: Node.js with Express for handling API requests
- **AI Models**: YOLO for crowd detection, Mask R-CNN for seat detection, SLAM for navigation
- **Authentication**: JWT (JSON Web Tokens) for secure user login
- **Storage**: SharedPreferences for local storage

## Installation

### Prerequisites

Make sure you have the following installed on your system:
- [Flutter](https://flutter.dev/docs/get-started/install) (for building the app)
- [Node.js](https://nodejs.org/) (for backend)

