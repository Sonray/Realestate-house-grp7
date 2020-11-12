from django.shortcuts import render

# Create your views here.
# Profile views

class UserProfile:
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        profile_serializer = UserProfileSerializer(UserProfile)
        return Response(profile_serializer.data)