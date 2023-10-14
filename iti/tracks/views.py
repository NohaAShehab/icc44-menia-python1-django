from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import View

from tracks.forms import  TrackModelForm
from tracks.models import Track


# Create your views here.


def index(request):
    # tracks = Track.objects.all()
    tracks = Track.get_all_objects()
    return render(request, 'tracks/index.html', context={"tracks": tracks})



def create(request):
    form = TrackModelForm()
    if request.method == 'POST':
        form = TrackModelForm( request.POST, request.FILES)
        if form.is_valid():
            track =form.save() # save object to the database
            return redirect(Track.get_index_url())

    return  render(request, 'tracks/create.html', {'form':form})


# def edit(request, id ):
#     track = Track.get_specific_object(id)
#     form = TrackModelForm(instance=track)
#     if request.method=='POST':
#         form = TrackModelForm(request.POST, request.FILES, instance=track)
#         if form.is_valid():
#             track = form.save()  # save object to the database
#             return redirect(Track.get_index_url())
#
#     return render(request, 'tracks/edit.html', {'form':form})
#


class EditTrackView(View):

    def get(self, request, id):
        track = Track.get_specific_object(id)
        form = TrackModelForm(instance=track)
        return render(request, 'tracks/edit.html', {'form': form})

    def post(self, request, id):
        track = Track.get_specific_object(id)
        form = TrackModelForm(request.POST, request.FILES, instance=track)
        if form.is_valid():
            track = form.save()  # save object to the database
            return redirect(track.get_show_url())

        return render(request, 'tracks/edit.html', {'form': form})

######## views ---> class

class ShowTrack(View):
    # request method --> GET
    def get(self, request, id):
        track = Track.get_specific_object(id)
        return render(request, 'tracks/show.html', {'track':track})

    ## request --> POST
    # def post(self, request, id):
    #     pass



