from django import forms 
from tasks.models import Task

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
    # একটি ক্লাস সেট করুন যেটা সহজে কাস্টমাইজ করা যায়
    common_class = "border border-gray-400 w-full rounded-md shadow-sm mt-2 mb-4 "
    
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
                    'class': f" bg-gray-50 px-2 py-1 border border-gray-400 rounded-md shadow-sm mb-4"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': "flex flex-col  "  # চেকবক্স গুলো সুন্দর দেখাবে
                })
            else:
                field.widget.attrs.update({
                    'class': self.common_class
                })


# Model form start 
class TaskModelForm(StyleFormMixin ,forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'title' , 'description' , 'due_date' , 'employee' ]
        # exclude = ['project' , 'is_completed' , 'created_at' , 'updated_at']
        widgets = {
        #     'title' : forms.TextInput(attrs={
        #         'class': "border border-gray-400 w-full rounded-sm shadow-sm mt-2 mb-4",
        #         'placeholder': 'Inter your task title.'
        #     }),
        #     'description': forms.Textarea(attrs={
        #         'class' : "border border-gray-500 w-full rounded-sm shadow-sm mt-2 mb-4",
        #         'placeholder': 'Inter task details there .'
        #     }),
            'due_date': forms.SelectDateWidget(attrs={
                'class' : " border border-gray-400 bg-gray-100 rounded-md "
            }),
        #     'employee': forms.CheckboxSelectMultiple(attrs={
        #         'class': "mx-2 font-normal "
        #     })
        }

    def __init__(self, *args, **kwargs):
        super().__init__( *args , **kwargs)
        # StyleFormMixin()
        self.apply_style_widgets()
