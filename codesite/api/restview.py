from rest_framework import viewsets
from codesite.models import Loan,Member,Group,Savings,LoanPayments
from .  import serialize

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all().order_by('duedate')
    serializer_class = serialize.LoanSerializer
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('rank')
    serializer_class = serialize.MemberSerializer
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = serialize.GroupSerializer
class LoanPaymentsViewSet(viewsets.ModelViewSet):
    queryset = LoanPayments.objects.all().order_by('-transact_date')
    serializer_class = serialize.LoanPaymentsSerializer
class SavingsViewSet(viewsets.ModelViewSet):
    queryset = Savings.objects.all().order_by('-transact_date')
    serializer_class = serialize.SavingsSerializer
