import logging
import requests
from django.core.mail import EmailMultiAlternatives

def send_email_with_image(subject, message, from_email, recipient_list, image_url):
    try:
        # Fetch the image from the URL
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content

            # Create an EmailMultiAlternatives object
            email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
            email.attach('image.jpg', image_data, 'image/jpeg')  # Attach image directly
            email.send()

            logging.info("Email sent successfully")
        else:
            logging.error(f"Failed to fetch image from URL: {image_url}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")
        logging.error(f"URL: {image_url}")
