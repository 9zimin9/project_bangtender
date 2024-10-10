from django.shortcuts import render

# 메인 페이지
def index(request):
    return render(request, 'index.html')

# 주류 목록 페이지 (위스키, 럼 등)
def liquor_list(request):
    return render(request, 'liquor_list.html')

# 칵테일 목록 페이지
def cocktail_list(request):
    return render(request, 'cocktail_list.html')

# 방텐더봇 페이지
def bot(request):
    return render(request, 'bot.html')

# 주변 매장 찾기 페이지
def store_locator(request):
    return render(request, 'store_locator.html')

# 프로필 페이지
def profile(request):
    return render(request, 'profile.html')

