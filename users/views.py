import requests
from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from coupons.models import Coupon
from users.models import User
from . import serializers


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Users(APIView):  # 유저 생성 # django에서 유니크를 알아서 판단해주기 때문에 password만 있으면 생성가능
    def post(self, request):
        username = request.data.get("username")
        if User.objects.filter(username=username).exists():
            print(User.objects.get(username=username))
            return Response({"detail": "same username"})
        else:
            password = request.data.get("password")
            serializer = serializers.UserCreateSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                user.set_password(password)
                user.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        # old_password, new_password는 django에서 해주나봐
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

            
class LogIn(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )  # 로그인 정보가 유효하면 authentcate함수는 user객체를 반환
        if user:
            login(request, user)
            return Response({"ok": "welcome!"})
        else:
            return Response(
                {"error": "wrong password"}, status=status.HTTP_400_BAD_REQUEST
            )


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"logout ok": "bye bye"})


class UserCoupon(APIView):
    def get(self, request):
        user = request.user
        time = timezone.now() - timedelta(hours=1)
        print(time)
        if Coupon.objects.filter(user=user, created_at__gt=time).exists():
            return Response({"exists": True})
        else:
            return Response({"exists": False})


    def post(self, request):
        serializer = serializers.CouponSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            coupon = serializer.save(
                user = request.user
            )
            serializer = serializers.CouponSerializer(coupon)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class GithubLogin(APIView):
    def post(self, request):
        try:
            code = request.data.get("code") # url에서 ?code={code}를 받아오네
            access_token = requests.post(
                f"https://github.com/login/oauth/access_token?code={code}&client_id=384d5b15fea1a357b00c&client_secret={settings.GH_SECRET}",
                headers={"Accept": "application/json"},
            )   # url에 "code"를 넣고 github로 부터 access token과 교환한다.
            access_token = access_token.json().get("access_token") # access 토큰을 얻었다.
            user_data = requests.get(
                "https://api.github.com/user",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_data = user_data.json()

            user_emails = requests.get(
                "https://api.github.com/user/emails",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            print(user_emails.json())
            user_emails = user_emails.json()

            # user의 email이 없으면 sign up이고 email이 있으면 로그인이다.
            try:
                user = User.objects.get(email=user_emails[0]["email"])
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            except User.DoesNotExist:
                user = User.objects.create(
                    username=user_emails[0]["email"],
                    email=user_emails[0]["email"],
                    name=user_data.get("name"),
                    avator=user_data.get("avatar_url"),
                )
                user.set_unusable_password()  # .has_usable_password도 있다.
                user.save()  # 유저를 저장하고
                login(request, user)  # 바로 로그인 시켜주기
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CF_GetUploadURL(APIView):
    def post(self, request):
        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        one_time_url = requests.post(url, headers={
            "Authorization": f"Bearer {settings.CF_TOKEN}"
            },
        )
        one_time_url = one_time_url.json()
        result = one_time_url.get("result")
        return Response({"uploadURL": result.get("uploadURL")})
