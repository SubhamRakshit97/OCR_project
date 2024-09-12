# Visiting Card Upload and Text Extraction

## Objective

A Python-based web application that allows users to upload an image of a visiting card, extracts the text using Optical Character Recognition (OCR), and automatically populates predefined text fields such as Name, Job Title, Company Name, Email Address, Phone Number, and Address.

---

## Features

### Frontend
- **Upload Interface**: A simple web interface that allows users to upload a visiting card image.
  - Supports drag-and-drop functionality as well as traditional file input.
  - Displays a preview of the uploaded image.
  
- **Text Fields**: Fixed text fields for:
  - Name
  - Job Title
  - Company Name
  - Email Address
  - Phone Number
  - Address
  - These fields will be automatically populated after OCR processing.

- **User Feedback**:
  - Loading animations or progress indicators while the OCR process is running.
  - Validation messages for invalid uploads or OCR failures.

### Backend
- **File Upload Handling**: 
  - Backend using Flask/Django for image file handling.
  - Uploaded images are stored temporarily for OCR processing.
  
- **OCR Processing**: 
  - Uses Tesseract OCR (via the `pytesseract` package) to extract text from the uploaded images.
  - Extracted data is parsed and mapped to the corresponding fields.
  
- **API Endpoints**:
  - `/upload`: Accepts an image file, processes it using OCR, and returns the extracted data in JSON format.
  - `/cards`: Retrieves all stored entries from the database with pagination.

### Database
- **Data Storage**:
  - Extracted data and original image filename are stored in the database.
  - Fields: Name, Job Title, Company Name, Email Address, Phone Number, Address, and Timestamp.
  
- **Data Retrieval**: 
  - `/cards` endpoint for retrieving the stored entries with pagination support.

### Deployment
- **Local Deployment**:
  - Set up the project environment locally using `pip` or `conda`.
  - Instructions to run locally provided in the next section.
  
- **Cloud Deployment**: 
  - Deployed on a free cloud platform that supports Python (e.g., Render).
  - Access the deployed application via the public URL.

---

## Local Setup and Deployment

### Prerequisites
- Python 3.8 or higher
- Virtual environment setup (recommended: `pip` or `conda`)
- Tesseract OCR installed on the system
  - On Ubuntu: `sudo apt-get install tesseract-ocr`
  - On macOS: `brew install tesseract`
  - On Windows: [Download Tesseract](https://github.com/tesseract-ocr/tesseract/wiki)

### Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/visiting-card-ocr.git
    cd visiting-card-ocr
    ```

2. **Set up the virtual environment**:
    ```bash
    # Using pip
    python3 -m venv env
    source env/bin/activate   # For Linux/macOS
    .\env\Scripts\activate    # For Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - For Django:
      ```bash
      python manage.py migrate
      ```

5. **Run the application**:
    ```bash
    # For Django:
    python manage.py runserver
    ```

6. **Access the application**:
    - Open your browser and go to `http://127.0.0.1:8000/` 

---

## Cloud Deployment
**Render Deployment**:
    - Follow [this guide](https://docs.render.com/deploys) to deploy your app on Render.

---

## API Documentation

### 1. `/upload` [POST]
- **Description**: Uploads an image and returns extracted text.
- **Parameters**: `image` (file)
- **Response**:
    ```json
    {
      "name": "John Doe",
      "job_title": "Software Developer",
      "company": "ABC Corp",
      "email": "johndoe@example.com",
      "phone": "+1234567890",
      "address": "123 Main St, City, Country"
    }
    ```

### 2. `/cards` [GET]
- **Description**: Retrieves all stored visiting cards with pagination.
- **Parameters**:
    - `page`: Page number (default is 1).
- **Response**:
    ```json
    {
      "cards": [
        {
          "name": "John Doe",
          "job_title": "Software Developer",
          "company": "ABC Corp",
          "email": "johndoe@example.com",
          "phone": "+1234567890",
          "address": "123 Main St, City, Country",
          "timestamp": "2024-09-12 10:20:30"
        }
      ],
      "pagination": {
        "page": 1,
        "total_pages": 10
      }
    }
    ```

---

## Technologies Used

- **Backend**: Django, Python, Tesseract OCR
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Deployment**: Render, Docker

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Feel free to submit issues or fork the repository and make a pull request with improvements!

---

## Author

- **Subham Rakshit** - [GitHub Profile](https://github.com/SubhamRakshit97)
