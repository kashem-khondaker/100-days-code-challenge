from django import forms 
from tasks.models import Task , taskDetails

# Django form -- this is basic
class TaskForm(forms.Form):
    title = forms.CharField(max_length=200 , label="Title")
    description = forms.CharField(
        widget=forms.Textarea,
        label="Task Description "
    )
    due_date = forms.DateField(
        widget=forms.SelectDateWidget ,
        label="Due Date "
    )
    employee = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="Employee ",
        choices=[]
    )

    def __init__(self,*args , **kwargs):
        print(args , kwargs)
        employee = kwargs.pop("employee" , [])
        super().__init__( *args , **kwargs)
        print(self.fields)
        self.fields['employee'].choices = [(emp.id , emp.name) for emp in employee]

# class StyleFormMixin:

#     common_class = "border border-gray-400 w-full rounded-sm shadow-sm mt-2 mb-4",
    
#     def apply_style_widgets(self):
#         for field_name , field in self.fields.items():
#             if isinstance(field.widget , forms.TextInput):
#                 field.widget.attrs.update({
#                     'class' : self.common_class,
#                     'placeholder' : f"Enter {field.label.lower()}"
#                 })
#             elif isinstance(field.widget , forms.Textarea):
#                 field.widget.attrs.update({
#                     'class':self.common_class,
#                     'placeholder': f"Enter {field.label.lower()}",
#                     'rows': 5
#                 })
#             elif isinstance(field.widget , forms.CheckboxSelectMultiple):
#                 field.widget.attrs.update({
#                     'class' : self.common_class
#                 })


class StyleFormMixin:
    common_class = "border border-gray-400 w-full rounded-md shadow-lg mt-2 mb-4 "
    
    def apply_style_widgets(self):
        for field_name, field in self.fields.items():
            # print(field )
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.common_class,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.common_class,
                    'placeholder': f"Enter {field.label.lower()}",
                    'rows': 5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': f" bg-gray-100 px-2 py-1 border border-gray-400 rounded-md shadow-lg mb-4"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': f" rounded-md  mt-2 mb-4  " 
                })
            else:
                field.widget.attrs.update({
                    'class': self.common_class
                })

class TaskModelForm(StyleFormMixin ,forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'title' , 'description' , 'due_date' , 'employee' ]
        # exclude = ['project' , 'is_completed' , 'created_at' , 'updated_at']
        widgets = {
            'due_date': forms.SelectDateWidget,
            'employee': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__( *args , **kwargs)
        self.apply_style_widgets()

class TaskDetailsModelForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = taskDetails
        fields = ['priority','notes']
    
    def __init__(self, *args, **kwargs):
        super().__init__( *args , **kwargs)
        # StyleFormMixin()
        self.apply_style_widgets()
