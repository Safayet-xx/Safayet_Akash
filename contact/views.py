from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Compose email content
            subject = f'Contact Form Submission from {name}'
            message_body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            
            # Send email
            send_mail(
                subject,  # Subject
                message_body,  # Message
                email,  # From email (sender)
                [settings.EMAIL_HOST_USER],  # To email (recipient)
                fail_silently=False,
            )
            
            return redirect('home')  # Redirect after successful form submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
