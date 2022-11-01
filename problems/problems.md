# 1. Loss explosion
At late stage of training, loss may explode because the occupying grid is unstabe:

![](loss%20explosion/loss_explosion.png)

This is because the occupying grid is not updating continuously while the network is training. Another reason is that when bounding box is bounding the scene tightly, there is no extra space for the neural network to deal with the inconsistency lighting in different images, so the space in the room is used to fit. Early quit of training is needed, or the threshold (fixed to 0.01 in ngp) should be adjusted for specific scene.

# 2. Unclear renderings
Compared to mipnerf360, instant-ngp's renderings are unclear, especially at edges and detailed textures.

Up is ngp, below is mipnerf360.

<img src="unclear renderings/ngp.jpg" width="600"/>
<img src="unclear renderings/mipnerf360.png" width="600"/>

