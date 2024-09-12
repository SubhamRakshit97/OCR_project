from django.shortcuts import render
from django.http import JsonResponse
from .models import VisitingCard
from .forms import CardUploadForm
from django.views.decorators.csrf import csrf_exempt
import pytesseract
from PIL import Image
import re
import ipdb
from django.core.paginator import Paginator
# Create your views here.



def perform_ocr(image_path):
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    # ipdb.set_trace()
    return text


# def extract_info_from_text(text):
#     # Regular expressions for different data types
#     email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' 
#     # phone_regex = r'(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}'
#     phone_regex = r'(\+?\d{1,3}[\s.-]?)?(\(?0?\d{2,3}\)?[\s.-]?)?\d{3}[\s.-]?\d{3,4}'
#     url_regex = r'(https?://[^\s]+)|(www\.[^\s]+)'
#     job_title_regex = r'\b(Manager|Engineer|Developer|Designer|Director|Coordinator|Analyst|Consultant|Specialist|Executive|Administrator|Technician|CEO|Founder|Admin)\b'

    
#     # Extract email address
#     email_match = re.search(email_regex, text)
#     email = email_match.group() if email_match else None

#     # Extract phone number
#     phone_match = re.search(phone_regex, text)
#     phone_number = phone_match.group() if phone_match else None

#     # Extract website URL
#     url_match = re.search(url_regex, text)
#     website = url_match.group() if url_match else None

#     # Extract job title using regex
#     job_title = None
#     job_title_matches = re.finditer(job_title_regex, text, re.IGNORECASE)
#     for match in job_title_matches:
#         # Capture the complete line containing the job title
#         start_pos = text.rfind('\n', 0, match.start())
#         end_pos = text.find('\n', match.end())
#         start_pos = start_pos if start_pos != -1 else 0
#         end_pos = end_pos if end_pos != -1 else len(text)
#         job_title_text = text[start_pos:end_pos].strip()
#         job_title = job_title_text
#         break 

#     # Extract name from the first non-matching line or lines with specific patterns
#     lines = text.splitlines()
#     name = None
#     for line in lines:
#         if line.strip() and all(not re.search(regex, line) for regex in [email_regex, phone_regex, url_regex]):
#             name = line.strip()
#             break

#     # Extract address
#     address_lines = []
#     address_keywords = ['Street', 'Ave', 'Avenue', 'Rd', 'Road', 'Blvd', 'Boulevard', 'Suite', 'Unit','St','City']
#     # for line in lines:
#     #     if any(keyword in line for keyword in address_keywords) or any(char.isdigit() for char in line):
#     #         address_lines.append(line.strip())

#     # address = " ".join(address_lines).strip() if address_lines else None
#     for line in lines:
#         # Ensure the line doesn't contain phone numbers or email addresses
#         if any(keyword in line for keyword in address_keywords) or any(char.isdigit() for char in line):
#             # Remove the phone number from the line if it exists
#             cleaned_line = re.sub(phone_regex, '', line).strip()
#             if cleaned_line:  # Add the cleaned line if not empty after removing phone number
#                 address_lines.append(cleaned_line)

#     address = " ".join(address_lines).strip() if address_lines else None

    

#     if job_title and address:
#         address = re.sub(re.escape(job_title), '', address, flags=re.IGNORECASE).strip()

#     # Extract company name
#     company_name = None
#     company_keywords = ['Company', 'Corp', 'Corporation', 'Ltd', 'Limited', 'Inc', 'Incorporated', 'LLC','www']
#     for line in lines:
#         if any(keyword in line for keyword in company_keywords):
#             company_name = line.strip()
#             break
    
#     # Icons are wrongly interpreted as @ so removing them except from email
#     name = name.replace('@', '') if name else None
#     job_title = job_title.replace('@', '') if job_title else None
#     company_name = company_name.replace('@', '') if company_name else None
#     address = address.replace('@', '') if address else None
#     website = website.replace('@', '') if website else None

#     # Creating a dictionary of extracted information
#     extracted_info = {
#         "name": name,
#         "job_title": job_title,
#         "company_name": company_name,
#         "email": email,
#         "phone_number": phone_number,
#         "address": address,
#         "website": website
#     }
    
#     return extracted_info

#current correct
# import re

# def extract_info_from_text(text):
#     # Regular expressions for different data types
#     email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     phone_regex = r'(\+?\d{1,3}[\s.-]?)?\(?\d{3,4}\)?[\s.-]?\d{3}[\s.-]?\d{3,4}'
#     url_regex = r'(https?://[^\s]+)|(www\.[^\s]+)'
#     job_title_regex = r'\b(Manager|Engineer|Developer|Designer|Director|Coordinator|Analyst|Consultant|Specialist|Executive|Administrator|Technician|CEO|Founder|Admin)\b'
    
