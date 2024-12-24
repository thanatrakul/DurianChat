from .models import FacebookPage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from django import forms


class FacebookPageForm(forms.ModelForm):
    class Meta:
        model = FacebookPage
        fields = [
            "name",
            "icon",
            "page_id",
            "access_token"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 col-form-label"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(Submit("submit", "Add Page", css_class="btn btn-primary"))
        self.helper.layout = Layout(
            Field("name", css_class="form-control"),
            Field("icon", css_class="form-control"),
        )
