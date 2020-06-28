from rest_framework import serializers
from codesite.models import Loan, Member,Group,Loan, LoanPayments,Savings

class LoanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loan
        fields = ('loaned_to', 'memberid','total_amount', 'installment_amount','interest','scheme','is_approved', 'duration','duedate' )
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname','address', 'age','group', 'loans','is_credible','birthdate','rank'  )
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name','last_activity','pub_date')
class LoanPaymentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoanPayments
        fields = ('loan','amount','amount_total','interest_paid','is_passdue','transact_date')
class SavingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Savings
        fields = ('memberid','amount','interest','scheme','isapproved','duration','duedate')
