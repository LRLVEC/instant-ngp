# 1. Todo
**Note: release branch is used to developing future features, no new or legacy branches will be used**

Planning:
1. UE5 plugin (edit)
2. mipnerf
3. big scene
4. aabb fit for scenes
   1. cube
   2. cuboid
   3. unbounded
## 1.1. MipNeRF360
1. change how cursor applys to the camera pos: testbed.cu: 1335, mouse_drag -- Done
2. use s instead of t as the m in dist loss, define s -- Done
3. malloc gpu mem for the computation of cumsum of w and w*m -- Done
4. calculate distortion loss and its grad -- Done
5. add opacity loss -- Done
6. add random rays starting from positions outside the aabb -- Done
   1. add function generate_extra_training_samples_nerf -- Done
   2. add function compute_extra_ray_loss_kernel_train_nerf -- Done
   3. add function train_extra_nerf_step -- Done
   4. modify fucntion train_nerf -- Done
7. test the effect of dist loss and opacity loss, compare with native ngp
   1. render full images and video for test
   2. calculate psnr
8. change multiple optimizer_step calls into one (merge batches)
9. change opacity loss to see effects

### 1.1.1. Ideas
1. add unbounded scene encoding as mipnerf360 for ngp?
2. add decay for distortion loss scale and opacity loss scale so they may converge faster?
   1. no, use 0.01 for distortion loss scale and 0.001 for opacity loss scale constantly
   2. otherwise, they effect of the loss will decay
3. sample extra rays according to the density grid may be helpful?
   1. not very necessary since the sample num is the same

## 1.2. RegNeRF
1. calculate gradients for geometry loss in regnerf -- Done
2. sample a patch of rays instead of single ray, geometry loss will not calculate on original rays
   1. generate sample patches, including direction, starting point etc. Strategies for generating patches:
      1. <font color=red>adaptively select average depth from camera</font> (store depth in a map?)
      2. the origin point should be near a camera with small offset, offset is proportional to scene size
      3. the end point should be selected randomly according to depth map of a camera
      4. the spacing between rays in a patch is calculated by average depth and camera fov
   2. generate rays from patches using a block of threads to generate a patch of rays
3. compute loss and its gradients
   1. image_idx_regnerf: generate image index for each patch
   2. generate_training_patches_regnerf: output patch_pos (float: img, x, y)
   3. generate_training_samples_regnerf
   4. compute_loss_kernel_train_regnerf
   5. train_regnerf_step

patch size: 1-16, so max pixel num is 256, reasonable for a thread block

regnerf buffers:
1. patch_pos (global): record img id and xy position
2. (shared)

## 1.3. MultiGPU
1. pixel streaming on multi-gpu

## 1.4. pyngp
The searching of pyngp library which is *.pyd or *.so should match the version of ngp since there are multiple version of ngp under folder build.