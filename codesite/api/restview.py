from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
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

    # @action(detail=False, methods=['get'])
    # def list_passdue(self, request):
    #     queryset = Savings.objects.all().order_by('-transact_date')
    #     savings = get_object_or_404(queryset)
    #     serializer = serialize.SavingsSerializer(savings)
    #     return Response(serializer.data)
# # @action(detail=False, methods=['get'])
# class SavingsDueViewSet(viewsets.ViewSet):
#     queryset = Savings.objects.all().order_by('-transact_date')
#     serializer_class = serialize.SavingsSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
# @api_view(['GET'])
# # # other decorators if required
# # @permission_classes([IsAuthenticated])
# def savings_due(request):
#     serializer = serialize.SavingsSerializer
#     queryset = Savings.objects.all().order_by('-transact_date')
#     return Response(serializer.errors)
# # function based urls.py

class SavingsDueList(APIView):
    def get(self, request, format=None):
        savings =  Savings.objects.all().order_by('-transact_date')
        serializer = serialize.SavingsSerializer(savings)
        return Response(serializer.data)
