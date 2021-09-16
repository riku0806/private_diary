from django.core.mail import EmailMessage, message
from django import forms
from django.core.mail import EmailMessage
from django.forms import fields
from .models import Diary


class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = "お問い合わせ{}".format(title)
        message = '送信者名:{0}\nメールアドレス:{1}\nメッセージ:\n{2}'.format(
            name, email, message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]
        message = EmailMessage(subject=subject, body=message,
                               from_email=from_email, to=to_list, cc=cc_list)
        message.send()


class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content', 'photo1', 'photo2', 'photo3',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
