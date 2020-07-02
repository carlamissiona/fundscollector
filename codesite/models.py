from django.db import models
from decimal import Decimal


class Group(models.Model):
    name = models.CharField(max_length=100, default ="None")
    last_activity = models.DateTimeField('Date of last activity', auto_now_add=True)
    pub_date = models.DateTimeField('Publish date', auto_now_add=True)

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,null=True)
    loans = models.CharField(max_length=255)
    is_credible = models.BooleanField()
    rank = models.IntegerField()
    birthdate = models.DateTimeField('Birthdate',null=True)


class Loan(models.Model):
    loaned_to = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    memberid = models.CharField(max_length=40)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2, default=Decimal('0.0000'))
    installment_amount = models.DecimalField(max_digits=10,decimal_places=2, default=Decimal('0.0000'))
    scheme = models.CharField(max_length=100)
    interest = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.0000'))
    is_approved = models.BooleanField(default=False, null=True)
    duration =  models.CharField(max_length=100, null=True)
    duedate = models.DateTimeField('Loan Due Date',null=True)

class LoanPayments(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.0000'))
    amount_total = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.0000'))
    interest_paid = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.0000'))
    is_passdue = models.BooleanField()
    duedate = models.DateTimeField('Loan Due Date',null=True)
    transact_date = models.DateTimeField('Transact Date',null=True)

class Savings(models.Model):
    memberid = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.0000'))
    interest = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.0000'))
    scheme = models.CharField(max_length=100)
    isapproved = models.CharField(max_length=100)
    duration =  models.CharField(max_length=100, null=True)
    duedate = models.DateField('Loan Due Date', null=True )
    transact_date = models.DateTimeField('Transact Date',auto_now_add=True, null= True)


# class Member(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     age = models.CharField(max_length=100)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     loans = models.CharField(max_length=255)
#     is_credible = models.BooleanField()
#     latest_rank = models.IntegerField()
#     birthdate = models.DateTimeField('Birthdate',null=True)
#
# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     last_activity = models.DateTimeField('Date of last activity', auto_now_add=True)
#     pub_date = models.DateTimeField('Publish date', auto_now_add=True)


#     pub_date = models.DateTimeField('Publish Date', auto_now_add=True)
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=40)
#     pub_date = models.DateTimeField('publish date', auto_now_add=True)
#
#
#
# class Field(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=40)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField('publish date',auto_now_add=True)
