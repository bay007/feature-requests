from django import forms

from .models import Comment, Feature


class FeatureForm(forms.ModelForm):
    """Formulario para crear nuevas solicitudes de funcionalidades."""
    class Meta:
        model = Feature
        fields = ['title', 'description', 'additional_context']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-purple rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-purple rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 4}),
            'additional_context': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-purple rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 4, 'placeholder': 'Contexto adicional (opcional)'}),
        }
        labels = {
            'title': 'Título de la Funcionalidad',
            'description': 'Descripción de la Funcionalidad',
            'additional_context': 'Contexto Adicional (Opcional)',
        }


class CommentForm(forms.ModelForm):
    """Formulario para añadir comentarios a las solicitudes de funcionalidades."""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-purple rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 3, 'placeholder': 'Añade tus ideas sobre esta funcionalidad...'}),
        }
        labels = {
            'content': 'Tu Comentario',
        }
