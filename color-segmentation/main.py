import os
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st
import cv2
from PIL import Image
import colorsys
from PIL import ImageColor

bcolor = st.sidebar.beta_color_picker(label='bottom')
ucolor = st.sidebar.beta_color_picker(label='upper')

image = st.file_uploader(label='images', type=['png', 'jpg', 'jpeg'])
image = np.array(Image.open(image))
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
st.image(image)


def get_b(color):
    rgb = ImageColor.getcolor(color, "RGB")
    r,g,b = rgb
    h,s,v = colorsys.rgb_to_hsv(int(r)/255,int(g)/255,int(b)/255)
    h,s,v = int(h*255),int(s*255),int(v*255)
    return h,s,v

h1,s1,v1 = get_b(bcolor)
h2,s2,v2 = get_b(ucolor)

h1,s1,v1
h2,s2,v2

# l = st.text_input(label='rgb0', value='2 2 2').split(' ')
# if len(l)==3:
#     r,g,b = l
#     r,g,b
#     h,s,v = colorsys.rgb_to_hsv(int(r)/255,int(g)/255,int(b)/255)
#     h,s,v = int(h*255),int(s*255),int(v*255)


# bh = st.sidebar.slider(label='bottom H', min_value=0, max_value=255, value=h)
# bc = st.sidebar.slider(label='bottom C', min_value=0, max_value=255, value=s)
# bv = st.sidebar.slider(label='bottom V', min_value=0, max_value=255, value=v)

# l = st.text_input(label='rgb1', value='2 2 2').split(' ')
# if len(l)==3:
#     r,g,b = l
#     r,g,b
#     h,s,v = colorsys.rgb_to_hsv(int(r)/255,int(g)/255,int(b)/255)
#     h,s,v = int(h*255),int(s*255),int(v*255)

# uh = st.sidebar.slider(label='upper H', min_value=0, max_value=255, value=h)
# uc = st.sidebar.slider(label='upper C', min_value=0, max_value=255, value=s)
# uv = st.sidebar.slider(label='upper V', min_value=0, max_value=255, value=v)





hsv_min = np.array([h1, s1, v1], np.uint8)
hsv_max = np.array([h2, s2, v2], np.uint8)


thresh = cv2.inRange(hsv, hsv_min, hsv_max)

st.image(thresh)


# https://github.com/swiftcarrot/react-input-color


st.components.v1.html(html='<a href="https://www.yandex.ru">google</a>', width=None, height=None, scrolling=False)

import streamlit.components.v1 as components

components.declare_component('here', 'here.html')