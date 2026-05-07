from rest_framework.permissions import BasePermission, SAFE_METHODS


# from apps.models import Enrollment

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return user.is_authenticated and obj.author == user


class CustomPostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method == 'POST':
            return request.user and request.user.is_authenticated

        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user and request.user.is_staff

        if request.method in ['PUT', 'PATCH']:
            return obj.author == request.user or request.user.is_staff

        return True

# class IsCourseOwnerOrEnrolled(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if hasattr(obj, 'course'):
#             course = obj.course
#             lesson = obj
#         else:
#             course = obj
#             lesson = None
#
#         if course.instructor == request.user:
#             return True
#
#         enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
#
#         if lesson:
#             if enrolled:
#                 return True
#             return lesson.is_preview and request.method in SAFE_METHODS
#
#         return enrolled
