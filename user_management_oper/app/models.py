from django.db import models

# Create your models here.
import  re

# Create your models here.
from django.core.exceptions import ValidationError
def main(value):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)
    mat = re.search(pat, value)
    if mat:
        return mat
    else:
        raise ValidationError("check the password")
class User_register(models.Model):
    Username = models.EmailField(primary_key=True)
    desig = models.CharField(max_length=50)
    password = models.CharField(max_length=30,validators=[main])


