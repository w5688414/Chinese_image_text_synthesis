# Chinese_image_text_synthesis
experiments

1.框架基本形成，后面用它来产生训练样例，用于ocr定位与识别

2.产生的图片背景基本上为白色，本人需要的训练样例是文字的位置

3.输出的文件在output文件夹下

    groundtruth为图片文字的位置信息

    images为生成的图片

## usage

for image generation

```
pyhon3 picture_gen.py
```

convert data format to voc2007 data format

```
python3 pascal_voc_convert.py
```

# environments
- python 3.7
- mac system
- Pillow   5.3.0
- opencv 3.4