#     # Extract email address
#     email_match = re.search(email_regex, text)
#     email = email_match.group() if email_match else None

#     # Extract phone number but exclude pin code-like numbers (specifically checking for 6-digit sequences)
#     phone_match = re.search(phone_regex, text)
#     phone_number = phone_match.group() if phone_match and not re.fullmatch(r'\d{6}', phone_match.group().replace(' ', '')) else None  # Ensuring phone number is not a 6-digit pin code

#     # Extract website URL
#     url_match = re.search(url_regex, text)
#     website = url_match.group() if url_match else None

#     # Extract job title using regex
#     job_title = None
#     job_title_matches = re.finditer(job_title_regex, text, re.IGNORECASE)
#     for match in job_title_matches:
#         # Capture the complete line containing the job title
#         start_pos = text.rfind('\n', 0, match.start())
#         end_pos = text.find('\n', match.end())
#         start_pos = start_pos if start_pos != -1 else 0
#         end_pos = end_pos if end_pos != -1 else len(text)
#         job_title_text = text[start_pos:end_pos].strip()
#         job_title = job_title_text
#         break

#     # Extract name from the first non-matching line or lines with specific patterns
#     lines = text.splitlines()
#     name = None
#     for line in lines:
#         if line.strip() and all(not re.search(regex, line) for regex in [email_regex, phone_regex, url_regex]):
#             name = line.strip()
#             break

#     # Extract address by filtering out lines that contain email, URL, or phone numbers
#     address_lines = []
#     address_keywords = ['Street', 'Ave', 'Avenue', 'Rd', 'Road', 'Blvd', 'Boulevard', 'Suite', 'Unit', 'St', 'City', 'Nagar', 'Block', 'Cross', 'Main', 'PIN']
#     for line in lines:
#         if line.strip() and all(not re.search(regex, line) for regex in [email_regex, phone_regex, url_regex]):
#             # If the line has address keywords or contains digits (but is not a phone number), assume it's part of the address
#             if any(keyword in line for keyword in address_keywords) or (any(char.isdigit() for char in line) and len(line.strip()) > 10):
#                 address_lines.append(line.strip())

#     # Join address lines into a single string
#     address = " ".join(address_lines).strip() if address_lines else None

#     # Remove job title from address (if mistakenly included)
#     if job_title and address:
#         address = re.sub(re.escape(job_title), '', address, flags=re.IGNORECASE).strip()

#     # Extract company name by looking for common company keywords, handling multi-line names
#     company_name = None
#     company_keywords = ['Company', 'Corp', 'Corporation', 'Ltd', 'Limited', 'Inc', 'Incorporated', 'LLC', 'Co.']
#     company_name_lines = []
#     for i, line in enumerate(lines):
#         if any(keyword in line for keyword in company_keywords):
#             company_name_lines.append(line.strip())
#             # Check if the next line might also be part of the company name
#             if i + 1 < len(lines) and not any(re.search(regex, lines[i + 1]) for regex in [email_regex, phone_regex, url_regex]):
#                 company_name_lines.append(lines[i + 1].strip())
#             break
    
#     # Join multi-line company names into a single string
#     company_name = " ".join(company_name_lines).strip() if company_name_lines else None
    

#     # Clean up artifacts in the extracted information
#     name = name.replace('@', '') if name else None
#     job_title = job_title.replace('@', '') if job_title else None
#     company_name = company_name.replace('@', '') if company_name else None

#     # List of symbols to remove in address as its taking any icon infront of it as text
#     symbols_to_remove = ['@', '©', '®']
#     for symbol in symbols_to_remove:
#         address = address.replace(symbol, '')


#     website = website.replace('@', '') if website else None

#     # Creating a dictionary of extracted information
#     extracted_info = {
#         "name": name,
#         "job_title": job_title,
#         "company_name": company_name,
#         "email": email,
#         "phone_number": phone_number,
#         "address": address,
#         "website": website
#     }

#     return extracted_info

import re

