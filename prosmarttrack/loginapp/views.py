import json
from django.shortcuts import redirect, render
from django.views import View
from .models import Token, Userprofile
from django.contrib.auth import authenticate
from django.contrib import messages


class UserLogin(View):
    template_name ="administrator/login.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
                        "ADMIN": "dashboard_page",
                        "INSTITUTE":"user:loadinstitute",
                        "TEACHER":"user:loadteacher",
                    }
        username = request.POST.get("username")
        password = request.POST.get("password")
        authenticated = authenticate(username=username, password=password)
        try:
            user = Userprofile.objects.get(username=username)
            print("hel")
        except Userprofile.DoesNotExist:
            response_dict[
                            "reason"
                        ] = "No account found for this username. Please signup."
            messages.error(request, response_dict["reason"])
        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            return redirect(request.GET.get("from") or "login")

        else:
            print("hello")
            session_dict = {"real_user": authenticated.id}
            token, c = Token.objects.get_or_create(
                        user=user, defaults={"session_dict": json.dumps(session_dict)}
                        )

            user_type = authenticated.user_type
            print("hai")
            print(user)
            print(user_type)

            return redirect(landing_page_url[user_type])
        return redirect(request.GET.get("from") or "login")