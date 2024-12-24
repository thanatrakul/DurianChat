from django import forms


class ControlModelForm(forms.ModelForm):
    # def save(self, commit=True):
    #     instance = super().save(commit=False)

    #     print("*" * 50, "Save", self.__dict__)
    #     # if not instance.pk:
    #     #     instance.created_user = self.user
    #     # instance.updated_user = self.user

    #     if commit:
    #         instance.save()
    #         self.save_m2m()
    #     return instance

    def form_valid(self, form):
        if form.non_field_errors():
            return super().form_invalid()

        if not self.object:
            form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user

        return super().form_valid(form)


class SoftControlModelForm(ControlModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_deleted'].widget = forms.HiddenInput()


class HardControlControlModelForm(ControlModelForm):
    pass
