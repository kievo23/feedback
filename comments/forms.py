from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = {
			'comment',
			'first_name',
			'second_name',			
			'phone',
			'company_id'			
		}
	
	def __init__(self, *args, **kw):
		super(CommentForm, self).__init__(*args, **kw)
		self.fields.keyOrder = ['first_name','second_name','phone','comment','company_id']


