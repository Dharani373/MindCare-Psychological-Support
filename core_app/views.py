from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import StressQuestion,StressResponse, StressAssessment,SupportChat,UserProfile
from ml_models.predict_sentiment import predict_sentiment
from .utils import is_crisis_message



def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("signup")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "core_app/signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "core_app/login.html",
                {"error": "Invalid credentials"}
            )

    return render(request, "core_app/login.html")

@login_required(login_url="login")
def home_view(request):
    return render(request, "core_app/home.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def stress_check_view(request):
    questions = StressQuestion.objects.all()

    if request.method == "POST":
        total_score = 0

        for question in questions:
            value = request.POST.get(f"q{question.id}")

            if value is None:
                return render(request, "core_app/stress_check.html", {
                    "questions": questions,
                    "error": "Please answer all questions."
                })

            total_score += int(value)

        #  Calculate stress level
        if total_score <= 13:
            stress_level = "Low"
            stress_class = "low"
        elif total_score <= 26:
            stress_level = "Moderate"
            stress_class = "medium"
        else:
            stress_level = "High"
            stress_class = "high"

        # SAVE TO DATABASE (THIS WAS MISSING)
        StressResponse.objects.create(
            user=request.user,
            total_score=total_score,
            stress_level=stress_level
        )

        # 🔹 Render result
        return render(request, "core_app/stress_result.html", {
            "score": total_score,
            "stress_level": stress_level,
            "stress_class": stress_class
        })

    return render(request, "core_app/stress_check.html", {
        "questions": questions
    })

@login_required
def stress_result_view(request):
    score = request.session.get("stress_score", 0)

    if score <= 13:
        level = "Low Stress"
    elif score <= 26:
        level = "Moderate Stress"
    else:
        level = "High Stress"

    return render(request, "core_app/stress_result.html", {
        "score": score,
        "level": level
    })

@login_required
def stress_history_view(request):
    assessments = StressAssessment.objects.filter(
        user=request.user
    ).order_by("created_at")

    dates = [a.created_at.strftime("%d %b") for a in assessments]
    scores = [a.score for a in assessments] 

    return render(request, "core_app/stress_history.html", {
        "dates": dates,
        "scores": scores,
        "assessments": assessments
    })

@login_required
def ai_support_view(request):
    chats = SupportChat.objects.filter(
        user=request.user
    ).order_by("created_at")

    if request.method == "POST":
        user_message = request.POST.get("message")

        if user_message:
            # save user message
            SupportChat.objects.create(
                user=request.user,
                sender="user",
                message=user_message
            )

            # crisis check
            if is_crisis_message(user_message):
                bot_reply = (
                    "🚨 I’m really glad you reached out. You are not alone.\n\n"
                    "If you are feeling unsafe right now, please contact:\n\n"
                    "AASRA: 91-22-27546669\n"
                    "Kiran (24x7): 1800-599-0019\n\n"
                    "Please reach out to someone you trust."
                )
                crisis_flag = True
            else:
                sentiment = predict_sentiment(user_message)
                crisis_flag = False

                if sentiment == "negative":
                    bot_reply = "I’m really sorry you’re feeling this way 💙"
                elif sentiment == "neutral":
                    bot_reply = "Thanks for sharing 💙 I’m here to listen."
                else:
                    bot_reply = "That’s great to hear 🌱"

            # save bot message
            SupportChat.objects.create(
                user=request.user,
                sender="bot",
                message=bot_reply,
                is_crisis=crisis_flag
            )

            return redirect("ai_support")

    return render(request, "core_app/ai_support.html", {
        "chats": chats
    })


@login_required
def resources_view(request):
    return render(request, "core_app/resources.html")

@login_required
def find_doctors_view(request):
    return render(request, "core_app/find_doctors.html")

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name")
        profile.profession = request.POST.get("profession")

        dob = request.POST.get("date_of_birth")
        if dob:
            profile.date_of_birth = dob

        if "profile_photo" in request.FILES:
            profile.profile_photo = request.FILES["profile_photo"]

        profile.save()

    return render(request, "core_app/profile.html", {
        "profile": profile
    })
