from rest_framework.permissions import BasePermission


"""
permission #1: être commercial ou gestionnaire
permission #2: être commercial responsable ou être gestionnaire
permission #3: être commercial ou gestionnaire ou support responsable event
permission #4: être gestionnaire (pour tout DELETE)
permission #5: être support responsable event ou être gestionnaire
LISTE AUTORISATIONS:
    /client:
        GET, POST: perm#1
        UPDATE: perm#2
        DELETE: perm#4
        GET 'retrieve': perm#3
    /contract:
        GET: perm#1
        POST: perm#1 (ATTENTION: lié à un client dont le commercial est responsable)
        UPDATE: perm#2
        DELETE: perm#4
        GET 'retrieve': perm#3
    /event:
        GET: perm#1
        POST: perm#1 (ATTENTION: lié au contrat pour un client dont le commercial est responsable)
        UPDATE: perm#5
        DELETE: perm#4
        GET 'retrieve': perm#3  
"""
class CanViewEvents(BasePermission):

    def has_permission(self, request, view):
        if request.method in ["GET", "POST"]:
            return request.user.assignement in ['Commercial', 'Management']
        elif request.method == "PUT":
            return request.user.assignement in ['Commercial', 'Management']
        else:
            return request.user.assignement == "Management"

    def has_object_permission(self, request, view, obj):
        cond1 = request.user.assignement == "Management"
        cond2 = obj.responsible == request.user
        if request.method == "DELETE":
            return cond1
        elif request.method == "PUT":
            return cond1 or cond2
        elif request.method == "GET":
            roles = ['Commercial', 'Management']
            cond3 = request.user.assignement in roles
            return cond2 or cond3
        else:
            # FAUT IL METTRE LE CAS POST ICI COMME DANS HAS_PERMISSION ?
            return False
