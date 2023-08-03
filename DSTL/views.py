from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('datastory_datastory_list_urlpattern')
