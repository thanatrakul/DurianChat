from reversion.admin import VersionAdmin


class SoftControlAdminModel(VersionAdmin):
    actions_on_top = True
    save_on_top = True

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.created_user = request.user
        obj.updated_user = request.user

        # obj.save()
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for obj in formset.deleted_objects:
            obj.delete()

        for instance in instances:
            # Do something with `instance`

            if instance.pk is None:
                instance.created_user = request.user
            instance.updated_user = request.user
            instance.save()
        formset.save_m2m()
        # formset.save()
