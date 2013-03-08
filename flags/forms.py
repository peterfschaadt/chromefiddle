from django import forms
from django.contrib.comments import CommentForm
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from django.conf import settings
import datetime


class ContactForm(forms.Form):
    """
    Form for contact page.
    """
    sender_name = forms.CharField(max_length=100)
    sender =      forms.EmailField()
    subject =     forms.CharField(max_length=100)
    message =     forms.CharField()
    cc_myself =   forms.BooleanField(required=False)


class FlagCommentForm(CommentForm):
    """
    Form for commenting on Flag details.
    """
    def get_comment_create_data(self):
        return dict(
            content_type = ContentType.objects.get_for_model(self.target_object),
            object_pk =    force_unicode(self.target_object._get_pk_val()),
            comment =      self.cleaned_data['comment'],
            submit_date =  datetime.datetime.now(),
            site_id =      settings.SITE_ID,
            is_public =    True,
            is_removed =   False,
        )

# Remove URL and Email fields from comment form
FlagCommentForm.base_fields.pop('email')
FlagCommentForm.base_fields.pop('url')