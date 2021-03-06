from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import TemplateView
import httpagentparser
from flags.models import Flag
from forms import ContactForm
from django.template.defaultfilters import slugify
import traceback
from django.utils.log import getLogger
logger = getLogger('app')


def home(request):
    """
    View for Home page.
    """
    # Pull user agent string from web request
    user_agent = request.META['HTTP_USER_AGENT']
    # Parse user agent string for OS, browser, and version
    user_info = httpagentparser.detect(user_agent)
    
    # logger.info('USER AGENT STRING: %s' % user_agent)
    # logger.info('USER INFO: %s' % user_info)

    # test_user_mac = {'flavor': {'version': 'X 10.8.2', 'name': 'MacOS'}, 'os': {'name': 'Macintosh'}, 'browser': {'version': '24.0.1312.57', 'name': 'Chrome'}}
    # test_user_android = {'dist': {'version': '4.0.4', 'name': 'Android'}, 'os': {'name': 'Linux'}, 'browser': {'version': '26.0.1410.40', 'name': 'Chrome'}}

    # Workaround to prevent Android device from being identified as Linux device
    if 'dist' in user_info:
        operating_system = user_info['dist']['name'].lower()
    else:
        operating_system = user_info['os']['name'].lower()

    # Check for operating system type
    if operating_system == 'macintosh':
        os = 'Mac OS X'
        supported_flags = Flag.objects.filter(is_mac=True)
    elif operating_system == 'windows':
        os = 'Windows'
        supported_flags = Flag.objects.filter(is_windows=True)
    elif operating_system == 'linux':
        os = 'Linux'
        supported_flags = Flag.objects.filter(is_linux=True)
    elif operating_system == 'chrome-os':
        os = 'Chrome OS'
        supported_flags = Flag.objects.filter(is_chrome_os=True)
    elif operating_system == 'android':
        os = 'Android'
        supported_flags = Flag.objects.filter(is_android=True)
    else:
        # Display all flags if user's OS cannot be determined
        os = 'an unfamiliar OS'
        supported_flags = Flag.objects.all()

    os_slug = slugify(os)

    return render(request, 'home.html', {'os': os, 'os_slug': os_slug,
                                         'browser': user_info['browser'],
                                         'supported_flags': supported_flags})


def flags(request):
    """
    View for page listing all flags.
    """
    all_flags = Flag.objects.all()
    # flag_count = all_flags.count()
    # logger.info('TOTAL FLAGS: %d' % flag_count)
    return render(request, 'flags.html', {'all_flags': all_flags})


def details(request, flag_id):
    """
    View for flag details.
    """
    try:
        flag = Flag.objects.get(pk=flag_id)
    except Flag.DoesNotExist:
        raise Http404
    return render(request, 'details.html', {'flag': flag})


def mac(request):
    """
    View for Mac compatible flags.
    """
    os = 'Mac OS X'
    os_slug = slugify(os)
    mac_flags = Flag.objects.filter(is_mac=True)
    return render(request, 'os.html', {'os': os, 'os_slug': os_slug,
                                       'os_flags': mac_flags})


def windows(request):
    """
    View for Windows compatible flags.
    """
    os = 'Windows'
    os_slug = slugify(os)
    windows_flags = Flag.objects.filter(is_windows=True)
    return render(request, 'os.html', {'os': os, 'os_slug': os_slug,
                                       'os_flags': windows_flags})


def linux(request):
    """
    View for Linux compatible flags.
    """
    os = 'Linux'
    os_slug = slugify(os)
    linux_flags = Flag.objects.filter(is_linux=True)
    return render(request, 'os.html', {'os': os, 'os_slug': os_slug,
                                       'os_flags': linux_flags})


def chrome_os(request):
    """
    View for Linux compatible flags.
    """
    os = 'Chrome OS'
    os_slug = slugify(os)
    chrome_os_flags = Flag.objects.filter(is_chrome_os=True)
    return render(request, 'os.html', {'os': os, 'os_slug': os_slug,
                                       'os_flags': chrome_os_flags})


def android(request):
    """
    View for Android compatible flags.
    """
    os = 'Android'
    os_slug = slugify(os)
    android_flags = Flag.objects.filter(is_android=True)
    return render(request, 'os.html', {'os': os, 'os_slug': os_slug,
                                       'os_flags': android_flags})


def contact(request):
    """
    View for Contact page with form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['sender_name']
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['peter.schaadt@gmail.com']
            if cc_myself:
                recipients.append(sender)

            message = 'ChromeFiddle Contact Form\n' \
                      'message from: %s\n' \
                      'reply to: %s\n\n' % (sender_name, sender) + message

            # Attempt to send email, log information and traceback if error
            try:
                from django.core.mail import send_mail
                send_mail(subject, message, 'peter.schaadt@gmail.com', recipients)
                # logger.info('### Sending mail!')
            except:
                mail_error = traceback.format_exc()
                # logger.error('Contact Form - error sending mail: %s' % mail_error +
                #             '\n%s\n%s\n%s' % (subject, message, recipients))

            # Redirect after POST request
            return HttpResponseRedirect('/thanks')
    else:
        # Unbound form
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def thanks(request):
    """
    View for Thanks page after contact form.
    """
    return render(request, 'thanks.html', {})
