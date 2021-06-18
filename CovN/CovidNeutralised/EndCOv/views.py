import os

from django.shortcuts import render
from keras.preprocessing import image
import numpy as np
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

import tensorflow as tf
from tensorflow.keras.models import load_model
import keras
#from tensorflow.python.framework import ops
#from tensorflow.keras import backend
from .forms import *
from .models import Members
# from keras import backend as K

# global graph,modely
# https://help.heroku.com/sharing/80a028d7-6dc6-4dde-aaaf-55cc4ce5028c

# Hii  Sripad,
# The link takes me to https://help.heroku.com/ and there is no article over there.
# And here is the result for the following command :::
# apps:info -a healtec
# h
# === healtech
# Auto Cert Mgmt: false
# Dynos:
# Git URL:        https://git.heroku.com/healtech.git
# Owner:          sahiceooftextbook@gmail.com
# Region:         us
# Repo Size:      0 B
# Slug Size:      0 B
# Stack:          heroku-18
# Web URL:        https://healtech.herokuapp.com/
#
# I don't know why my GitHub repo size is showing 0  here but its actually showing  7.09 MB on GitHub.
# Sorry About the access permission ,  maybe my Organization later allows me to grant you the access.
# Thanks Very Much for the help,
# Best Regards,
# Adarsh
print("Model Loading......HiiiADarsh")
model=load_model('EndCOv/my_model.h5')

print("model loaded sucessfully")


class_dict={'0':'Yes. The Patient is Covid Positive According to the Model.....The Confidence Score out of 1 is = ',
            '3':'No! The Patient Is Covid Negative According to the Model!!....The Confidence Score out of 1 is  = ',
            '2':'The Patient is having Viral Pneumonia and Not Covid .....The Confidence Score out of 1 is = ',
            '1':'The Patient is having Lung Opacity ....The confidence score out of 1 is =',
            }
# {'COVID': 0, 'Lung_Opacity': 1, 'Viral Pneumonia': 2, 'non-COVID': 3}
class_names = list(class_dict.values())

'''def load_modelo
	global model
	model = load_model("XrayApp/my_model.h5")
	global graph
	graph = tf.Graph()
'''

def prediction(request):

    if request.method == 'POST':

        img_file = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)
        uploaded_file_path = fs.path(filename)
        print('absolute file path', uploaded_file_path)



        # f = request.FILES['myfile']
        # file_name = "ransome.png"
        # file_name_2 = default_storage.save(file_name, f)
        # file_url = default_storage.url(file_name_2)
        # file_lo=os.path.abspath(os.path.join(file_url, f))
        # print(file_lo)



        # request.POST.get('is_private', False)
      # myfile=request.FILES['media']
      # myfile = request.FILES.get('Image')
      #   {'COVID': 0, 'Lung_Opacity': 1, 'Viral Pneumonia': 2, 'non-COVID': 3}
     # form = ImageForm(request.POST, request.FILES)
     # if form.is_valid():
     #
     #    form.save(commit=True)
     #    Imag=form.cleaned_data['Image']
     #    print(Imag)
     #    # Img=Members.objects.get(pk=5).Image.url
     #    # print(Img)



        # myfile = 'C:/Users/SHRIKANT/PycharmProjects/CovN/CovidNeutralised/media/media/' +str(request.FILES['Image'])
        # myfile=request.FILES['myfile']
        # print((myfile))
        img = image.load_img(uploaded_file_path, target_size=(64, 64))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255
        # keras.backend.clear_session()
        # graph = tf.Graph()
        model = load_model("EndCOv/my_model.h5")

        # with graph.as_default(): GHar Ka number Lopez!!
        # model = keras.models.load_model('EndCOv/my_model.h5')
        # GHarKaNumber

        preds = model.predict(img)
        # y_classes  = preds.argmax(axis=-1)

        # print(y_classes)
        print("Unflattendee" + str(preds))
        # K.clear_session()
        preds = preds.flatten()
        print(str(preds) + "This is the pred")
        # x = (1 - float(preds[0]))
        # preds = np.append(preds, [x])
        print(preds)
        m = max(preds)
        print(m)
        for index, item in enumerate(preds):
            print(index, item)
            if item == m:
                result = class_names[index] + str(m)
                return render(request, "EndCOv/prediction.html", {
                    'result': result})


      # if form.is_valid():
      #
      #   form.save()


    else:
      form = ImageForm()
      return render(request, 'EndCOv/prediction.html')



    # if request.method == 'POST' and request.FILES['myfile']:
        # post = request.method == 'POST'
        # myfile = request.FILES['myfile']#try using get
        #load_modelo()

    # else:
    #     return render(request, "EndCOv/prediction.html")



def DiagnoseXray (request):
    return render(request,'EndCOv/diagnoseXray.html')
def loginView(request):
    return render(request,'EndCOv/login.html')
