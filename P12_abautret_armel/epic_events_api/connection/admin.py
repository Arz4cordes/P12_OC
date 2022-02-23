from django import forms
from django.contrib import admin
from connection.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',
                  'assignement',
                  'first_name',
                  'last_name',
                  'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        if user.assignement == 'Management':
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_superuser = False
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username',
                  'assignement',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_active')


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # which attributes are displayed in the users's list
    list_display = ('username',
                    'assignement',
                    'first_name',
                    'last_name',
                    'email')
    # which filters are displayed aside
    list_filter = ('assignement',)
    # which attributes are displayed when a particular user is displayed
    fieldsets = (
        ('Login informations', {'fields': ('username', 'password')}),
        ('Group', {'fields': ('assignement',)}),
        ('Personal info', {'fields': ('first_name',
                                      'last_name',
                                      'email',
                                      'is_active',)}),
    )
    # which attributes are displayed when adding a new user
    add_fieldsets = (
        ('Personal info', {'classes': ('wide',),
                           'fields': ('first_name',
                                      'last_name',
                                      'email',)}),
        ('Group', {'classes': ('wide',),
                   'fields': ('assignement',)}),
        ('Login informations', {'classes': ('wide',),
                                'fields': ('username', 'password1', 'password2',)})
    )
    # in which attributes an admin can make some search 
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username', 'last_name', 'email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, CustomUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
