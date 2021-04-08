from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
import uuid
# Create your models here.

EVENT_CHOICES = (
    ("Deposit","Deposit"),
    ("Withdraw","Withdraw"),
    ("Enquiry","Enquiry")
    )
ACCOUNT_STATUS = (
    ("Active","Active"),
    ("Deactive","Deactive")
    )
class account(models.Model):
    """ User account information with History """
    account_no= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    event = models.CharField(max_length=20,choices=EVENT_CHOICES)
    created_by = models.ForeignKey(User,related_name="create_user",on_delete=models.DO_NOTHING)
    modified_by = models.ForeignKey(User,related_name="modified_user",on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=ACCOUNT_STATUS,default="Active")
    history = HistoricalRecords()


    def __str__(self):
        return self.user.username

