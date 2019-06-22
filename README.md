# BinarizeAnImage
This a straight-forward basic approach to binarize an image using OpenCV and NumPy

## Samples
### Pikatchu 

Input

![alt text](https://github.com/alaabenfatma/BinarizeAnImage/blob/master/pika.png)

Output

![alt text](https://github.com/alaabenfatma/BinarizeAnImage/blob/master/output/pika_bin.png)
### Board

Input

![alt text](https://github.com/alaabenfatma/BinarizeAnImage/blob/master/board.jpg)

Output

![alt text](https://github.com/alaabenfatma/BinarizeAnImage/blob/master/output/board_bin.png)

Imagine this matrix in which 0 represents black pixels. (Other values are irrelevant)

<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;160&space;&&space;0&space;&&space;193&&space;173&space;\\&space;190&space;&&space;0&space;&&space;190&space;&&space;180\\&space;243&&space;0&space;&&space;60&space;&&space;170\\&space;214&&space;0&space;&&space;0&space;&&space;216&space;\end{bmatrix}" title="\begin{bmatrix} 160 & 0 & 193& 173 \\ 190 & 0 & 190 & 180\\ 243& 0 & 60 & 170\\ 214& 0 & 0 & 216 \end{bmatrix}" />

If we look closely, we will notice that the letter L can be spotted.

We convert every every pixel that has a value lesser than 150 into a white one. And we convert to black the rest. Hence, we will end up with the following matrix

<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;0&space;&&space;255&space;&&space;0&&space;0&space;\\&space;0&space;&&space;255&space;&&space;0&space;&&space;0\\&space;0&&space;255&space;&&space;255&space;&&space;0\\&space;0&&space;255&space;&&space;255&space;&&space;0&space;\end{bmatrix}" title="\begin{bmatrix} 0 & 255 & 0& 0 \\ 0 & 255 & 0 & 0\\ 0& 255 & 255 & 0\\ 0& 255 & 255 & 0 \end{bmatrix}" />

| In order to enhance the process of binarizing the picture, it is highly recommended to apply some sort of blurring! This approach gives satisfactory results, albeit being unperfect. |
| --- |
