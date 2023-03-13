# If you want to show only available choices for a foreignfield for a model. 

# create a form as per below and use it in a modeladmin.

class ModelAAdminForm(forms.ModelForm):
    class Meta:
        model = ModelA

    def __init__(self, *args, **kwargs):
        super(ModelAAdminForm, self).__init__(*args, **kwargs)
        
        if self.instance.id and self.instance.modelb:
          
            q = Q(active=True)| Q(id=self.instance.modelb.id)
            self.fields['modelb'].queryset = ModelB.objects.filter(q)
            ''' relatedName__ModelFieldName__isnull = True query for available fields only'''
            
        else:
            self.fields['modelb'].queryset = ModelB.objects.filter(active=True)


class ModelAAdmin(admin.ModelAdmin):
    form = ModelAAdminForm