def extract_info_from_text(text):
    # Regular expressions for different data types
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_regex = r'(\+?\d{1,3}[\s.-]?)?\(?\d{3,4}\)?[\s.-]?\d{3}[\s.-]?\d{3,4}'
    url_regex = r'(https?://[^\s]+)|(www\.[^\s]+)'
    job_title_regex = r'\b(Manager|Engineer|Developer|Designer|Director|Coordinator|Analyst|Consultant|Specialist|Executive|Administrator|Technician|CEO|Founder|Admin|CMD)\b'
    
    # Extract email address
    email_match = re.search(email_regex, text)
    email = email_match.group() if email_match else None

    # Extract phone number but exclude pin code-like numbers (specifically checking for 6-digit sequences)
    phone_match = re.search(phone_regex, text)
    phone_number = phone_match.group() if phone_match and not re.fullmatch(r'\d{6}', phone_match.group().replace(' ', '')) else None

    # Extract website URL
    url_match = re.search(url_regex, text)
    website = url_match.group() if url_match else None

    # Extract job title using regex
    job_title = None
    job_title_matches = re.finditer(job_title_regex, text, re.IGNORECASE)
    for match in job_title_matches:
        # Capture the complete line containing the job title
        start_pos = text.rfind('\n', 0, match.start())
        end_pos = text.find('\n', match.end())
        start_pos = start_pos if start_pos != -1 else 0
        end_pos = end_pos if end_pos != -1 else len(text)
        job_title_text = text[start_pos:end_pos].strip()
        job_title = job_title_text
        break

    # Extract name from the first non-matching line or lines with specific patterns
    lines = text.splitlines()
    name = None
    for line in lines:
        if line.strip() and all(not re.search(regex, line) for regex in [email_regex, phone_regex, url_regex]):
            name = line.strip()
            break

    # Extract address by filtering out lines that contain email, URL, or phone numbers
    address_lines = []
    address_keywords = ['Street', 'Ave', 'Avenue', 'Rd', 'Road', 'Blvd', 'Boulevard', 'Suite', 'Unit', 'St', 'City', 'Nagar', 'Block', 'Cross', 'Main', 'PIN']
    for line in lines:
        if line.strip() and all(not re.search(regex, line) for regex in [email_regex, phone_regex, url_regex]):
            # If the line has address keywords or contains digits (but is not a phone number), assume it's part of the address
            if any(keyword in line for keyword in address_keywords) or (any(char.isdigit() for char in line) and len(line.strip()) > 10):
                address_lines.append(line.strip())

    # Join address lines into a single string
    address = " ".join(address_lines).strip() if address_lines else None

    # Remove job title from address (if mistakenly included)
    if job_title and address:
        address = re.sub(re.escape(job_title), '', address, flags=re.IGNORECASE).strip()

    # Extract company name by looking for company keywords and stopping at the first match
    company_keywords = ['Company', 'Corp', 'Corporation', 'Ltd', 'Limited', 'Inc', 'Incorporated', 'LLC', 'Co.','Estate']
    company_name = None
    for line in lines:
        if any(keyword in line for keyword in company_keywords):
            company_name = line.strip()
            break

    # Clean up artifacts in the extracted information
    name = name.replace('@', '') if name else None
    job_title = job_title.replace('@', '') if job_title else None
    # company_name = company_name.replace('@', '') if company_name else None

    # List of symbols to remove in address as its taking any icon in front of it as text
    symbols_to_remove = ['@', '©', '®',"Q"]
    for symbol in symbols_to_remove:
        address = address.replace(symbol, '') if address else None
    symbols_to_remove_company=['®','www.reallygreatsite.com']
    for symbol1 in symbols_to_remove_company:
        company_name=company_name.replace(symbol1,'') if company_name else None
    website = website.replace('@', '') if website else None

    # Creating a dictionary of extracted information
    extracted_info = {
        "name": name,
        "job_title": job_title,
        "company_name": company_name,
        "email": email,
        "phone_number": phone_number,
        "address": address,
        "website": website
    }

    return extracted_info


def upload_card(request):
    # ipdb.set_trace()
    extracted_info = None
    if request.method == 'POST':
        form = CardUploadForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save()
            # Perform OCR on the uploaded image
            image_path = card.image.path
            extracted_text = perform_ocr(image_path)

            # Extract information from the extracted text
            extracted_info = extract_info_from_text(extracted_text)

            # Update the card instance with the extracted information
            card.name = extracted_info.get('name')
            card.job_title = extracted_info.get('job_title')
            card.company_name = extracted_info.get('company_name')
            card.email = extracted_info.get('email')
            card.phone_number = extracted_info.get('phone_number')
            card.address = extracted_info.get('address')
            card.save()

            # return JsonResponse({'message': 'Card uploaded and processed successfully!', 'data': extracted_info}, status=200)
    else:
        form = CardUploadForm()
    
    return render(request, 'cards/upload_card.html', context={'form': form, 'extracted_info': extracted_info})


def list_cards(request):
    # Get the page number from the request, default to 1 if not provided
    page_number = request.GET.get('page', 1)
    # Define the number of cards per page
    cards_per_page = 10
    
    # Get all cards from the database
    all_cards = VisitingCard.objects.all()
    
    # Create a Paginator object
    paginator = Paginator(all_cards, cards_per_page)
    
    # Get the current page of cards
    page_obj = paginator.get_page(page_number)
    
    # Convert the page object to a list of dictionaries
    cards_data = list(page_obj.object_list.values())
    
    # Prepare the response data with pagination info
    response_data = {
        'page': page_obj.number,
        'num_pages': paginator.num_pages,
        'total_cards': paginator.count,
        'cards': cards_data
    }
    
    return JsonResponse(response_data)



