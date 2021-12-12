from .models import *


def AdminCheck(request):
    user = request.user
    if user.is_authenticated:
        try:
            u = Account.objects.get(user=user)
            if u.type == 'admin':
                return (True)
            else:
                return (False)
        except:
            return (False)
    else:
        return (False)